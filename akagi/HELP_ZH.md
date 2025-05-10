# Akagi

加入 [Discord 社群](https://discord.gg/Z2wjXUK8bN) 以獲得支援與更新資訊。

邀請連結: https://discord.gg/Z2wjXUK8bN

### YouTube 教學
[安裝與設定Akagi](https://youtu.be/Z88Ncxbe2nw)
https://youtu.be/Z88Ncxbe2nw

## 操作指南

1. **安裝 Visual C++ Redistributables**
   1. 首先，確保你使用的是管理員權限的 PowerShell。找到 PowerShell，右鍵點擊快捷方式並選擇 `以管理員身份執行`
   2. 複製並粘貼以下命令到 PowerShell 並按 Enter:
      > Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://vcredist.com/install.ps1'))
   3. 這將下載並安裝最新的 Visual C++ Redistributables。
   4. 安裝完成後，重新啟動電腦。
   5. 以上教學來自 [vcredist.com](https://vcredist.com/quick/)

2. **檢查設定與 AI 模型**
   1. 選擇模型
      - 點選左下角的「Model」按鈕
      - 從清單中選擇一個模型
      - 若沒有模型，可從 [Discord](https://discord.gg/Z2wjXUK8bN) 取得
      - 內建預設模型為弱 AI
      - __3 人對局請選 3P 模型！__
      - __不要用 4P 模型參與 3 人對局！__
   2. 檢查設定
      - 點選左下角的「Settings」按鈕
      - 檢查設定是否正確
      - 將 MITM 類型設定為你正在玩的遊戲
      - 設定正確的 MITM Host與Port
      - 若不清楚，請保留預設值
      - 預設值: (host: 127.0.0.1) (port: 7880)
      - 若你有取得線上伺服器 API 金鑰，請在設定中輸入
      - 線上伺服器提供更強的 AI 模型
      - 可從 [Discord](https://discord.gg/Z2wjXUK8bN) 取得 API 金鑰
   3. 儲存設定
      - 點選「Save」按鈕
      - 將設定儲存下來
   4. 重新啟動 Akagi
      - 關閉 Akagi 並重新開啟
      - 設定才會套用
   5. 啟動 MITM
      - 點選左下角的「MITM Stopped」按鈕
      - 這會啟動 MITM 代理伺服器

3. **安裝 MITM Proxy 憑證**
   1. 開啟檔案總管（按下 `Windows 鍵 + E`）
   2. 在上方地址欄輸入 `%USERPROFILE%\.mitmproxy` 然後按 Enter
   3. 找到名為 `mitmproxy-ca-cert.cer` 的檔案
   4. 雙擊該檔案
   5. 點選「安裝憑證」按鈕
   6. 若出現選項，請選「本機電腦」，然後點選「下一步」
   7. 選擇「將所有憑證放入下列存放區」，然後點「瀏覽...」
   8. 選「受信任的根憑證授權單位」，按下 OK，再點選「下一步」與「完成」
   9. 若系統要求權限，請點選「是」

4. **Proxifier 設定**
   1. 開啟 Proxifier 並前往「Profile」>「Proxy Servers...」
   2. 點選「Add...」，並輸入以下資訊：
      - 地址: 預設為 127.0.0.1
      - 埠號: 預設為 7880
      - 協定: HTTPS
   3. 點選「OK」儲存代理設定
   4. 前往「Profile」>「Proxification Rules...」
   5. 點選「Add...」新增一條規則
   6. 在「Applications」頁籤點選「Browse...」並選擇遊戲執行檔
      - 以雀魂（Mahjong Soul）Steam 版為例:
        - 到 Steam 資料庫中找到遊戲
        - 點選管理按鈕（齒輪圖示）並選擇「瀏覽本機檔案...」
        - 這會開啟遊戲安裝資料夾
        - 你應該能找到雀魂的執行黨 (`Jantama_MahjongSoul.exe`).
        - 若使用其他平台，請尋找相似的選項
      - 雀魂（Mahjong Soul）網頁版:
        - 遊戲執行檔為 `chrome.exe` 或 `firefox.exe`
        - 注意：這樣會導致所有 Chrome 或 Firefox 流量都經過代理
   7. 「Target Hosts」可維持預設
   8. 「Action」選擇剛新增的代理伺服器
   9. 點選「OK」儲存規則

5. **啟動遊戲用戶端**
6. **加入對局**
7. **檢查 Akagi**
   1. 現在你應該能看到 AI 實時分析對局
   2. 若沒有，請檢查設定與 Proxifier 設定
   3. 或是檢查Logs，看看是否有錯誤訊息
   4. 若有錯誤訊息，可以到 [Discord](https://discord.gg/Z2wjXUK8bN) 尋求協助

## 疑難排解

開發中。
請至 [Discord](https://discord.gg/Z2wjXUK8bN) 尋求協助。
