"""Convert XML elements into nested dictionaries, preserving attributes."""
import json
import xml.etree.ElementTree as ET

def element_to_data(element):
    children = list(element)
    if not children:
        text = (element.text or "").strip()
        if element.attrib:
            return {"@attributes": element.attrib, "#text": text}
        return text
    result = {}
    for child in children:
        value = element_to_data(child)
        if child.tag in result:
            if not isinstance(result[child.tag], list):
                result[child.tag] = [result[child.tag]]
            result[child.tag].append(value)
        else:
            result[child.tag] = value
    if element.attrib:
        result["@attributes"] = element.attrib
    return result

if __name__ == "__main__":
    root = ET.fromstring("<item id='7'><name>Pen</name><tag>office</tag><tag>blue</tag></item>")
    print(json.dumps({root.tag: element_to_data(root)}, indent=2))
