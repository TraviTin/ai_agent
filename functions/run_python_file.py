import os
import subprocess
from google.genai import types
from google import genai


def run_python_file(working_directory, file_path, args=[]):
    full_path = os.path.abspath(os.path.join(working_directory, file_path))
    wd_abs = os.path.abspath(working_directory)
    if not full_path.startswith(wd_abs):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        result = subprocess.run(["python3", full_path] + args, capture_output=True, cwd=working_directory, timeout=30, text=True) 
        if len(result.stdout) ==0 and len(result.stderr) == 0:
            return "No output produced."
        stdout_only = "STDOUT:" + result.stdout
        stderr_only = "STDERR:" + result.stderr
        output = stdout_only + "\n" + stderr_only
        exit_err = result.returncode
        if exit_err != 0:
            output += f"\nProcess exited with code {result.returncode}"
        return output 
    
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute Python files with optional arguments.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Execute Python files with optional arguments.",
                ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="A list of potential arguments to give the the program you are running. Only needed if the program requires args. "
                )
        },
        required=["file_path"]
    ),
)
