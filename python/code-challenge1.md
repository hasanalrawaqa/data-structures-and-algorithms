# array-reverse

## Whiteboard Process

![Whiteboard](../White%20board_page-0001.jpg)

## Approach & Efficiency

The approach of the reverseArray function is to create a new empty array and iterate through the original array from the end to the start, pushing each element into the new array. Once all elements have been added to the new array, it is returned as the reversed array.

In terms of efficiency, the function has a time complexity of O(n) where n is the length of the input array, since it must iterate through the entire array once. The space complexity is also O(n), since a new array is created to store the reversed elements.

## Solution

```
def reverse_array(arr):
    reversed_arr = []
    for i in range(len(arr)-1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr
```
