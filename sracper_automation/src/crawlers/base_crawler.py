from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
import json
import pandas as pd
from datetime import datetime
from pathlib import Path

class BaseCrawler:
    def __init__(self):
        self.driver = None
        # 建立輸出目錄基本路徑
        project_root  = Path(__file__).resolve().parent.parent
        self.base_output_dir = project_root / "output"
        os.makedirs(self.base_output_dir, exist_ok=True)

    def initialize_driver(self):
        """Initialize the web driver."""
        try:
            # 設定 Chrome 選項
            options = Options()
            # options.add_argument('--headless')  # 無頭模式
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")
            
            # 初始化 WebDriver
            self.driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()),
                options=options
            )
            self.driver.implicitly_wait(10)  # 設定隱式等待時間
            print("WebDriver 初始化成功")
            return True
        except Exception as e:
            print(f"初始化 WebDriver 時發生錯誤: {e}")
            import traceback
            traceback.print_exc()
            return False

    def scroll_to_bottom(self):
        """Scroll to the bottom of the page to load all content."""
        if self.driver is None:
            print("WebDriver 未初始化，無法執行滾動操作")
            return

        print("滾動頁面以載入所有內容...")
        
        # 優化滾動策略 - 一次滾動更多距離
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        
        while True:
            # 一次滾動到底部，而非逐步滾動
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            # 減少等待時間
            time.sleep(0.5)  # 從 1 秒減少到 0.5 秒
            
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        
        # 滾動回頂部的時間也減少
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(0.5)  # 從 1 秒減少到 0.5 秒

    def scroll_to_element(self, element):
        """滾動到特定元素使其在視窗內"""
        if self.driver is None:
            print("WebDriver 未初始化，無法執行滾動操作")
            return

        try:
            # 使用 JavaScript 快速滾動，不使用 smooth 動畫
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",  # 移除 smooth behavior
                element,
            )
            # 減少等待時間
            time.sleep(0.1)  # 從 0.5 秒減少到 0.1 秒
        except Exception as e:
            print(f"滾動到元素時出錯: {e}")
    
    def save_to_file(self, data, output_subdir=None):
        """儲存資料到 JSON 和 Excel 檔案"""
        # 確定輸出目錄
        if output_subdir:
            output_dir = os.path.join(self.base_output_dir, output_subdir)
        else:
            output_dir = self.output_dir if hasattr(self, 'output_dir') else self.base_output_dir
        
        # 確保輸出目錄存在
        os.makedirs(output_dir, exist_ok=True)
        
        # 生成檔案名稱的時間戳部分
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # 1. 儲存為 JSON 格式
        json_path = os.path.join(output_dir, f"data_{timestamp}.json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"已儲存資料到 {json_path}")

        # 2. 儲存為 XLSX 格式
        try:
            # 將多層結構轉換為平坦結構，用於 Excel
            records = self.flatten_data_for_excel(data)
            
            df = pd.DataFrame(records)
            xlsx_path = os.path.join(output_dir, f"data_{timestamp}.xlsx")
            df.to_excel(xlsx_path, index=False)
            print(f"已儲存資料到 {xlsx_path}")
        except Exception as e:
            print(f"儲存 Excel 時發生錯誤: {e}")
            import traceback
            traceback.print_exc()
        
        return json_path, xlsx_path

    def flatten_data_for_excel(self, data):
        """將多層結構數據轉為適合 Excel 的平坦結構"""
        # 基礎實現，子類應覆寫此方法
        return data

    def close(self):
        """Close the web driver."""
        if self.driver:
            self.driver.quit()
            print("瀏覽器已關閉")