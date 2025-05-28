import numpy as np

def calculate(input_list):
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(input_list).reshape(3, 3)

    stats = ['mean', 'var', 'std', 'max', 'min', 'sum']

    return {
        name.replace('var', 'variance').replace('std', 'standard deviation'): [
            getattr(matrix, name)(axis=0).tolist(),  # column-wise
            getattr(matrix, name)(axis=1).tolist(),  # row-wise
            getattr(matrix, name)().item()           # overall
        ]
        for name in stats
    }
