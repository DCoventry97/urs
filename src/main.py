#!/usr/bin/python3
import sys
import xml.etree.ElementTree as ET
from check_input import check_input


def main():
    tree = ET.parse("../urls.xml")
    root = tree.getroot()

    decision = check_input(sys.argv, root)
    if decision == -1:
        print("Invalid Arguments Given: use help to learn more about arguments.")


main()