import g4f
import asyncio

client = g4f.client.Client()

stop = False

async def gen(model, prompt):
    response = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": prompt}])
    return response.choices[0].message.content


