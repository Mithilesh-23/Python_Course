from openai import OpenAI
client=OpenAI(api_key="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")
def chatt(prompt):
    response=client.chat.completions.create(
        model="gpt-4",
        messages=[{"role":"user", "content":prompt}]
    )
    return response.choices[0].message.content.strip()


wt=input("Enter weight in kg : ")
ht=input("Enter height in kg : ")

prompt="you are a fitness trainer and consultant, take a data from the customer and analyse the data and give the feedback to the customer as he/she are fit or not, also give some advice about fitness to the user. and give the analyses and advice from their current"+ht+ "meter and"+wt+"in kg of the customer. "
response=chatt(prompt)
print(response)