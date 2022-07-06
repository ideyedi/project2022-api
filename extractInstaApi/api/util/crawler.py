
import requests


class InstaCrawler:
    def __init__(self, url):
        super().__init__(url)
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        }
        self.session = requests.Session()
        self.session.headers = self.headers

    def get_html(self):
        response = self.session.get(self.url)
        return response.text

    def get_json(self):
        response = self.session.get(self.url)
        return response.json()

    def get_text(self):
        response = self.session.get(self.url)
        return response.text

    def get_status_code(self):
        response = self.session.get(self.url)
        return response.status_code

    def get_headers(self):
        response = self.session.get(self.url)
        return response.headers

    def get_cookies(self):
        response = self.session.get(self.url)
        return response.cookies

    def get_history(self):
        response = self.session.get(self.url)
        return response.history

    def get_encoding(self):
        response = self.session.get(self.url)
        return response.encoding

    def get_content(self):
        response = self.session.get(self.url)
        return response.content

    def get_raw_headers(self):
        response = self.session.get(self.url)
        return response.raw.headers

    def get_raw_content(self):
        response = self.session.get(self.url)
        return response.raw.read()

    def get_raw_text(self):
        response = self.session.get(self.url)
        return response.raw.read().decode('utf-8')
