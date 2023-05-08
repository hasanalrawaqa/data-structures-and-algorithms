# Code Challenge 02

## Array insert shift
----------------------------------------------------------------
![Alt text](../codechallanege%202%20_page-0001.jpg)

### Approach & Efficiency

Approach: The function calculates the middle index of the input arr, and then creates a new array by slicing arr before and after the middle index, and inserting val in the middle.
Time complexity: O(n), where n is the length of the input arr. This is because the function needs to create a new array with length n+1 and copy all n elements from the input arr into the new array.
Space complexity: O(n+1), where n is the length of the input arr. This is because the function creates a new array with length n+1 to store the modified array.

### Solution

```
def insertShiftArray(arr, val):
    if len(arr) % 2 == 0:
        mid = len(arr) // 2
    else:
        mid = len(arr) // 2 + 1
    arr = arr[:mid] + [val] + arr[mid:]
    return arr
 ```
----------------------------------------------------------------
## remove Middle Element
----------------------------------------------------------------
![Alt text](../codechallanege%202%20-2_page-0001.jpg)

### Approach & Efficiency

Approach: The function calculates the middle index of the input arr, and then creates a new array by slicing arr before and after the middle index, excluding the middle element.
Time complexity: O(n), where n is the length of the input arr. This is because the function needs to create a new array with length n-1 and copy all n-1 elements from the input arr into the new array.
Space complexity: O(n-1), where n is the length of the input arr. This is because the function creates a new array with length n-1 to store the modified array.

### solution

``` 
def removeMiddleElement(arr):
    if len(arr) % 2 == 0:
        mid = len(arr) // 2-1
    else:
        mid = len(arr) // 2
    arr = arr[:mid] + arr[mid+1:]
    return arr
```