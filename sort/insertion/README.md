# Blog Article: Insertion Sort Explained Step-by-Step

## Introduction:

-----------------------------------------------------

In this blog article, we will explore the Insertion Sort algorithm and provide a step-by-step explanation using a sample array. Insertion Sort is a comparison-based sorting algorithm that builds the final sorted array one element at a time. It is efficient for small data sets and performs well on nearly sorted arrays. We will review the algorithm's pseudocode, trace the process with a sample array, and visualize the output at each iteration.


## Pseudocode:

------------------------------------------------------------

Before diving into the step-by-step process, let's review the pseudocode for the Insertion Sort algorithm:

```
InsertionSort(int[] arr)
    DECLARE n <-- arr.Length;
    FOR i = 0 to n - 1
        DECLARE min <-- i;
        FOR j = i + 1 to n
            if (arr[j] < arr[min])
                min <-- j;

        DECLARE temp <-- arr[min];
        arr[min] <-- arr[i];
        arr[i] <-- temp;
```

## Step-by-Step Explanation:

--------------------------------------------------------

Now, let's step through the Insertion Sort algorithm using a sample array `[8, 4, 23, 42, 16, 15]` and visualize the output after each iteration.

### Pass 1:

Pass 1 of Insertion Sort

In the first pass of Insertion Sort, we evaluate the elements in the array and find the smallest value. Initially, the smallest value is at index 0 (8). We swap it with the value at index 1 (4), resulting in `[4, 8, 23, 42, 16, 15]`.

### Pass 2:

Pass 2 of Insertion Sort

The second pass compares the elements from index 1 onwards and finds the smallest value, which is already in the correct position (8). No swaps are needed, and the array remains `[4, 8, 23, 42, 16, 15]`.

### Pass 3:

Pass 3 of Insertion Sort

During the third pass, we evaluate the elements from index 2 onwards. The smallest value is 15, so we swap it with the value at index 2, resulting in `[4, 8, 15, 42, 16, 23]`.

### Pass 4:

Pass 4 of Insertion Sort

In the fourth pass, we consider the elements from index 3 onwards. The smallest value is 16, which is in the correct position. Therefore, no swaps are needed, and the array remains `[4, 8, 15, 42, 16, 23]`.

### Pass 5:

Pass 5 of Insertion Sort

The fifth pass evaluates the elements from index 4 onwards. We find that 16 is smaller than 23, so we swap them. The array becomes `[4, 8, 15, 16, 42, 23]`.

### Pass 6:

Pass 6 of Insertion Sort

On the final iteration, we compare the elements from index 5 onwards. The smallest value is 23, which is already in its correct position. No swaps are needed, and the array remains `[4, 8, 15, 16, 23, 42]`.

After iterating through the entire input array, we obtain the final sorted array `[4, 8, 15, 16, 23, 42]`.

## Implementation in Python:

----------------------------------------------------------------

```python
def insertion_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Testing the implementation
sample_array = [8, 4, 23, 42, 16, 15]
insertion_sort(sample_array)
print(sample_array)
```

Output: `[4, 8, 15, 16, 23, 42]`

## Conclusion:
 
 ------------------------------------------------

In this article, we explored the Insertion Sort algorithm step-by-step using a sample array. We visualized the output after each iteration and gained a better understanding of how the algorithm works. Additionally, we provided an implementation of Insertion Sort in Python and tested it with the sample array to verify its correctness. Insertion Sort is a simple yet efficient sorting algorithm that can be useful in various scenarios, especially for small or nearly sorted arrays.


***The Big O notation for the Insertion Sort algorithm is as follows:***

Time Complexity: O(n^2)
The worst-case time complexity of Insertion Sort is quadratic, O(n^2). This is because for each element in the input array, we need to compare it with all the previous elements in the sorted subarray to determine its correct position. This results in nested loops and leads to a time complexity of n * (n - 1), which simplifies to O(n^2).

Space Complexity: O(1)
The space complexity of Insertion Sort is constant, O(1), because the algorithm performs sorting in-place. It doesn't require any additional space that scales with the input size. The sorting is done by swapping elements within the original array, without using any auxiliary data structures.