def insertShiftArray(arr, val):
    if len(arr) % 2 == 0:
        mid = len(arr) // 2
    else:
        mid = len(arr) // 2 + 1
    arr = arr[:mid] + [val] + arr[mid:]
    return arr

def removeMiddleElement(arr):
    if len(arr) % 2 == 0:
        mid = len(arr) // 2-1
    else:
        mid = len(arr) // 2
    arr = arr[:mid] + arr[mid+1:]
    return arr
