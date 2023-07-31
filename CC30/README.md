# Code Challenge no.30: Hash Tables

## Description
In this challenge, you are required to implement a Hashtable class with specific methods: `set`, `get`, `has`, `keys`, and `hash`. The Hashtable class should handle collisions using appropriate techniques, such as chaining or open addressing. Additionally, you need to write tests to verify the functionality of each method and ensure that it satisfies the given requirements.

## Approach & Efficiency
For the `set` method, the approach involves hashing the key and then handling collisions to insert or update the key-value pair in the Hashtable. The `get` method retrieves the value associated with a given key by searching for it in the appropriate bucket. The `has` method checks whether a key exists in the Hashtable or not. The `keys` method returns a collection of all unique keys in the Hashtable. Lastly, the `hash` method calculates the index in the Hashtable for a given key.

The time complexity for each method depends on the efficiency of the hash function and the collision resolution technique. In the average case, for a well-distributed hash function and minimal collisions, the time complexity for `set`, `get`, `has`, and `hash` methods is O(1) or constant time. However, in the worst case scenario with many collisions, the time complexity could degrade to O(n) or linear time.

Regarding space complexity, it depends on the number of unique keys and the collision resolution technique used. In general, the space complexity for the Hashtable is O(n), where n is the number of unique keys stored in the Hashtable.

## Solution
To run your code and perform tests, you can follow these steps:

1. Implement the `HashTable` class with the required methods: `set`, `get`, `has`, `keys`, and `hash`. Ensure that you handle collisions appropriately.

2. Write the tests to verify the functionality of each method. Ensure that you cover all the scenarios mentioned in the specifications.

3. Save your `HashTable` class in a file named `hashtable.py`.

4. Save the tests in a separate file named `test_hashtable.py`.

5. Install pytest if you haven't already:

```bash
pip install pytest
```

6. Run the tests using pytest:

```bash
pytest test_hashtable.py
```

7. Check the test results to ensure that all tests are passing successfully.

Remember to use meaningful and descriptive variable names and to handle any potential edge cases in your implementation.

Good luck with your Hashtable implementation! If you encounter any issues or have further questions, feel free to ask.