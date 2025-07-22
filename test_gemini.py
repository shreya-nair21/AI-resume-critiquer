import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY"),
    transport="rest",  # Use REST to get v1 API, not v1beta
)

# Step 4: List available models — add this BEFORE using any model
models = genai.list_models()
print("Available models:")
for m in models:
    print(m.name)

# Then try to create the model with the full model name
model = genai.GenerativeModel("models/gemini-1.5-pro-latest")



response = model.generate_content("Give me a one-line resume feedback.")
print("\nResponse from gemini-pro model:")
print(response.text)
