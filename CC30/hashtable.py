
class HashTable:
    def __init__(self, size=100):
        # Initialize the table with a given size (default size is 100)
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def __hash(self, key):
        # Private method to calculate the index for the given key
        return hash(key) % self.size

    def set(self, key, value):
        index = self.__hash(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self.__hash(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None

    def has(self, key):
        index = self.__hash(key)
        for item in self.table[index]:
            if item[0] == key:
                return True
        return False

    def keys(self):
        keys_set = set()
        for bucket in self.table:
            for item in bucket:
                keys_set.add(item[0])
        return list(keys_set)


# Write a function to find the first repeated word
def repeated_word(input_string):
    # Convert the input string to lowercase and remove punctuation
    cleaned_string = ''.join(char.lower() if char.isalnum() else ' ' for char in input_string)
    
    # Split the cleaned string into words
    words = cleaned_string.split()
    
    # Create a set to store encountered words
    word_set = set()
    
    # Iterate through the words and find the first repeated word
    for word in words:
        if word in word_set:
            return word
        word_set.add(word)

    # If no repeated word is found, return None
    return None

# stretch goals
#  Modify the function to return a count of each word in the provided string
def word_count(input_string):
    cleaned_string = ''.join(char.lower() if char.isalnum() else ' ' for char in input_string)
    words = cleaned_string.split()
    
    word_count_dict = {}
    for word in words:
        word_count_dict[word] = word_count_dict.get(word, 0) + 1
    
    return word_count_dict

# Modify the function to return a list of the words most frequently used in the provided string
def most_frequent_words(input_string, n):
    word_count_dict = word_count(input_string)
    
    # Sort the dictionary items based on the word count in descending order
    sorted_word_count = sorted(word_count_dict.items(), key=lambda x: x[1], reverse=True)
    
    # Get the first 'n' words from the sorted list
    return [word for word, _ in sorted_word_count[:n]]
