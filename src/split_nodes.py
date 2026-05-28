from textnode import TextNode, TextType

def split_nodes_delimiter(
    old_nodes: list[TextNode], 
    delimiter: str, 
    text_type: TextType
) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN:
            new_nodes.append(old_node)
            continue
        
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError(f"Delimiter '{delimiter}' is not balanced in text: '{old_node.text}'")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(text=sections[i], text_type=TextType.PLAIN))
            else:
                split_nodes.append(TextNode(text=sections[i], text_type=text_type))
        new_nodes.extend(split_nodes)
    return new_nodes