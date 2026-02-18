import pandas as pd
import numpy as np

def calculate_topsis(input_file, weights, impacts, output_file):
    if input_file.endswith('.xlsx'):
        data = pd.read_excel(input_file)
    else:
        data = pd.read_csv(input_file)

    weights = list(map(float, weights.split(',')))
    impacts = impacts.split(',')

    matrix = data.iloc[:, 1:].values
    norm = np.sqrt((matrix ** 2).sum(axis=0))
    normalized = matrix / norm
    weighted = normalized * weights

    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(max(weighted[:, i]))
            ideal_worst.append(min(weighted[:, i]))
        else:
            ideal_best.append(min(weighted[:, i]))
            ideal_worst.append(max(weighted[:, i]))

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    dist_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    score = dist_worst / (dist_best + dist_worst)
    rank = score.argsort()[::-1] + 1

    data["Topsis Score"] = score
    data["Rank"] = rank

    data.to_excel(output_file, index=False)
