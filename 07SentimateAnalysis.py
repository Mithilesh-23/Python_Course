# from openai import OpenAI
# import openai

# client=openai.OpenAI(api_key="sk-proj-mgKIMoUer8JW6sF5Ic6ms9Acq_ZbcHK3mBmYyH-UVWxY4UusxnPXyooZ0V7-LnphCRkFJzi9qqIj-AeWwQj03ru1K6i5zllJ6K0zDOMgiW0h-8AdY692OTVrptpAkjOA83V5zE_MhoUgEcA")


# def chat_gpt(prompt):
#     response=client.chat.completions.create(
#         model="gpt-4o",
#         messages=[{"role":"user", "content":prompt}]
#     )
#     return response.choices[0].message.content.strip()

# review=input("Enter a review : ")
# prompt='''
# I am sending you a profuct review, analyse the sentiment in the review, tell me the overall sentiment of the review text.
# if it is a mix of the sentiment classify them into positive and negative. list the possitive aspects od the review and negative aspects of the review, also 
# give the suggestion to product department the company to improve the product based on customer revview.
# '''

# response=chat_gpt(prompt+review)
# print(response)


from openai import OpenAI

client=OpenAI(api_key="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")

def chat_gpt(prompt):
    response=client.chat.completions.create(
        model="gpt-4",
        messages=[{"role":"user","content":prompt}]
    )
    return response.choices[0].message.content.strip()


prompt=input("Enter a prompt : ")
response=chat_gpt(prompt)
print(response)
