# Python

import numpy as np
import time


date_time = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())


def display_nasa_tlx_form_rating():
    rating_task_questions = [
        "Mental Demand: How mentally demanding was the task?",
        "Physical Demand: How physically demanding was the task?",
        "Temporal Demand: How hurried or rushed was the pace of the task?",
        "Performance: How successful were you in accomplishing what you were asked to do?",
        "Effort: How hard did you have to work to accomplish your level of performance?",
        "Frustration: How insecure, discouraged, irritated, stressed, and annoyed were you?",
    ]

    rating_task_responses = {}

    print("\nNASA-TLX Form")
    print("Please rate each question on a scale:")
    print("|--|--|--|--|--|--|--|--|--|--||--|--|--|--|--|--|--|--|--|--| 20(High)")
    print("0 (Low)                       10                             20(High)\n")

    for i, question in enumerate(rating_task_questions, start=1):
        while True:
            try:
                response = int(input(f"Question {i}/6: {question} "))
                if 0 <= response <= 20:
                    rating_task_responses[question] = response
                    break
                else:
                    print("Please enter a number between 0 and 20.")
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 20.")
    with open(f"{date_time}_nasa_tlx_rating_responses.txt", "w") as file:
        for question, response in rating_task_responses.items():
            file.write(f"{response}\n")
            print(f"{response} <- {question}")

    with open(f"{date_time}_nasa_tlx_rating_responses_calculated.txt", "w") as file:
        for question, response in rating_task_responses.items():
            file.write(f"{response * 5}\n")
            print(f"{response * 5} <- {question}")


def display_nasa_tlx_form_pairing():

    dimensions = [
        "Mental Demand: How mentally demanding was the task?",
        "Physical Demand: How physically demanding was the task?",
        "Temporal Demand: How hurried or rushed was the pace of the task?",
        "Performance: How successful were you in accomplishing what you were asked to do?",
        "Effort: How hard did you have to work to accomplish your level of performance?",
        "Frustration: How insecure, discouraged, irritated, stressed, and annoyed were you?",
    ]

    # Generate all pairs of dimensions for comparison
    pairs = [
        (i, j) for i in range(len(dimensions)) for j in range(i + 1, len(dimensions))
    ]

    # Collect responses for each pair (user rates which dimension is more relevant)
    responses = []
    print("\nNASA TLX Pairing Test\n")
    print("For each of the following pairs,")
    print("please circle the scale title that contributed more")
    print("to your experience of workload during this run.")
    print("In other words, which of the pair made the task harder?\n")

    counter = 1
    for i, j in pairs:
        while True:
            print(f"Pair {counter}/15:")
            print(f"(1) {dimensions[i]}")
            print(f"(2) {dimensions[j]}")
            response = input("Enter 1 or 2: ")
            print()
            if response in ["1", "2"]:
                counter += 1
                responses.append(int(response))
                break
            else:
                print("Invalid input. Please enter 1 or 2. \n")

    # Calculate weights based on responses
    weights = np.zeros(len(dimensions))
    for (i, j), response in zip(pairs, responses):
        if response == 1:
            weights[i] += 1
        elif response == 2:
            weights[j] += 1

    # Display results
    print("NASA TLX Dimension Weights:")
    for i, dimension in enumerate(dimensions):
        print(f"{dimension}: {weights[i]}")

    with open(f"{date_time}_nasa_tlx_pairing_responses.txt", "w") as file:
        for response, (i, j) in zip(responses, pairs):
            file.write(f"{response} <--- 1. {dimensions[i]} 2. {dimensions[j]}\n")
        for i, dimension in enumerate(dimensions):
            file.write(f"{weights[i]} <- {dimension}\n")


if __name__ == "__main__":
    display_nasa_tlx_form_rating()
    display_nasa_tlx_form_pairing()
