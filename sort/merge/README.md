# Blog Article: Merge Sort Explained Step-by-Step

## Introduction:

In this blog article, we will explore the Merge Sort algorithm and provide a step-by-step explanation using a sample array. Merge Sort is a divide-and-conquer sorting algorithm that divides the input array into smaller subarrays, sorts them individually, and then merges them to obtain the final sorted array. It has a time complexity of O(n log n) and is considered an efficient sorting algorithm. We will review the algorithm's pseudocode, trace the process with a sample array, and visualize the output at each iteration.

## Pseudocode:

Before diving into the step-by-step process, let's review the pseudocode for the Merge Sort algorithm:

```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
        DECLARE mid <-- n/2
        DECLARE left <-- arr[0...mid]
        DECLARE right <-- arr[mid...n]
        // sort the left side
        Mergesort(left)
        // sort the right side
        Mergesort(right)
        // merge the sorted left and right sides together
        Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
        set remaining entries in arr to remaining values in right
    else
        set remaining entries in arr to remaining values in left
```

## Step-by-Step Explanation:

Now, let's step through the Merge Sort algorithm using a sample array `[8, 4, 23, 42, 16, 15]` and visualize the output after each iteration.

Pass 1:

Pass 1 of Merge Sort

In the first pass of Merge Sort, the input array is divided into two halves: `[8, 4, 23]` and `[42, 16, 15]`. The left half is recursively sorted using the `Mergesort` function, which further divides it into `[8]` and `[4, 23]`. The right half is recursively sorted as well, resulting in `[42]` and `[16, 15]`.

Pass 2:

Pass 2 of Merge Sort

The second pass merges the sorted subarrays. For the left side, we compare 8 with 4 and 23. Since 4 is smaller, it becomes the first element of the merged array. Next, we compare 8 with 23 and insert them accordingly. The left side is now sorted as `[4, 8, 23]`.

For the right side, we compare 42 with 16 and 15. As 15 is smaller, it becomes the first element of the merged array. We then compare 42 with 16 and insert them in the correct order. The right side is now sorted as `[15, 16, 42]`.

Finally, we merge the sorted left and right sides together, resulting in the fully sorted array `[4, 8, 15, 16, 23, 42]`.

After the iteration completes, the array `[8, 4, 23, 42, 16, 15]` is sorted into `[4, 8, 15, 16, 23, 42]`.

## Implementation in Python:

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        merge(left, right, arr)

def merge(left, right, arr):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

# Testing the implementation
sample_array = [8, 4, 23, 42, 16, 15]
merge_sort(sample_array)
print(sample_array)
```

**Output: `[4, 8, 15, 16, 23, 42]`**

## Conclusion:

In this article, we explored the Merge Sort algorithm step-by-step using a sample array. We visualized the output after each iteration and gained a better understanding of how the algorithm works. Additionally, we provided an implementation of Merge Sort in Python and tested it with the sample array to verify its correctness. Merge Sort is an efficient sorting algorithm that guarantees a time complexity of O(n log n) and is widely used in practice. It is particularly useful for handling large data sets and provides a stable sorting solution.

***The Big O notation for the Merge Sort algorithm is as follows:***

**Time Complexity: O(n log n)**
Merge Sort has a time complexity of O(n log n) in all cases, where n represents the number of elements in the input array. This time complexity is achieved due to the divide-and-conquer strategy employed by Merge Sort. The algorithm divides the input array into smaller subarrays recursively until the base case is reached. Each division takes O(log n) time, and the merging process takes O(n) time. Since the merging process occurs log n times, the overall time complexity is O(n log n).

**Space Complexity: O(n)**
Merge Sort has a space complexity of O(n) because it requires additional space to store the merged result of subarrays during the merging process. In the worst case, when merging two subarrays, the temporary merged array can be as large as the original input array. Hence, the space complexity is linear, scaling with the size of the input array.
