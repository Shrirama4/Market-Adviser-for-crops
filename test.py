import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(model_name="gemini-1.5-flash")
prompt='''translate this to kannnada and i want only kannada translation as reponse and nothing else :Market Details for Coffee:
  - Average Daily Price: ₹1069.52
  - Average Price Change: 0.81%
  - Recommendation: It is better to hold the crop'''
response = model.generate_content(prompt)
# print(response.text)
with open('response.txt', 'w') as file:
    file.write(response.text)