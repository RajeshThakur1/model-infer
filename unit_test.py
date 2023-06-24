import unittest
import random

def generate_random_array(sentence):
    random.seed(sentence)
    random_array = [random.random() for _ in range(500)]
    return random_array

class TestGenerateRandomArray(unittest.TestCase):

    def test_empty_sentence(self):
        input_sentence = ""
        random_array = generate_random_array(input_sentence)
        self.assertEqual(len(random_array), 500)

    def test_sentence_with_spaces(self):
        input_sentence = "       "
        random_array = generate_random_array(input_sentence)
        self.assertEqual(len(random_array), 500)

    def test_sentence_with_special_characters(self):
        input_sentence = "!@#$%^&*()_+"
        random_array = generate_random_array(input_sentence)
        self.assertEqual(len(random_array), 500)

    def test_sentence_with_single_word(self):
        input_sentence = "Hello"
        random_array = generate_random_array(input_sentence)
        self.assertEqual(len(random_array), 500)

    def test_sentence_with_multiple_words(self):
        input_sentence = "This is a test sentence."
        random_array = generate_random_array(input_sentence)
        self.assertEqual(len(random_array), 500)

    def test_identical_sentences(self):
        input_sentence1 = "OpenAI is amazing."
        input_sentence2 = "OpenAI is amazing."
        random_array1 = generate_random_array(input_sentence1)
        random_array2 = generate_random_array(input_sentence2)
        self.assertEqual(random_array1, random_array2)

    def test_different_sentences(self):
        input_sentence1 = "OpenAI is amazing."
        input_sentence2 = "OpenAI is incredible."
        random_array1 = generate_random_array(input_sentence1)
        random_array2 = generate_random_array(input_sentence2)
        self.assertNotEqual(random_array1, random_array2)

    def test_long_sentence(self):
        input_sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin id ligula at mi pharetra vestibulum. Sed non mauris vulputate, blandit odio quis, malesuada neque. In eget scelerisque urna."
        random_array = generate_random_array(input_sentence)
        self.assertEqual(len(random_array), 500)

    def test_value_range(self):
        input_sentence = "Test"
        random_array = generate_random_array(input_sentence)
        self.assertTrue(all(0 <= value <= 1 for value in random_array))

if __name__ == '__main__':
    unittest.main()
