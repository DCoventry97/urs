#!/usr/bin/python3
import sys
import webbrowser
import xml.etree.ElementTree as ET
from check_input import check_input
from shortened_url import get_url, check_new_url, add_url_to_xml


def main():
    tree = ET.parse("../urls.xml")
    root = tree.getroot()

    decision = check_input(sys.argv, root)
    if decision == -1:
        print("Invalid Arguments Given: use help to learn more.")
        exit()

    elif decision == 0:
        webbrowser.open_new(get_url(sys.argv[1], root));

    elif decision == 1:
        if check_new_url(sys.argv):
            short_url = sys.argv[2]
            long_url = sys.argv[3]
            add_url_to_xml(short_url, long_url, tree, "../urls.xml")



main()

