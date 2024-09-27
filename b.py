import google.generativeai as genai
import os

file_name = "MarcoPoloReading.pdf"
genai.configure(api_key=os.environ["GEMINI"])
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")
prompt = "I have a reading quiz on this pdf. Please explain the key topic or of the reading and what some possible question on the quiz might be."

print(file_name)
uploaded_file = genai.upload_file(path=file_name, display_name=file_name)

response = model.generate_content([uploaded_file, 
    prompt])

f = open("marcopolo.txt", "w")
f.write(response.text)
f.close()

for file in genai.list_files():
    genai.delete_file(file.name)
    print(f"{file.display_name}, URI: {file.uri}, Name: {file.name}")