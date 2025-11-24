from functions.get_file_content import get_file_content
import os




def print_test_result(working_dir, directory_param):
    header_dir_name = "'" + directory_param +"'"
    if directory_param == '.':
        header_dir_name = "current"

    print(f"Result for {header_dir_name} directory:")

    result = get_file_content(working_dir, directory_param)

    for line in result.split('\n'):
        print(f"    {line}")
    print("\n")




print_test_result("calculator", "main.py")
print_test_result("calculator", "pkg/calculator.py")
print_test_result("calculator", "/bin/cat")
print_test_result("calculator", "pkg/does_not_exist.py")