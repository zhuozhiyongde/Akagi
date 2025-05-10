# Akagi

Join the Akagi community on [Discord](https://discord.gg/Z2wjXUK8bN) for support and updates.

Invite Link: https://discord.gg/Z2wjXUK8bN

### Youtube Tutorial
[Akagi Setup Guide](https://youtu.be/Z88Ncxbe2nw)
https://youtu.be/Z88Ncxbe2nw

## Step by step guide

0. **Install Visual C++ Redistributables**
   1. First, ensure that you are using a PowerShell as an administrator. Find PowerShell in the Start menu, right-click on the shortcut and choose `Run as Administrator`
   2. Copy and paste the following command into PowerShell and press Enter:
      > Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://vcredist.com/install.ps1'))
   3. This will download and install the latest Visual C++ Redistributables.
   4. Restart your computer after the installation is complete.
   5. Instructions above are from [vcredist.com](https://vcredist.com/quick/)

1. **Check your settings and AI Model.**
   1. Select a Model.
      - By clicking on the "Model" button in the bottom left corner.
      - Select a model from the list.
      - If you don't have a model, get it from [Discord](https://discord.gg/Z2wjXUK8bN).
      - Builtin default model is weak AI.
      - __Choose 3P model for 3P game!__
      - __Do not join 3P game with 4P model!__
   2. Check your settings.
      - By clicking on the "Settings" button in the bottom left corner.
      - Check your settings and make sure they are correct.
      - Set the MITM type to the game you are playing.
      - Set the MITM host and port to the correct values.
      - If you don't know what to set, leave it as default.
      - Default: (host: 127.0.0.1) (port: 7880)
      - If you have got a Online server API key, set it in the settings.
      - Online server provides a stronger AI model.
      - You can get the API key from [Discord](https://discord.gg/Z2wjXUK8bN).
   3. Save your settings.
      - By clicking on the "Save" button.
      - This will save your settings.
   4. Restart Akagi.
      - Close Akagi and open it again.
      - This will apply the settings.
   5. Start MITM.
      - By clicking on the "MITM Stopped" button in the bottom left corner.
      - This will start the MITM proxy server.
2. **Install MITM Proxy Certificate.**
   1. Open File Explorer (press `Windows key + E`)
   2. In the address bar at the top, type: `%USERPROFILE%\.mitmproxy` and press Enter.
   3. Look for a file called `mitmproxy-ca-cert.cer`.
   4. Double-click on the `mitmproxy-ca-cert.cer` file.
   5. Click the "__Install Certificate__" button.
   6. If you see a choice, select "__Local Machine__" and click "Next".
   7. Choose "__Place all certificates in the following store__", then click "__Browse...__"
   8. Select "__Trusted Root Certification Authorities__", click OK, then click "Next" and "Finish".
   9. If you're asked for permission, click "Yes".
3. **Proxifier Setup**
   1. Open Proxifier and go to "Profile" > "Proxy Servers..."
   2. Click "Add..." and enter the following:
      - Address: The host you set in Akagi settings (default: `127.0.0.1`)
      - Port: The port you set in Akagi settings (default: `7880`)
      - Protocol: HTTPS
   3. Click "OK" to save the proxy settings.
   4. Go to "Profile" > "Proxification Rules..."
   5. Add a new rule by clicking "Add..."
   6. In the "Applications" tab, click "Browse..." and select the game executable.
      - This is usually located in the game installation folder.
      - For example, for Mahjong Soul Steam version:
        - Browse to your game in Steam library.
        - Click the manage button (gear icon) and select "Browse local files..."
        - This will open the game installation folder.
        - You should see the game executable file (e.g., `Jantama_MahjongSoul.exe`).
      - For web version, you can use the browser executable (e.g., `chrome.exe` or `firefox.exe`).
   7. In the "Target Hosts" tab, you can leave it default.
   8. In the "Action" tab, select the proxy server you just added.
   9. Click "OK" to save the rule.
4. **Start the game client.**
   - Launch the game client (e.g., Mahjong Soul) and log in.
5. **Join a game.**
   - Join a game as you normally would.
6. **Check Akagi.**
   - You should see the AI analyzing the game in real-time.
   - If you see any errors, check the Logs for more information.
   - Or ask for help in the [Discord](https://discord.gg/Z2wjXUK8bN) server.

## Troubleshooting

WIP.

Ask for help in the [Discord](https://discord.gg/Z2wjXUK8bN) server.
