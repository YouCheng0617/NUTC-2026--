import os
from google import genai
from dotenv import load_dotenv

# 1. 讀取 .env 檔案
load_dotenv() 

# 2. 從環境變數抓取金鑰
api_key = os.getenv("GEMINI_API_KEY")

# 3. 初始化 Client
client = genai.Client(api_key=api_key)

# 4. 測試生成內容
response = client.models.generate_content(
    model="gemini-2.0-flash",
        contents="分析這段話的心情：『專題快做不完了好焦慮』"
        )

print("-" * 20)
print(response.text)