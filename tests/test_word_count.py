import unittest
from src.word_count import word_count

class TestWordCount(unittest.TestCase):
    def test_word_count(self):
        input_data = ["hello world", "hello PySpark"]
        expected_output = [("hello", 2), ("world", 1), ("PySpark", 1)]
        result = word_count(input_data)
        self.assertCountEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()
