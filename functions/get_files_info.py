import os
from google import genai
from google.genai import types

def get_files_info(working_directory, directory="."):
    full_path = os.path.abspath(os.path.join(working_directory, directory))
    wd_abs = os.path.abspath(working_directory)
    if not full_path.startswith(wd_abs):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    elif not os.path.isdir(os.path.join(working_directory, directory)):
        return f'Error: "{directory}" is not a directory'
    directory_contents = []
    try:
        for item in os.listdir(os.path.join(working_directory, directory)):
            name = "- " + item + ": "
            sizes = "file_size=" + str(os.path.getsize(os.path.join(working_directory, directory, item))) + "bytes, "
            is_dir = "is_dir=" + str(os.path.isdir(os.path.join(working_directory, directory, item)))
            directory_contents.append(name + sizes + is_dir)
        return "\n".join(directory_contents)
    except Exception as e:
        return f"Error: {str(e)}"
        
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)