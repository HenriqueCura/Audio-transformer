import os
from openai import OpenAI
from pydantic import BaseModel

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class resumo(BaseModel):
    titulo: str
    resumo: str

prompt = client.chat.completions.create(
    model = "chatgpt-4o-latest",
    messages = [
        {"role": "system", "content":"You are a pdf summary agent. You will be given a pdf and your job is to summarise the text in that pdf."},
        {
            "role": "user", 
            "content": "x"
        }
    ],
)

response = prompt.choices[0].message.content
print(response)

prompt = client.beta.chat.completions.parse(
    model = "chatgpt-4o-latest",
    messages = [
        {"role": "system", "content":"You are a pdf summary agent. You will be given a pdf and your job is to summarise the text in that pdf."
        " Also get the pdf's title."},
        {
            "role": "user", 
            "content": "x"
        }
    ],
    response_format=resumo,
)

response = prompt.choices[0].message.parsed
titulo = response.titulo
resumoo = response.resumo
