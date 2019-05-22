import requests

def check_response():
    """

    :return:
    """
    return requests.get('https://www.google.by').status_code
