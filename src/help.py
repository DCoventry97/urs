
def get_help_message():
    """
    Prints a help message.
    """
    print("This program allows the user to store a word which relates to a url and open the url by entering "
          "the shortened word.")
    print("Arguments:")
    print("[short word] : opens a web browser on the web page associated with the short word")

    print("[-d | --delete] [short word] : deletes a short word and its associated url")
    print("[-h | --help | help] : displays help for this program")
    print("[-r | --rename] [new short word] [old short word]: renames a short word to a new short word")
    print("[-n | --new] [short word] [url] : sets a new short word to be associated with a new url")
    print("[-v | --view-all-urls] : view all short words and their associated url's")

