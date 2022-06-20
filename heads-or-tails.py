import numpy as np

def weighted_lottery(weights):
    container_list = []

    for (name, weight) in weights.items():
        for _ in range(weight):
            container_list.append(name)

    return np.random.choice(container_list)

weights = {
    'heads': 1,
    'tails': 1,
}

print(weighted_lottery(weights))