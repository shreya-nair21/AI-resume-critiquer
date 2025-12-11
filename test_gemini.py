import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# Configure API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

print("=" * 60)
print("CHECKING AVAILABLE MODELS")
print("=" * 60)

# List all models that support generateContent
available_models = []
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            available_models.append(m.name)
            print(f"✓ {m.name}")
    
    print(f"\n Found {len(available_models)} models")
    
except Exception as e:
    print(f"Error listing models: {e}")

print("\n" + "=" * 60)
print("TESTING MODELS")
print("=" * 60)

# Test each model
models_to_test = [
    'gemini-pro',
    'gemini-1.5-pro',
    'gemini-1.5-flash',
    'models/gemini-pro',
    'models/gemini-1.5-pro',
    'models/gemini-1.5-flash',
]

for model_name in models_to_test:
    try:
        print(f"\nTesting: {model_name}...")
        model = genai.GenerativeModel(model_name)
        response = model.generate_content("Say hello")
        print(f" SUCCESS! Response: {response.text[:50]}...")
        break  # If one works, we're good
    except Exception as e:
        print(f" Failed: {str(e)[:100]}")

print("\n" + "=" * 60)
