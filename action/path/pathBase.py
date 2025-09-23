import webbrowser

class PathBase:
    def __init__(self, path, url):
        self.path = path
        self.url = url
    
    def run(self):
        webbrowser.open(self.url)