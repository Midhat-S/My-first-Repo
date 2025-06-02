from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-4.1",
    tools=[{"type": "web_search_preview"}],
    input="What is the current weather of London?"
)

print(response.output_text)

for i in range(1, 6):
    print(i)

color
