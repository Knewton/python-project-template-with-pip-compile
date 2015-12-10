from my_project.my_module import get_page_title


def test_get_page_title():
    """
    These tests check that the title retrieved from the PyPI main page is correct.
    """
    title_lower_case = get_page_title("https://pypi.python.org/pypi").lower()
    assert "python" in title_lower_case
    assert "package" in title_lower_case
    assert "index" in title_lower_case
    assert "cats" not in title_lower_case
