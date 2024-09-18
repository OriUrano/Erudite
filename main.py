import flask
import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI"])

sample_file = genai.upload_file(path="nosesoff.pdf",
                                display_name="Noses Off PDF")

print(f"Uploaded file '{sample_file.display_name}' as: {sample_file.uri}")

file = genai.get_file(name=sample_file.name)
print(f"Retrieved file '{file.display_name}' as: {sample_file.uri}")

# Choose a Gemini model.
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")

prompt = "Make me a charcter analysis report. In this report you should include Age, Voice, Walk, Physical Description, Occupation, Interests, Beliefs (Religous and otherwise), Ambitions, Favorite color, Favorite food, Favorite Song or Type of Music, Favorite (Play, Movie, Book, TV Show, Radio Show, pick one), Body lead, What animal are they most like, Some important items or images associated with the character, What is the character's relationship to the other characters in the play (Other character, relationship, feelings toward him or her), small character history in bullet points. If the information isn't there, be creative and makes something up that fits the character. The character you will be doing the analyis on is Obo."

fileOutput = "nosesOffOboAnalysis.txt"

# Prompt the model with text and the previously uploaded image.
response = model.generate_content([sample_file, 
    prompt])

print(response.text)

f = open(fileOutput, "a")
f.write("\nPrompt:\n")
f.write(prompt)
f.write("\nResponse:\n")
f.write(response.text)
f.close()

for file in genai.list_files():
    genai.delete_file(file.name)
    print(f"{file.display_name}, URI: {file.uri}, Name: {file.name}")