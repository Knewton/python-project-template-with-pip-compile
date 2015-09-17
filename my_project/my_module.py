from lxml import html
import requests


def get_page_title(url):
    """
    This is a simple function that returns the title of an HTML page.

    :param str url: the URL to an HTML page
    :return str: the title (from the HTML "head" section) of the page
    """
    response = requests.get(url)
    parsed_tree = html.fromstring(response.content)
    title, = parsed_tree.xpath('//head/title/text()')
    return title
