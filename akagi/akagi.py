import os

os.environ["LOGURU_AUTOINIT"] = "False"

import sys
import time
import traceback
import requests
from threading import Thread

from .logger import logger
from .libriichi_helper import meta_to_recommend
from mitm.client import Client
from mjai_bot.bot import AkagiBot
from mjai_bot.controller import Controller
from settings.settings import settings

# Global variables
mitm_client: Client = None
mjai_controller: Controller = None
mjai_bot: AkagiBot = None


class AkagiApp:
    """
    Main application class for Akagi (non-TUI version).
    Handles MITM proxy and AI bot.
    """

    def __init__(self):
        """Initializes the Akagi application."""
        pass

    def main_loop(self) -> None:
        """
        Main processing loop.
        Fetches messages from MITM client, gets recommendations, and performs actions.
        """
        try:
            global mitm_client, mjai_controller, mjai_bot, settings
            if not mitm_client.running:
                return

            mjai_msgs = mitm_client.dump_messages()
            if mjai_msgs:
                mjai_response = mjai_controller.react(mjai_msgs)
                logger.debug(f"<- {mjai_response}")
                mjai_bot.react(input_list=mjai_msgs)
                self.update_recommandation(mjai_response)

                can_act_4p = (mjai_response["type"] != "none" or mjai_bot.can_act) and (not mjai_bot.is_3p)
                can_act_3p = (mjai_response["type"] != "none" or mjai_bot.can_act_3p) and (mjai_bot.is_3p)


        except Exception:
            logger.error(f"Error in main loop: {traceback.format_exc()}")

    def update_recommandation(self, mjai_msg: dict) -> None:
        """
        Updates recommendation based on MJAI message and sends it to the frontend.
        """
        global mjai_bot
        if "meta" not in mjai_msg or "q_values" not in mjai_msg["meta"]:
            return

        meta = mjai_msg["meta"]
        recommands: list[tuple[str, float]] = meta_to_recommend(meta, mjai_bot.is_3p)
        
        thread = Thread(target=self.send_to_frontend, args=(recommands, mjai_bot))
        thread.start()

    def send_to_frontend(self, recommendations: list[tuple[str, float]], bot: AkagiBot):
        """
        Formats and sends recommendation data to the frontend server.
        """
        try:
            formatted_data = []
            last_kawa_tile = bot.last_kawa_tile

            for r in recommendations:
                action, confidence = r
                confidence = float(confidence)
                rec_data = {"action": action, "confidence": confidence}

                if action in ("chi_low", "chi_mid", "chi_high"):
                    chi_candidates = bot.find_chi_candidates_simple()
                    if action == "chi_low":
                        assert bot.can_chi_low and chi_candidates.chi_low_meld is not None
                        rec_data["tile"], rec_data["consumed"] = chi_candidates.chi_low_meld
                    elif action == "chi_mid":
                        assert bot.can_chi_mid and chi_candidates.chi_mid_meld is not None
                        rec_data["tile"], rec_data["consumed"] = chi_candidates.chi_mid_meld
                    elif action == "chi_high":
                        assert bot.can_chi_high and chi_candidates.chi_high_meld is not None
                        rec_data["tile"], rec_data["consumed"] = chi_candidates.chi_high_meld
                elif action == "pon":
                    assert bot.can_pon
                    rec_data["tile"] = last_kawa_tile
                    rec_data["consumed"] = [last_kawa_tile[:2]] * 2
                elif action == "kan_select":
                    assert bot.can_kan
                    if bot.can_daiminkan:
                        rec_data["tile"] = last_kawa_tile
                        rec_data["consumed"] = [last_kawa_tile[:2]] * 3
                
                formatted_data.append(rec_data)

            payload = {
                "type": "recommandations",
                "data": {
                    "recommendations": formatted_data,
                    "tehai": bot.tehai_mjai,
                    "last_kawa_tile": bot.last_kawa_tile,
                },
            }

            logger.debug(f"Sending recommendation to http://{settings.frontend.host}:{settings.frontend.port}:\n{payload}")
            username = os.environ.get('AKAGI_AUTH_USERNAME')
            password = os.environ.get('AKAGI_AUTH_PASSWORD')
            auth = (username, password) if username and password else None
            res = requests.post(f"http://{settings.frontend.host}:{settings.frontend.port}/update", json=payload, timeout=1, proxies={}, auth=auth)
            res.raise_for_status()
        except Exception:
            logger.error(f"Error sending recommendation to frontend: {traceback.format_exc()}")



def main():
    """
    Main entry point for Akagi.
    Initializes components and runs the main loop.
    """
    global mitm_client, mjai_controller, mjai_bot, settings

    logger.info("Starting Akagi...")
    logger.info(f"MITM Proxy: {settings.mitm.host}:{settings.mitm.port} ({settings.mitm.type})")
    
    mitm_client = Client()
    mjai_controller = Controller()
    mjai_bot = AkagiBot()

    logger.info("Starting Akagi main loop...")
    app = AkagiApp()
    
    if not mitm_client.running:
        mitm_client.start()

    try:
        while True:
            app.main_loop()
            time.sleep(1 / 20)
    except KeyboardInterrupt:
        logger.info("Stopping Akagi...")
    finally:
        if mitm_client and mitm_client.running:
            mitm_client.stop()
        logger.info("Akagi stopped")
        sys.exit(0)
