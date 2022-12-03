from os.path import exists
from sys import exit
from argparse import ArgumentParser

CELLS = [] # All our cells
POINTER = 0
MAX_CELLS = 0

def running_error(line:int, column:int, msg:str) -> None:
    """
    Description: Prints a customzied error message to the screen before it terminates the application
    Input:
        - line (int) Current line that we are on
        - column (int) Current column where the error occurred
        - msg (str) What went wrong
    Return: None
    """
    exit(f"""
    # Error:
    Line: {line}
    Column: {column}
    Msg: {msg}
    """)

def interpreter(line:str, line_nr:int) -> None:
    """
    Description: Parses all our data, and interpretes it 
    Input:
        - line (str) The line to parse
        - line_nr (int) The line number, used for error messages
    Return: None
    """
    global POINTER, CELLS

    for c, char in enumerate(line):
        if char == ">":
            if POINTER+1 > MAX_CELLS: # Out-of-bounds
                running_error(line_nr, c, "Increasing the POINTER would put it out-of-bounds")

            POINTER +=1

        elif char == "<":
            if POINTER-1 < 0: # Out-of-bounds
                running_error(line_nr, c, "Decreasing the POINTER would put it out-of-bounds")

            POINTER -= 1

        elif char == "+":
            CELLS[POINTER] += 1

        elif char == "-":
            CELLS[POINTER] -= 1

        elif char == "[":
            if line.find("]") == -1:
                running_error(line_nr, c, "Failed to find ']' in a while-clause")

            chars = line[c+1:line.find("]")+1]
            interpreter(line=chars, line_nr=line_nr)

        elif char == "]" and CELLS[POINTER] <= 0: # Time to exit
            return

        elif char == ",":
            try:
                CELLS[POINTER] = int(input())
            except Exception as err:
                running_error(line_nr, c, err)

        elif char == ".":
            if CELLS[POINTER] >= 32 and CELLS[POINTER] <= 126: 
                print(chr(CELLS[POINTER]))
            else:
                print(CELLS[POINTER])


def main(file_path:str, max_amount_of_cells:int) -> None:
    """
    Description: Main loop of the software
    Input:
        - file_path (str) The file to read
    Return: None
    """
    global CELLS, POINTER, MAX_CELLS
    if not exists:
        exit(f"Error: Failed to find file '{file_path}'")

    MAX_CELLS = max_amount_of_cells
    CELLS = [0 for _ in range(MAX_CELLS)] # All our cells
    POINTER = 0

    for l, line in enumerate(open(file_path, "r").readlines()):
        interpreter(line, l)

if __name__ == "__main__":
    parser = ArgumentParser(description="Brainfuck, because why not")
    parser.add_argument("-f", "--file", help="File to parse", required=True)
    parser.add_argument("-c", "--cells", help="How many cells to use? Default is 30000", default=30000, type=int)

    parser = parser.parse_args()

    main(parser.file, parser.cells) # Start the interpretation!