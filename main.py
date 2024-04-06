from app.io.input import input_text, read_file, read_file_pandas
from app.io.output import output_text, write_file


def main():
    print("Testing input_text:")
    text = input_text()
    print(f"You entered: {text}")

    print("\nTesting read_file:")
    file_content = read_file("data/text.txt")
    print(f"Content of 'equirements.txt':\n{file_content}")

    print("\nTesting read_file_pandas:")
    df = read_file_pandas("data/df1.csv")
    print(df)

    print("\nTesting output_text:")
    output_text("Hello, world!")

    print("\nTesting write_file:")
    write_file("data/test_output.txt", "Writing to a file.")
    print("Wrote to 'test_output.txt'.")


if __name__ == "__main__":
    main()
