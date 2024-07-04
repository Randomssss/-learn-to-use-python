import unittest
from main import measure_load_time

class TestSpeed(unittest.TestCase):
    def test_measure_load_time(self):
        url = "https://chatgpt.com"
        load_time = measure_load_time(url)
        self.assertLessEqual(load_time, 5.0, "Load time should be less than or equal to 5 seconds")

if __name__ == '__main__':
    unittest.main()
