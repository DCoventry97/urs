#!/usr/bin/python3
import sys
import xml.etree.ElementTree as ET
from check_input import check_input

tree = ET.parse("urls.xml")
root = tree.getroot()

check_input(sys.argv, root)






