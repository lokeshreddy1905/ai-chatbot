from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

print("🤖 AI Chatbot")
print("Type 'exit' to quit.\n")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    response = client.responses.create(
        model="gpt-5.5",
        input=user
    )

    print("Bot:", response.output_text)
