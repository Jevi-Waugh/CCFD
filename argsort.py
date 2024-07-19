import numpy as np


def key_func_warpper(arr: list):
    # returns value of the array based off index param
    def key_func(index : int):
        return arr[index]
    return key_func

def argsort_lambda(arr: list):
    return sorted(range(len(arr)), key=lambda x: arr[x])

def argsort_slice(arr: list, slice: int):
    return sorted(range(len(arr)), key=lambda x: arr[x])[:slice]

def argsort_get_item(arr: list):
    return sorted(range(len(arr)), key=arr.__getitem__)

def argsort_func(arr: list):
    key_func = key_func_warpper(arr)
    return sorted(range(len(arr)), key=key_func)

def argsort_numpy(arr, slice):
    return np.argsort(arr) if slice is None else np.argsort(arr)[:slice]