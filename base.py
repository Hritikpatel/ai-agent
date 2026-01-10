from config import client
from masterAgent import Master
from prompts import system_prompt

messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
]

# isUser = False

masterInstance = Master("Master", client, system_prompt("Creating rough roadmap."))
print(masterInstance.name)
print(masterInstance.prompt)
print(masterAgent._id)





























# for i in range(20):
#     response = client.chat(model='gemma3:270m', messages=messages)

#     print(response.message.content)
    
#     if isUser:
#         messages.append(
#             {
#                 'role': 'user',
#                 'content': response.message.content,
#             }
#         )
#         isUser = False
#     else:
#         messages.append(
#             {
#                 'role': 'ai',
#                 'content': response.message.content,
#             }
#         )
#         isUser = True

# print(messages)