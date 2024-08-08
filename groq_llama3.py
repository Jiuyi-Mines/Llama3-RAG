import os

from groq import Groq

# You should obtain your own GROQ_API_KEY.
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="mixtral-8x7b-32768",
)

print(client.api_key)
print(chat_completion.choices[0].message.content)
