import numpy as np

def calculate(list):
    
    if len(list) <= 9:
        #arr = np.array([[list[0],list[1],list[2]], [list[3],list[4],list[5]], [list[6],list[7],list[8]]], np.int8)
        ar = np.array(list)
        arr = ar.reshape(3,3)
        calculations = {
            'mean': [np.mean(arr, axis=0), np.mean(arr, axis=1), np.mean(arr)],
            'variance': [np.var(arr, axis=0), np.var(arr, axis=1), np.var(arr) ],
            'standard deviation': [np.std(arr, axis=0), np.std(arr, axis=1), np.std(arr)],
            'max': [np.max(arr, axis=0), np.max(arr, axis=1), np.max(arr)],
            'min': [np.min(arr, axis=0), np.min(arr, axis=1), np.min(arr)],
            'sum': [np.sum(arr, axis=0), np.sum(arr, axis=1), np.sum(arr)],
            }
    else:
        print("List must contain nine numbers.")

    return calculations

print(calculate([0,1,2,3,4,5,6,7,8]))