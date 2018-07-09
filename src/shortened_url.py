

def is_shortened_url(shortened_url, xml_root):
    """
    Checks that the requested shortened url exists. CURRENTLY USING PLACEHOLDER VALUE.
    :param shortened_url: A string to check for if its a valid shortened url.
    :return: boolean value for if the shortened url is valid.
    """
    for child in xml_root:
        if child.get("short") == shortened_url:
            return True
    return False


def get_url(shortened_url, xml_root):
    for child in xml_root:
        if child.get("short") == shortened_url:
            return child.find("url").text
