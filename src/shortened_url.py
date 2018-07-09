

def is_shortened_url(shortened_url, xml_root):
    """
    Checks that the requested shortened url exists.
    :param shortened_url: A string to check for if its a valid shortened url.
    :return: boolean value for if the shortened url is valid.
    """
    for child in xml_root:
        if child.get("short") == shortened_url:
            return True
    return False


def get_url(shortened_url, xml_root):
    """
    Gets the url associated with a shortened url.
    :param shortened_url: The shortened url that is associated with a url.
    :param xml_root: The root of the xml that the url data is storied in
    :return: The url that is associated with the shortened url.
    """
    for child in xml_root:
        if child.get("short") == shortened_url:
            return child.find("url").text


def check_new_url(user_input):
    invlaid_short_words = ["-n", "new", "help", "-h", "--help", "r", "--rename", "-d", "--delete"]
    for word in invlaid_short_words:
        if word == user_input[2]:
            return False

    return True

