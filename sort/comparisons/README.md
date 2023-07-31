# Code Challenge no.28: Comparisons

## Approach & Efficiency

### Movies Sorted Methods

The code challenge involves implementing two methods for sorting a list of movie objects.

1. **By year**: This method sorts movies by year in descending order. It takes a list of movie objects as input and returns an ordered list of objects based on the most recent years.

2. **By title**: This method sorts movies by title while ignoring leading "A"s, "An"s, or "The"s. It takes a list of movie objects as input and returns an ordered list of objects based on alphabetical order, ignoring the specified prefixes.

The space complexity of both methods is O(1) since they do not use any additional data structures that grow with the input size.

The time complexity of both methods is O(n log n), where 'n' represents the number of movie objects in the input list. This is due to the sorting operation using the `sorted` function.

## Solution

The code provides two methods, `movies_sorted_by_year` and `movies_sorted_by_title`, which implement the required sorting functionality. The methods take a list of movie objects as input and return the sorted list based on the specified criteria.

To run the tests and verify the correctness of the sorting methods, execute the following command:

```
pytest tests/test_objects_sort.py
```

This will run the test cases defined in the `test_objects_sort.py` file and provide the test results, ensuring that the sorting methods are working as expected.

Make sure to have the required dependencies installed and the project set up correctly before running the tests.

Feel free to explore the code and modify it as needed for your specific use case or further enhancements.