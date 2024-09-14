import flask
import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI"])

sample_file = genai.upload_file(path="nosesoff.pdf",
                                display_name="Noses Off Script")

print(f"Uploaded file '{sample_file.display_name}' as: {sample_file.uri}")

file = genai.get_file(name=sample_file.name)
print(f"Retrieved file '{file.display_name}' as: {sample_file.uri}")

# Choose a Gemini model.
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Prompt the model with text and the previously uploaded image.
response = model.generate_content([sample_file, "Can you summarize this document as a bulleted list?"])

print(response.text)