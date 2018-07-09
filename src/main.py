#!/usr/bin/python3
import sys
import xml.etree.ElementTree as ET
from check_input import check_input

tree = ET.parse("../urls.xml")
root = tree.getroot()

decision = check_input(sys.argv, root)

if decision == -1:
    print("Invalid input, use ")





