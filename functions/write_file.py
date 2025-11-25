import os
from google import genai
from google.genai import types


def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    dir_path = os.path.dirname(abs_file_path)
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        if os.path.exists(abs_file_path) and os.path.isdir(abs_file_path):
            return f'Error: "{file_path}" is a directory, not a file'
        if dir_path and not os.path.exists(dir_path):
            os.makedirs(dir_path)
        with open(abs_file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f'Error: {e}'
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write or overwrite to the file if the file exists, then explain what was written, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="If the file does not exist create a new file with the given name, write or overwrite content in that file",
                ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="What is being written to the file. The content being added",
                ),
        },
        required = ["file_path", "content"]
    ),
)

