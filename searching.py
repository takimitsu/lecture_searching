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

def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")

    print(linear_search(sequential_data, 9))

if __name__ == "__main__":
    main()
