from email.charset import Charset
import os
import string
import math

def read_input(filename='input.txt'):
    # Construct the path relative to this script file
    file_path = os.path.join(os.path.dirname(__file__), filename)
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # The last line contains the operations
    operations_line = lines[-1].strip()
    operations = operations_line.split()

    # The previous lines are the grid
    grid_lines = lines[:-1]
    raw_rows = []
    for line in grid_lines:
        if line.strip(): # Skip empty lines if any
            raw_rows.append([int(x) for x in line.split()])

    # Transpose the rows into columns so they match the operations (one column per operation)
    # zip(*raw_rows) takes the i-th element from each row and groups them together
    grid_columns = [list(col) for col in zip(*raw_rows)] 

    return grid_columns, operations


def find_homework_answer(homework):
    """
    Given a 'homework' tuple or list where:
        - homework[0] is a list of lists of integers (each representing a row of numbers)
        - homework[1] is a list of arithmetic operator strings of the same length (e.g., ["*", "+", "*", "+"])
    For each row and its corresponding operator:
        - If the operator is '+', sum the numbers in the row.
        - If the operator is '*', multiply the numbers in the row.
    Returns the sum of all row results.
    """
    arithmetic_operators: list[str] = homework[1]
    results = []

    for i in range(len(arithmetic_operators)):
        ao: str = arithmetic_operators[i]
        numbers: list[int] = homework[0][i]
        match ao:
            case "+":
                results.append(sum(numbers))
            case "*":
                results.append(math.prod(numbers))
    
    answer = sum(results)
    return answer



def read_input_promax(filename='input.txt'):
    # Construct the path relative to this script file
    file_path = os.path.join(os.path.dirname(__file__), filename)
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    # The last line contains the operations and defines the column structure
    # We use rstrip('\n') to keep trailing spaces if they exist, but remove the newline
    op_line = lines[-1].rstrip('\n')
    grid_lines = lines[:-1]
    
    # Identify indices where operators are present
    # These indices mark the start of each column block
    op_info = [(i, char) for i, char in enumerate(op_line) if char.strip()]
    op_indices = [x[0] for x in op_info]
    operators = [x[1] for x in op_info]
    
    grid = []
    for line in grid_lines:
        # Remove newline char
        clean_line = line.rstrip('\n')
        
        # Ensure the line is at least as long as the op_line to avoid index errors
        # (Padding with spaces if necessary, effectively adding 'e's later)
        max_len = max(len(clean_line), op_indices[-1] + 1)
        if len(clean_line) < max_len:
            clean_line += ' ' * (max_len - len(clean_line))
            
        row_chunks = []
        for i in range(len(op_indices)):
            start = op_indices[i]
            
            # Determine the end of the current chunk
            if i + 1 < len(op_indices):
                end = op_indices[i+1]
            else:
                # For the last chunk, go to the end of the line
                end = len(clean_line)
            
            # Extract the chunk and replace spaces with 'e'
            chunk = clean_line[start:end]
            processed_chunk = chunk.replace(' ', 'e')
            row_chunks.append(processed_chunk)
            
        grid.append(row_chunks)

    # Transpose the grid so that it returns a list of columns
    # matching the operators
    grid_columns = [list(col) for col in zip(*grid)]
        
    return grid_columns, operators


def cephalopods_numbers_translator(numbers):
    """
    Given a list of number columns (strings potentially containing 'e' for empty),
    this function reconstructs complete numbers from right to left, stacking digits
    from each "row" (i.e., column strings) while ignoring 'e' placeholders, until
    no more valid digits are present. Returns a list of reconstructed integers, in
    least significant to most significant order.
    """
    length = len(numbers[0])  # All input number columns are of equal length
    needle = 0                # Tracks 'distance' from right (least significant digit)
    output = []

    # We'll loop from the rightmost character toward the left
    while needle < length:
        needle += 1

        # Gather the relevant digit (ignoring 'e', which acts as blank)
        chars = [x[-needle] for x in numbers if x[-needle] != "e"]

        # Remove empty characters just in case
        chars = [y for y in chars if y]

        # If we found any digits, join and convert to int, add to output
        if chars != []:
            cur_tran = int("".join(chars))
            output.append(cur_tran)  # Store the reconstructed number
    return output  # List of integers, one per "place" scanned from the right



    
def find_homework_answer_promax(homework):
    """
    Given a 'homework' tuple or list where:
        - homework[0] is a list of lists of number columns (each problem's columns in string form)
        - homework[1] is a list of arithmetic operator strings for each corresponding problem (e.g., ["*", "+", "*", "+"])
    For each problem:
        - Use cephalopods_numbers_translator() to decode the columnar digits into integers,
          where digits are assembled right-to-left per the cephalopod rules.
        - If the associated operator is '+', sum those numbers.
        - If the associated operator is '*', multiply those numbers together.
    Returns the sum of all per-problem results (the grand total for the worksheet).
    """
    arithmetic_operators: list[str] = homework[1]
    results = []

    for i in range(len(arithmetic_operators)):
        ao: str = arithmetic_operators[i]
        numbers: list[str] = homework[0][i]
        numbers = cephalopods_numbers_translator(numbers)
        match ao:
            case "+":
                results.append(sum(numbers))
            case "*":
                results.append(math.prod(numbers))
    
    answer = sum(results)
    return answer