import re

def search_path(data):

    key = re.search(r"(/.*?)\s", data).group(1)
    print(repr(key))
    if key == "/":
        path = "./index.html"
        state = "200 OK"
    elif key == "/index.html":
        path = "./index.html"
        state = "200 OK"
    elif key == "aa.html":
        path = None
        state = "404 NOT FOUND"
    else:
        path = None
        state = "404 NOT FOUND"
    return path, state