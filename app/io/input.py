import pandas as pd


def input_text():
    """
    This function is for inputting text from the console.
    """
    return input()


def read_file(file_path):
    """
    This function is for reading from a file using built-in Python capabilities.
    """
    with open(file_path, "r") as file:
        return file.read()


def read_file_pandas(file_path):
    """
    This function is for reading from a file using the pandas library.
    """
    return pd.read_csv(file_path)
