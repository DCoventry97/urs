import xml.etree.ElementTree as ET


def make_new_xml_file(xml_file):
    """
    Makes an xml file with a root to store the users short words and associated urls.
    :param xml_file: Name of the xml file to make.
    """
    root = ET.Element("shortenedUrls")
    tree = ET.ElementTree(root)
    tree.write(xml_file)
