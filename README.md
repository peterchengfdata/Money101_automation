# Python 環境設定教學

## 安裝 Python

1. 開啟瀏覽器，前往 [Python 官方下載頁面](https://www.python.org/downloads/)。

2. 下載適合您作業系統的最新穩定版本安裝程式：

   * **Windows**：選擇「Download Windows installer」。
   * **macOS**：選擇「Download macOS installer」。

3. 執行下載的安裝程式：

   * **Windows**：勾選「Add Python to PATH」選項，再點選「Install Now」。
   * **macOS/Linux**：依照畫面指示完成安裝。

4. 驗證安裝： 打開命令提示字元（Windows）或終端機（macOS/Linux），輸入：

   ```bash
   python --version
   ```

   如果顯示 Python 版本號，代表安裝成功。

## 安裝 Visual Studio Code (VS Code)

1. 開啟瀏覽器，前往 [VS Code 官方下載頁面](https://code.visualstudio.com/Download)。
2. 選擇適合您作業系統的版本並下載安裝程式。
3. 執行下載的安裝程式，並一路下一步完成安裝。
4. 安裝完成後，啟動 VS Code，可在內建終端機直接執行命令。

## 安裝 Git

1. 開啟瀏覽器，前往 [Git 官方下載頁面](https://git-scm.com/downloads)。
2. 下載並安裝適合您作業系統的 Git 安裝程式，並一路下一步完成安裝。
3. 驗證安裝： 打開命令提示字元或終端機，輸入：

   ```bash
   git --version
   ```

   如果顯示 Git 版本號，代表安裝成功。

##

## 下載程式碼（Clone Git 倉庫）

1. 在命令提示字元或終端機，切換到您想存放專案的資料夾，例如：

   ```bash
   cd ~/Documents
   ```
2. 執行 Clone 指令：

   ```bash
   git clone https://github.com/peterchengfdata/Money101_automation.git
   ```
3. 進入專案資料夾：

   ```bash
   cd Money101_automation
   ```
4. 如果後續要更新程式碼，使用：

   ```bash
   git pull
   ```

## 建立虛擬環境（Virtual Environment）（Virtual Environment）

1. 在專案資料夾內，執行以下指令建立虛擬環境：

   ```bash
   python -m venv venv
   ```

   這會在專案資料夾建立一個名為 `venv` 的子資料夾。

2. 啟動虛擬環境：

   * **Windows**：

     ```bash
     venv\Scripts\activate
     ```
   * **macOS/Linux**：

     ```bash
     source venv/bin/activate
     ```

3. 啟動後，命令提示字元或終端機會出現 `(venv)` 前綴，代表已進入虛擬環境。

## 安裝相依套件（Dependencies）

1. 確認專案根目錄有 `requirements.txt`。
2. 在已啟動虛擬環境的情況下，執行：

   ```bash
   pip install -r requirements.txt
   ```
3. 安裝完成後，可驗證已安裝套件：

   ```bash
   pip list
   ```

##
