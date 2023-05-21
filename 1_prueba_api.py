import os
import openai
openai.organization = "org-cIzWval5Fo6zd1ECeBGvyMTH"
openai.api_key = os.getenv("OPENAI_API_KEY")
print("Prueba 1")
model_list = openai.Model.list()
print(model_list)
