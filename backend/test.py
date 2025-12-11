# Save as test_gemini_models.py
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("❌ No GOOGLE_API_KEY found in .env file!")
    exit()

print(f"✅ API Key found: {api_key[:20]}...")

genai.configure(api_key=api_key)

print("\n📋 Available Models for generateContent:")
available_models = []
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        model_name = m.name.replace('models/', '')
        available_models.append(model_name)
        print(f"  ✅ {model_name}")

print("\n🧪 Testing the first available model...")
if available_models:
    try:
        model = genai.GenerativeModel(available_models[0])
        response = model.generate_content("Say hello in 3 words")
        print(f"✅ SUCCESS! Model '{available_models[0]}' works!")
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"❌ Error: {e}")
else:
    print("❌ No models available! Check your API key permissions.")