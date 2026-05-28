from textnode import TextNode, TextType

def main():
    text_nodes = [
        TextNode("Hello, world!", TextType.PLAIN),
        TextNode("Bold text", TextType.BOLD),
        TextNode("Italic text", TextType.ITALIC),
        TextNode("Code snippet", TextType.CODE),
        TextNode("Link", TextType.LINK, "https://example.com"),
        TextNode("Image", TextType.IMAGE, "https://example.com/image.png"),
    ]

    for node in text_nodes:
        print(node)

main()