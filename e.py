import google.generativeai as genai
import os

file_name = "AMSCO+1.1.pdf"
genai.configure(api_key=os.environ["GEMINI"])
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")
prompt = "Rewrite this into Markdown format word for word. Don't keep the word wrapping. Dont include page numbers, images, image caption, questions to the reader, essential question, quotes."

print(file_name)
uploaded_file = genai.upload_file(path="AMSCO/"+file_name, display_name=file_name)

response = model.generate_content([uploaded_file, 
    prompt])

f = open("AMSCO/"+file_name[:-3]+"txt", "w")
f.write(response.text)
f.close()

for file in genai.list_files():
    genai.delete_file(file.name)
    print(f"{file.display_name}, URI: {file.uri}, Name: {file.name}")