import openai

client = openai.OpenAI()

response = client.chat.compleation.create(
    model="gpt-4o-mini",
    messages=[
        {"role":"system", "content": "You are a helpful assistant that can answer questions and help with tasks."},
        {"role":"user", "content": "What is the capital of France?"},
    ]
)

print(response.choices[0].message.content)
