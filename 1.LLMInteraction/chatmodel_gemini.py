from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
prompt = "Hello, how are you?, how ai work?"
result=model.invoke(prompt)
print(result.content)



