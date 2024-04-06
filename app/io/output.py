def output_text(text):
    """
    This function is for outputting text to the console.
    """
    print(text)


def write_file(file_path, content):
    """
    This function is for writing to a file using built-in Python capabilities.
    """
    with open(file_path, "w") as file:
        file.write(content)
