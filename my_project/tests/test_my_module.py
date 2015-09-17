from my_project.my_module import get_page_title

import unittest


class MyProjectTests(unittest.TestCase):
    def test_get_page_title(self):
        """
        These tests check that the title retrieved from the PyPI main page is correct.
        """
        title_lower_case = get_page_title("https://pypi.python.org/pypi").lower()
        self.assertIn("python", title_lower_case)
        self.assertIn("package", title_lower_case)
        self.assertIn("index", title_lower_case)
        self.assertNotIn("cats", title_lower_case)
