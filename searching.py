from pathlib import Path
import json


def read_data(file_name, field):
    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    # get current working directory path
    cwd_path = Path.cwd()
    
    file_path = cwd_path / file_name

    with open(file_path, "r") as f:
        data = json.load(f)

    if field in data.keys():
        return data[field]

    return None

# O(n)
def linear_search(sequence, number):
    result = {"positions": [], "count": 0}

    for i in range(len(sequence)):
        if sequence[i] == number:
            result["positions"].append(i)
            result["count"] += 1

    return result

# O(log n)
def binary_search(num_list, number):
    left = 0
    right = len(num_list) - 1

    while left <= right:
        middle = (left + right) // 2

        if num_list[middle] == number:
            return num_list[middle]
        elif num_list[middle] < number:
            left = middle + 1
        elif num_list[middle] > number:
            right = middle - 1

    return None

def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    ordered_list = read_data("sequential.json", "ordered_numbers")

    #print(linear_search(sequential_data, 9))
    print(binary_search(ordered_list, 102))

if __name__ == "__main__":
    main()
