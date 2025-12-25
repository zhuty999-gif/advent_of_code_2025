# --- Part 1 ---
def import_input_as_list(filename="input.txt"):
    # This function reads a file and returns a list of non-empty, stripped lines.
    # The default filename is "input.txt", but a different file can be specified.
    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    return lines


def find_largest_joltage_from_a_bank(bank: str) -> int:
    """
    Given a string 'bank' representing a bank of batteries (each character is a digit 1-9),
    this function finds the largest possible joltage that can be produced by turning on 
    exactly two batteries (i.e., selecting two positions in order, not necessarily adjacent).
    The joltage is formed by concatenating the two digits (as in the prompt).

    Args:
        bank (str): String of battery joltages, each as a digit character.

    Returns:
        int: The largest possible joltage by any two batteries in order.
    """
    if len(bank) < 2:
        return 0

    # We want to maximize the number formed by bank[i] + bank[j] where i < j.
    # Since the first digit is most significant, we first find the largest possible first digit.
    # We search in bank[:-1] because the first digit cannot be the very last character.
    max_first_digit = max(bank[:-1])

    # We find the *first* occurrence of this digit.
    # Any later occurrence would have a subset of possible second digits available to it,
    # so the max second digit for the first occurrence is guaranteed to be >= max second digit for later occurrences.
    first_idx = bank.find(max_first_digit)

    # Find the largest digit in the remainder of the string
    remaining = bank[first_idx+1:]
    max_second_digit = max(remaining)

    largest_joltage = int(max_first_digit + max_second_digit)
    return largest_joltage
