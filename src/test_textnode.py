import unittest
from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        cases = [
            ("Same", TextNode("Hello", TextType.PLAIN), TextNode("Hello", TextType.PLAIN), True),
            ("Type change", TextNode("Hello", TextType.PLAIN), TextNode("Hello", TextType.BOLD), False),
            ("Different text", TextNode("Hello", TextType.PLAIN), TextNode("Hi", TextType.PLAIN), False),
            ("Same link", TextNode("Hello", TextType.PLAIN, "https://example.com"), TextNode("Hello", TextType.PLAIN, "https://example.com"), True),
            ("Different link", TextNode("Hello", TextType.PLAIN, "https://example.com"), TextNode("Hello", TextType.PLAIN, "https://example.org"), False),
        ]
        for description, node1, node2, expected in cases:
            with self.subTest(description=description):
                self.assertEqual(node1 == node2, expected)

    def test_repr(self):
        cases = [
            (TextNode("Hello", TextType.PLAIN), "TextNode(text=Hello, text_type=TextType.PLAIN, url=None)"),
            (TextNode("Link", TextType.LINK, "https://example.com"), "TextNode(text=Link, text_type=TextType.LINK, url=https://example.com)"),
        ]
        for node, expected in cases:
            with self.subTest():
                self.assertEqual(repr(node), expected)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_node_to_html_node(self):
        cases = [
            (TextNode("Hello", TextType.PLAIN), "Hello"),
            (TextNode("Bold", TextType.BOLD), "<b>Bold</b>"),
            (TextNode("Italic", TextType.ITALIC), "<i>Italic</i>"),
            (TextNode("Code", TextType.CODE), "<code>Code</code>"),
            (TextNode("Link", TextType.LINK, "https://example.com"), '<a href="https://example.com">Link</a>'),
            (TextNode("", TextType.IMAGE, "https://example.com/image.png"), '<img src="https://example.com/image.png"></img>'),
        ]
        for text_node, expected_html in cases:
            with self.subTest():
                html_node = text_node_to_html_node(text_node)
                self.assertEqual(html_node.to_html(), expected_html)

if __name__ == "__main__":
    unittest.main()