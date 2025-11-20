from functions.get_files_info import get_files_info
import os



def print_test_result(working_dir, directory_param):
    header_dir_name = "'" + directory_param +"'"
    if directory_param == '.':
        header_dir_name = "current"

    print(f"Result for {header_dir_name} directory:")

    result = get_files_info(working_dir, directory_param)

    for line in result.split('\n'):
        print(f"    {line}")
    print("\n")




print_test_result("calculator", ".")
print_test_result("calculator", "pkg")
print_test_result("calculator", "/bin")
print_test_result("calculator", "../")

