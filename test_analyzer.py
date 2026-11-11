import os
import unittest
from text_analyzer import analyze_text, read_text_file


class TestTextAnalyzer(unittest.TestCase):

    def test_word_count_and_frequency(self):
        sample = "Мова та мовлення. Мова є важливою."
        res = analyze_text(sample)
        self.assertEqual(res["total_words"], 6)
        self.assertEqual(res["frequency_dict"]["мова"], 2)
        self.assertEqual(res["frequency_dict"]["важливою"], 1)

    def test_empty_text_handling(self):
        res = analyze_text("   \n\t  ")
        self.assertEqual(res["total_words"], 0)
        self.assertEqual(res["frequency_dict"], {})

    def test_file_not_found_exception(self):
        with self.assertRaises(FileNotFoundError):
            read_text_file("non_existing_file_123.txt")

    def test_empty_file_exception(self):
        temp_file = "temp_empty.txt"
        with open(temp_file, "w", encoding="utf-8") as f:
            f.write("   ")
        try:
            with self.assertRaises(ValueError):
                read_text_file(temp_file)
        finally:
            if os.path.exists(temp_file):
                os.remove(temp_file)


if __name__ == "__main__":
    unittest.main()