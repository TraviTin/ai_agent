import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    load_dotenv()

    def user_input():
        if len(sys.argv) > 1:
            return sys.argv[1]
        else:
            print("Error: No input provided. Please provide input as a command-line argument.")
            sys.exit(1)

    prompt = user_input()

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    generate_content(client, messages)

def generate_content(client, messages):
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents= messages,
    )

    print("Prompt tokens: ", response.usage_metadata.prompt_token_count)
    print("Response tokens: ", response.usage_metadata.candidates_token_count)
    print(response.text)



if __name__ == "__main__":
    main()
