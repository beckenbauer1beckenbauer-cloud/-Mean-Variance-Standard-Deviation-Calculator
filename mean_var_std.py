import numpy as np
def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    matrix = np.array(list).reshape(3, 3)
    def stats(arr):
        return [
            arr.mean(axis=0).tolist(),
            arr.mean(axis=1).tolist(),
            arr.mean().tolist()
        ]
    def var(arr):
        return [
            arr.var(axis=0).tolist(),
            arr.var(axis=1).tolist(),
            arr.var().tolist()
        ]
    def std(arr):
        return [
            arr.std(axis=0).tolist(),
            arr.std(axis=1).tolist(),
            arr.std().tolist()
        ]
    def max_vals(arr):
        return [
            arr.max(axis=0).tolist(),
            arr.max(axis=1).tolist(),
            arr.max().tolist()
        ]
    def min_vals(arr):
        return [
            arr.min(axis=0).tolist(),
            arr.min(axis=1).tolist(),
            arr.min().tolist()
        ]
    def sum_vals(arr):
        return [
            arr.sum(axis=0).tolist(),
            arr.sum(axis=1).tolist(),
            arr.sum().tolist()
        ]
    return {
        'mean': stats(matrix),
        'variance': var(matrix),
        'standard deviation': std(matrix),
        'max': max_vals(matrix),
        'min': min_vals(matrix),
        'sum': sum_vals(matrix)
    }
if __name__ == "__main__":
    result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
    for key, value in result.items():
        print(f"{key}:")
        print(f"  columns: {value[0]}")
        print(f"  rows:    {value[1]}")
        print(f"  flat:    {value[2]}")
