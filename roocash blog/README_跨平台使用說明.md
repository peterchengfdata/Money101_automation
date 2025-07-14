# RooCash 部落格爬蟲 - 跨平台版本

這個程式可以在 Windows 和 Mac 系統上運行，自動爬取 RooCash 部落格的文章內容。

## 系統需求

- Python 3.7+
- Chrome 瀏覽器

## 安裝步驟

1. 安裝 Python 套件：

```bash
pip install -r requirements.txt
```

2. 確保有對應系統的 chromedriver：
   - **Windows**: `chromedriver.exe` (已包含)
   - **Mac**: `chromedriver` (已包含)

## 檔案說明

- `roocash_blog.py` - 主要爬蟲程式
- `chromedriver.exe` - Windows 版本的 chromedriver
- `chromedriver` - Mac 版本的 chromedriver
- `download_chromedriver_mac.py` - Mac 用戶可執行此腳本重新下載 chromedriver

## 使用方法

直接執行主程式：

```bash
python roocash_blog.py
```

程式會自動：

1. 偵測你的作業系統 (Windows/Mac)
2. 使用對應的 chromedriver
3. 爬取 RooCash 部落格所有分類的文章
4. 將結果保存到 `../money101_cal/roocash_data/` 目錄

## 故障排除

### 如果 chromedriver 無法執行：

**Windows 用戶:**

- 確保 `chromedriver.exe` 檔案存在
- 檢查 Chrome 瀏覽器是否已安裝

**Mac 用戶:**

- 如果遇到權限問題，請執行：
  ```bash
  chmod +x chromedriver
  ```
- 如果遇到 macOS 安全限制，請在「系統偏好設定 > 安全性與隱私」中允許執行

### 如果自動偵測失敗：

程式會自動嘗試以下順序：

1. 使用本地 chromedriver 檔案
2. 使用 ChromeDriverManager 自動下載
3. 使用系統預設 Chrome

## 輸出檔案

程式會產生以下檔案：

- `roocash_all_articles.csv` - 所有文章列表
- `roocash_article_details.csv` - 文章詳細資訊
- `article_X_content.txt` - 個別文章內容
- `article_X_tables.txt` - 文章中的表格內容

## 注意事項

- 程式執行時間較長，請耐心等待
- 網路連線需要穩定
- 建議不要同時執行多個爬蟲程式
