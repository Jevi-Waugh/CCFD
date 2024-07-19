

arr = [50,4,30,32,1]

def func(index : int):
    return arr[index]

def argsort_lambda(arr: list):
    return sorted(range(len(arr)), key=lambda x: arr[x])

def argsort_get_item(arr: list):
    return sorted(range(len(arr)), key=arr.__getitem__)

def argsort_func(arr: list):
    return sorted(range(len(arr)), key=func)
