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

def left_join(synonyms, antonyms):
    result = []

    for key in synonyms:
        synonym = synonyms[key]
        antonym = antonyms.get(key, None)  
        result.append([key, synonym, antonym])

    return result
