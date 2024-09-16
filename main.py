import flask
import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI"])

sample_file = genai.upload_file(path="AMSCO+1.6.pdf",
                                display_name="AMSCO 1.6")

print(f"Uploaded file '{sample_file.display_name}' as: {sample_file.uri}")

file = genai.get_file(name=sample_file.name)
print(f"Retrieved file '{file.display_name}' as: {sample_file.uri}")

# Choose a Gemini model.
model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest")

prompt = "Rewrite this into Markdown word for word. Dont include page numbers, images, image caption, questions about connecting to other subjects"

# Prompt the model with text and the previously uploaded image.
response = model.generate_content([sample_file, 
    prompt])

print(response.text)

f = open("response.txt", "a")
f.write("\nPrompt:\n")
f.write(prompt)
f.write("\nResponse:\n")
f.write(response.text)
f.close()

for file in genai.list_files():
    genai.delete_file(file.name)
    print(f"{file.display_name}, URI: {file.uri}, Name: {file.name}")