import sys
import pandas as pd
import numpy as np


def error(message):
    print("Error:", message)
    sys.exit(1)


def main():

    # ---------------------------------------------------
    # 1. Check correct number of command line arguments
    # ---------------------------------------------------
    if len(sys.argv) != 5:
        error("Incorrect number of parameters.\n"
              "Usage: python topsis.py <InputDataFile> <Weights> <Impacts> <OutputFileName>")

    input_file = sys.argv[1]
    weights_input = sys.argv[2]
    impacts_input = sys.argv[3]
    output_file = sys.argv[4]

    # ---------------------------------------------------
    # 2. Handle File Not Found & File Reading
    # ---------------------------------------------------
    try:
        if input_file.endswith('.xlsx'):
            data = pd.read_excel(input_file)
        elif input_file.endswith('.csv'):
            data = pd.read_csv(input_file)
        else:
            error("Input file must be .xlsx or .csv format.")
    except FileNotFoundError:
        error("File not found.")
    except Exception:
        error("Error reading the input file.")

    # ---------------------------------------------------
    # 3. Check minimum columns (at least 3)
    # ---------------------------------------------------
    if data.shape[1] < 3:
        error("Input file must contain three or more columns.")

    # ---------------------------------------------------
    # 4. Check numeric values from 2nd to last column
    # ---------------------------------------------------
    for col in data.columns[1:]:
        if not pd.api.types.is_numeric_dtype(data[col]):
            error("All columns from 2nd to last must contain numeric values only.")

    # ---------------------------------------------------
    # 5. Process Weights and Impacts
    # ---------------------------------------------------
    weights = weights_input.split(',')
    impacts = impacts_input.split(',')

    criteria_count = len(data.columns) - 1

    if len(weights) != criteria_count:
        error("Number of weights must match number of criteria columns.")

    if len(impacts) != criteria_count:
        error("Number of impacts must match number of criteria columns.")

    # Convert weights to float
    try:
        weights = np.array(weights, dtype=float)
    except ValueError:
        error("Weights must be numeric and comma separated.")

    # Validate impacts
    for impact in impacts:
        if impact not in ['+', '-']:
            error("Impacts must be either '+' or '-' and comma separated.")

    impacts = np.array(impacts)

    # ---------------------------------------------------
    # 6. TOPSIS Calculation
    # ---------------------------------------------------

    # Step 1: Normalize the decision matrix
    decision_matrix = data.iloc[:, 1:].values
    norm = np.sqrt((decision_matrix ** 2).sum(axis=0))
    normalized_matrix = decision_matrix / norm

    # Step 2: Multiply by weights
    weighted_matrix = normalized_matrix * weights

    # Step 3: Determine Ideal Best and Ideal Worst
    ideal_best = []
    ideal_worst = []

    for i in range(criteria_count):
        if impacts[i] == '+':
            ideal_best.append(np.max(weighted_matrix[:, i]))
            ideal_worst.append(np.min(weighted_matrix[:, i]))
        else:
            ideal_best.append(np.min(weighted_matrix[:, i]))
            ideal_worst.append(np.max(weighted_matrix[:, i]))

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    # Step 4: Calculate distances
    distance_best = np.sqrt(((weighted_matrix - ideal_best) ** 2).sum(axis=1))
    distance_worst = np.sqrt(((weighted_matrix - ideal_worst) ** 2).sum(axis=1))

    # Step 5: Calculate Topsis Score
    topsis_score = distance_worst / (distance_best + distance_worst)

    # Step 6: Rank (Highest score gets Rank 1)
    rank = topsis_score.argsort()[::-1] + 1

    # ---------------------------------------------------
    # 7. Append results
    # ---------------------------------------------------
    data['Topsis Score'] = topsis_score
    data['Rank'] = rank

    # ---------------------------------------------------
    # 8. Save Output File
    # ---------------------------------------------------
    try:
        if output_file.endswith('.xlsx'):
            data.to_excel(output_file, index=False)
        elif output_file.endswith('.csv'):
            data.to_csv(output_file, index=False)
        else:
            error("Output file must be .xlsx or .csv format.")
    except Exception:
        error("Error writing output file.")

    print("TOPSIS successfully calculated.")
    print("Output saved to:", output_file)


if __name__ == "__main__":
    main()
