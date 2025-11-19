import os
import sys
from dotenv import load_dotenv
from google import genai


def main():
    load_dotenv()
    
    def user_input():
        if len(sys.argv) > 1:
            return sys.argv[1]
        else:
            print("Error: No input provided. Please provide input as a command-line argument.")
            sys.exit(1)
        
    prompt = user_input()

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents= prompt)

    print("Prompt tokens: ", response.usage_metadata.prompt_token_count)
    print("Response tokens: ", response.usage_metadata.candidates_token_count)
    print(response.text)



if __name__ == "__main__":
    main()
