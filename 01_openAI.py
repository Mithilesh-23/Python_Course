from openai import OpenAI

client=OpenAI(api_key="")

def chatgpt(prompt):
    response=client.chat.completions.create(
        model="gpt-4",
        messages=[{"role":"user", "content":prompt}]
    )
    return response.choices[0].message.content.strip()

prompt=input("Enter the Prompt : ")
response=chatgpt(prompt)
print(response)
