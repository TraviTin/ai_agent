from google.genai import types

from functions.get_files_info import schema_get_files_info, get_files_info
from prompts import system_prompt
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.write_file import schema_write_file, write_file
from functions.run_python_file import schema_run_python_file, run_python_file




def call_function(function_call_part, verbose=False):
    if verbose: 
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    functions_dict ={
        "run_python_file" : run_python_file,
        "write_file" : write_file,
        "get_file_content" : get_file_content,
        "get_files_info" : get_files_info,

    }
    function_name = function_call_part.name

    if not function_call_part.name in functions_dict:
        return types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=function_name,
            response={"error": f"Unknown function: {function_name}"},
        )
    ],
)
    else: 
        args = dict(function_call_part.args)
        args["working_directory"] = "./calculator" 
        function_result = functions_dict[function_name](**args)
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"result": function_result},
        )
    ],
)


