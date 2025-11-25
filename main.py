import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info, available_functions
from prompts import system_prompt
from google.genai import types

def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {prompt}")

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    generate_content(client, messages, verbose)

def generate_content(client, messages, verbose):
    config = types.GenerateContentConfig(
    tools=[available_functions],
    system_instruction=system_prompt,
    )
    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents= messages,
        config = config)
    
    if verbose:   
        print("Prompt tokens: ", response.usage_metadata.prompt_token_count)
        print("Response tokens: ", response.usage_metadata.candidates_token_count)   

    function_calls = response.function_calls
    if function_calls is not None:
        for func_parts in function_calls:
            print(f"Calling function: {func_parts.name}({func_parts.args})")
    else:
        print("Response:")
        print(response.text)
   
   


if __name__ == "__main__":
    main()
