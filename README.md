# BookBot

## Overview
A BookBot that read the book content and reports the total word count and number of characters used

## How to use
1. **Create a Book Folder**
    - Create a folder named `books` to store your book content in `.txt` format.

2. **Add a Book File**
    - Add your book content as a `.txt` file in the `books` folder.
    - For example, you can use the text file from the following link:
     [Frankenstein by Mary Shelley](https://raw.githubusercontent.com/asweigart/codebreaker/master/frankenstein.txt)

3. **Update the `book_path` Variable**
    - Open the `main.py` file.
    - Change the `book_path` variable to the relative path of your book file.
    - Example:

        ```python
        book_path = "books/frankenstein.txt"
        ```

4. **Run the Program**
    - Open your terminal or command prompt.
    - Run the `main.py` file:

        ```bash
        python main.py
        ```
    - The program will read the book, calculate the total word count and character count, and display the report in the terminal.

## Contributing


## License
None

