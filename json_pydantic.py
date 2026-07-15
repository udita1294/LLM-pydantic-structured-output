import os 
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("API key not found")

client = Groq(api_key = my_api_key);

model = "llama-3.3-70b-versatile"
role = "user"
text = "I purchased a SmartX Bluetooth speaker last month, but it frequently disconnects from my phone and the battery drains within an hour despite a full charge. Please arrange a repair or replacement as soon as possible.My name is Aarav Mehta. My email address is aarav.mehta482@example.com and phone number is 9876543210."
prompt = f"""
    This is a customer ticket. Please extract the following information from the text:
    1. Customer Name
    2. Product Name
    3. Issue Description
    4. Contact Information (Email and Phone Number) 
    from {text}
"""

message = {
    "role" : role,
    "content" : prompt
}

messages = [message]

response = client.chat.completions.create(model=model, messages=messages)
answer = response.choices[0].message.content
print(answer)