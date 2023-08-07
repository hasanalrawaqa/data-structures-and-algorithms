import pytest
from hashmap_left_join import left_join

class TestHashMapLeftJoin(unittest.TestCase):
    def test_left_join(self):
        synonyms = {
            'diligent': 'employed',
            'fond': 'enamored',
            'guide': 'usher',
            'outfit': 'garb',
            'wrath': 'anger',
        }
        antonyms = {
            'diligent': 'idle',
            'fond': 'averse',
            'guide': 'follow',
            'flow': 'jam',
            'wrath': 'delight',
        }
        expected_output = [
            ['diligent', 'employed', 'idle'],
            ['fond', 'enamored', 'averse'],
            ['guide', 'usher', 'follow'],
            ['outfit', 'garb', None],
            ['wrath', 'anger', 'delight'],
        ]
        self.assertEqual(left_join(synonyms, antonyms), expected_output)

    def test_left_join_empty(self):
        # Test with empty hashmaps
        synonyms = {}
        antonyms = {}
        expected_output = []
        self.assertEqual(left_join(synonyms, antonyms), expected_output)

    def test_left_join_missing_keys(self):
        # Test with a key present in synonyms but not in antonyms
        synonyms = {'key1': 'value1', 'key2': 'value2'}
        antonyms = {}
        expected_output = [['key1', 'value1', None], ['key2', 'value2', None]]
        self.assertEqual(left_join(synonyms, antonyms), expected_output)