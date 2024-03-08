import openai

# optional; defaults to `os.environ['OPENAI_API_KEY']`
openai.api_key = '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'

# all client options can be configured just like the `OpenAI` instantiation counterpart


completion = openai.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": "How do I output all files in a directory using Python?",
        },
    ],
)
print(completion.choices[0].message.content)