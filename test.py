from google import genai

# 初始化 Client
client = genai.Client(api_key="AIzaSyDk5xmS_YkESRDxYJErNZqWZM_RfbiPHpQ")

# 測試生成內容
response = client.models.generate_content(
    model="gemini-2.5-flash", 
        contents="分析這段話的心情：『專題快做不完了好焦慮』"
        )

print("-" * 20)
print(response.text)