import openai
import os

def call_openai(prompt):
    try:
        api_key = os.environ.get("OPENAI_API_KEY")
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=150,
            api_key=api_key  # use the environment variable
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {e}"
