class HashTable:
    def __init__(self):
        # Initialize an empty list to store the key-value pairs
        self.table = []

    def hash(self, key):
        # Implement your hash function here to convert the key into an index
        # Return the index

    def set(self, key, value):
        index = self.hash(key)
        # Handle collisions using chaining or other techniques
        # Update the key-value pair in the table or add a new entry

    def get(self, key):
        index = self.hash(key)
        # Search for the key in the appropriate bucket and return the value if found
        # Otherwise, return None

    def has(self, key):
        index = self.hash(key)
        # Check if the key exists in the table, return True if found, else False

    def keys(self):
        # Return a collection of all unique keys in the hashtable
