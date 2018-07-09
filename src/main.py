#!/usr/bin/python3
import sys
import webbrowser
import xml.etree.ElementTree as ET
from check_input import check_input
from shortened_url import get_url


def main():
    tree = ET.parse("../urls.xml")
    root = tree.getroot()

    decision = check_input(sys.argv, root)
    if decision == -1:
        print("Invalid Arguments Given: use help to learn more about arguments.")
        exit()

    elif decision == 0:
        webbrowser.open_new(get_url(sys.argv[1], root));


main()

