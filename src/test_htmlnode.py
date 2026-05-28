import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        cases = [
            (HTMLNode(props={"href": "https://example.com", "target": "_blank"}), ' href="https://example.com" target="_blank"'),
            (HTMLNode(props={"href": "https://example.com"}), ' href="https://example.com"'),
            (HTMLNode(props={"target": "_blank"}), ' target="_blank"'),
            (HTMLNode(), ""),
        ]
        for node, expected in cases:
            with self.subTest():
                self.assertEqual(node.props_to_html(), expected)
    
    def test_repr(self):
        cases = [
            (HTMLNode(tag="div", value="Hello", children=[HTMLNode()], props={"class": "container"}), "HTMLNode(tag=div, value=Hello, children=[HTMLNode(tag=None, value=None, children=None, props=None)], props={'class': 'container'})"),
            (HTMLNode(), "HTMLNode(tag=None, value=None, children=None, props=None)"),
        ]
        for node, expected in cases:
            with self.subTest():
                self.assertEqual(repr(node), expected)

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        cases = [
            (LeafNode(tag="p", value="Hello, world!"), '<p>Hello, world!</p>'),
            (LeafNode(tag="a", value="Click here", props={"href": "https://example.com"}), '<a href="https://example.com">Click here</a>'),
            (LeafNode(tag="span", value="Important", props={"style": "color: red;"}), '<span style="color: red;">Important</span>'),
            (LeafNode(tag=None, value="Just text"), 'Just text'),
        ]
        for node, expected in cases:
            with self.subTest():
                self.assertEqual(node.to_html(), expected)

    def test_repr(self):
        cases = [
            (LeafNode(tag="p", value="Hello, world!"), "LeafNode(tag=p, value=Hello, world!, props=None)"),
            (LeafNode(tag="a", value="Click here", props={"href": "https://example.com"}), "LeafNode(tag=a, value=Click here, props={'href': 'https://example.com'})"),
            (LeafNode(tag=None, value="Just text"), "LeafNode(tag=None, value=Just text, props=None)"),
        ]
        for node, expected in cases:
            with self.subTest():
                self.assertEqual(repr(node), expected)

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        cases = [
            (ParentNode(tag="div", children=[LeafNode(tag="p", value="Hello")]), '<div><p>Hello</p></div>'),
            (ParentNode(tag="ul", children=[LeafNode(tag="li", value="Item 1"), LeafNode(tag="li", value="Item 2")]), '<ul><li>Item 1</li><li>Item 2</li></ul>'),
            (ParentNode(tag="div", children=[ParentNode(tag="ul", children=[LeafNode(tag="li", value="Nested item 1"), LeafNode(tag="li", value="Nested item 2")])], props={"class": "container"}), '<div class="container"><ul><li>Nested item 1</li><li>Nested item 2</li></ul></div>'),
        ]
        for node, expected in cases:
            with self.subTest():
                self.assertEqual(node.to_html(), expected)

    def test_repr(self):
        cases = [
            (ParentNode(tag="div", children=[LeafNode(tag="p", value="Hello")]), "ParentNode(tag=div, children=[LeafNode(tag=p, value=Hello, props=None)], props=None)"),
            (ParentNode(tag="ul", children=[LeafNode(tag="li", value="Item 1"), LeafNode(tag="li", value="Item 2")]), "ParentNode(tag=ul, children=[LeafNode(tag=li, value=Item 1, props=None), LeafNode(tag=li, value=Item 2, props=None)], props=None)"),
            (ParentNode(tag="div", children=[ParentNode(tag="ul", children=[LeafNode(tag="li", value="Nested item 1"), LeafNode(tag="li", value="Nested item 2")])], props={"class": "container"}), "ParentNode(tag=div, children=[ParentNode(tag=ul, children=[LeafNode(tag=li, value=Nested item 1, props=None), LeafNode(tag=li, value=Nested item 2, props=None)], props=None)], props={'class': 'container'})"),
        ]
        for node, expected in cases:
            with self.subTest():
                self.maxDiff = None
                self.assertEqual(repr(node), expected)

if __name__ == "__main__":
    unittest.main()