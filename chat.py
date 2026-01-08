from groq import Groq

# Reemplaza con tu nueva clave de Groq
client = Groq(api_key="")

prompt = input("prompt: ")

completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

# La respuesta se encuentra en este atributo específico
print(completion.choices[0].message.content)