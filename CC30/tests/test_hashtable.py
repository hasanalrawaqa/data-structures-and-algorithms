import pytest
from hashtable import HashTable , repeated_word, most_frequent_words, word_count

def test_set():
    hashtable = HashTable()
    hashtable.set('key1', 'value1')
    assert hashtable.get('key1') == 'value1'

def test_retrieve():
    hashtable = HashTable()
    hashtable.set('key1', 'value1')
    assert hashtable.get('key1') == 'value1'

def test_non_existing_key():
    hashtable = HashTable()
    assert hashtable.get('non_existing_key') is None

def test_keys():
    hashtable = HashTable()
    hashtable.set('key1', 'value1')
    hashtable.set('key2', 'value2')
    hashtable.set('key3', 'value3')
    assert set(hashtable.keys()) == {'key1', 'key2', 'key3'}

def test_bucket_collision():
    hashtable = HashTable(size=2)  # Small size to force collision
    hashtable.set('key1', 'value1')
    hashtable.set('key2', 'value2')
    assert hashtable.get('key1') == 'value1'
    assert hashtable.get('key2') == 'value2'

def test_hashing():
    hashtable = HashTable(size=100)  # Large size to avoid collisions
    key = 'test_key'
    hashed_index = hashtable._HashTable__hash(key)
    assert 0 <= hashed_index < 100
    
# test for code challenge 31:
def test_repeated_word():
    assert repeated_word("Once upon a time, there was a brave princess who...") == "a"
    assert repeated_word("It was the best of times, it was the worst of times...") == "it"
    assert repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs...") == "summer"

def test_word_count():
    input_string = "Once upon a time, there was a brave princess who..."
    assert word_count(input_string) == {'once': 1, 'upon': 1, 'a': 2, 'time': 1, 'there': 1, 'was': 1, 'brave': 1, 'princess': 1, 'who': 1}

    input_string = "It was the best of times, it was the worst of times..."
    assert word_count(input_string) == {'it': 2, 'was': 2, 'the': 2, 'best': 1, 'of': 2, 'times': 2, 'worst': 1}

    input_string = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs..."
    assert word_count(input_string) == {'it': 1, 'was': 1, 'a': 1, 'queer': 1, 'sultry': 1, 'summer': 2, 'the': 2, 'they': 1, 'electrocuted': 1, 'rosenbergs': 1}

def test_most_frequent_words():
    input_string = "It was the best of times, it was the worst of times..."
    assert most_frequent_words(input_string, 2) == ['it', 'was']

    input_string = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs..."
    assert most_frequent_words(input_string, 3) == ['summer','the', 'it']