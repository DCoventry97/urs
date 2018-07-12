#!/usr/bin/python3
import sys
import webbrowser
import xml.etree.ElementTree as ET
from check_input import check_input, check_new_short_is_valid, check_new_short_is_unique
from shortened_url import get_url, check_new_url, add_url_to_xml, alter_short_url, is_shortened_url, delete_url
from help import get_help_message


def main():
    tree = ET.parse("../urls.xml")
    root = tree.getroot()

    decision = check_input(sys.argv, root)

    # If the user has input an invalid input
    if decision == -1:
        print("Invalid Arguments Given: use help to learn more.")

    # If the user has decided to open a short word
    elif decision == 0:
        webbrowser.open_new(get_url(sys.argv[1], root));

    # If the user has decided to add a new url
    elif decision == 1:
        if check_new_url(sys.argv):
            short_url = sys.argv[2]
            long_url = sys.argv[3]
            if not long_url.startswith("http://") and not long_url.startswith("https://"):
                long_url = "http://" + long_url
            add_url_to_xml(short_url, long_url, tree, "../urls.xml")

    # If the user needs help
    elif decision == 2:
        get_help_message()

    # If the user decided to re-name a short word
    elif decision == 3:
        try:
            if check_new_short_is_valid(sys.argv[2]) and check_new_short_is_unique(sys.argv[2], root) and \
                    is_shortened_url(sys.argv[3], root):
                alter_short_url(sys.argv[2], sys.argv[3], tree, "../urls.xml")
            else:
                print("Invalid Input: " + sys.argv[3] + " is not a current short word.")

        except IndexError:
            print("Invalid Input: specify the new short wword and the old short word to be replaced.")

    # If the user want to delete a short word
    elif decision == 4:
        try:
            delete_url(sys.argv[2], tree, "../urls.xml")
        except IndexError:
            print("Invalid Input: specify the short word to be deleted.")

    # If the user wants to see a list of all the short words and urls
    elif decision == 5:
        for child in root:
            print(child.get("short") + " : " + child.find("url").text)


if __name__ == "__main__":
    main()
