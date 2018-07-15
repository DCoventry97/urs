import xml.etree.ElementTree as ET


def make_new_xml_file(xml_file):
    root = ET.Element("shortenedUrls")
    tree = ET.ElementTree(root)
    tree.write(xml_file)