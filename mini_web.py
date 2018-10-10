def logic(path):
    state = "200 OK"
    if path == "/":
        open_path = "/index.html"
    elif path == "/control.html":
        open_path = "/control_html"
    elif path == "/1.html":
        open_path = "1.html"
    else:
        state = "404 NOTFONUD"
        return '1', state
    return open_path, state
