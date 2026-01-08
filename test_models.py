from google import genai
client = genai.Client(api_key="AIzaSyD76evxTorSk45Ny9CCQT5BewVCeykAyYE")

for model in client.models.list():
    print(model.name)