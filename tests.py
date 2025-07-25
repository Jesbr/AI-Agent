from functions.run_python import run_python_file


#def test():
#    result = get_file_content("calculator", "lorem.txt")
#    print("Result for lorem:")
#    print(result)


def test():
    result = run_python_file("calculator", "main.py")
    print("Result for run_python_file:")
    print(result)

    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print("Result for run_python_file:")
    print(result)

    result = run_python_file("calculator", "tests.py")
    print("Result for run_python_file:")
    print(result)

    result = run_python_file("calculator", "../main.py")
    print("Result for run_python_file:")
    print(result)

    result = run_python_file("calculator", "nonexistent.py")
    print("Result for run_python_file:")
    print(result)
    


if __name__ == "__main__":
    test()