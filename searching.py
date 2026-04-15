from pathlib import Path
import json
import matplotlib.pyplot as plt
import generators
import time
import random

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

def time_complexity_graphs(sizes):
    sizes = [100, 500, 1000, 5000, 10000, 100000, 1000000]
    number = 200

    times_linear = []
    times_binary = []

    for length in sizes:
        unordered_data = generators.unordered_sequence(length)
        ordered_data = generators.ordered_sequence(length)

        unordered_number = random.choice(unordered_data)
        ordered_number = random.choice(ordered_data)

        start_linear = time.perf_counter()
        linear_result = linear_search(unordered_data, unordered_number)
        end_linear = time.perf_counter()

        start_binary = time.perf_counter()
        binary_result = binary_search(ordered_data, ordered_number)
        end_binary = time.perf_counter()

        duration_linear, duration_binary = end_linear - start_linear, end_binary - start_binary

        times_linear.append(duration_linear)
        times_binary.append(duration_binary)

    _, ax = plt.subplots(1, 2)

    ax[0].plot(sizes, times_linear)
    ax[0].set_title("Linear Search")
    ax[0].set_xlabel("Input Size")
    ax[0].set_ylabel("Time [s]")
    ax[1].plot(sizes, times_binary)
    ax[1].set_title("Binary Search")
    ax[1].set_xlabel("Input Size")
    ax[1].set_ylabel("Time [s]")
    plt.show()

def pattern_search(sequence, pattern):
    result = []

    for i in range(len(sequence)):
       if sequence[i:i+len(pattern)] == pattern:
           result.append(i)

    return set(result)

def main():
    #sequential_data = read_data("sequential.json", "unordered_numbers")
    #ordered_list = read_data("sequential.json", "ordered_numbers")
    dna_sequence = read_data("sequential.json", "dna_sequence")

    #sizes = [[10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]]
    #time_complexity_graphs(sizes)

    print(pattern_search(dna_sequence, "ATA"))

if __name__ == "__main__":
    main()
