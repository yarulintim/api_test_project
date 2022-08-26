import requests


class BaseRequest(object):

    def __init__(self, url=None, data=None, headers=None, params=None, token_b=None, files=None):

        self.url = url
        self.data = data
        self.files = files
        self.token = token_b
        self.headers = headers
        self.params = params

        if headers:
             headers.update(self.headers or {})
             self.headers = headers
        if params:
              params.update(self.params or {})
              self.params = params

    def process_get(self):
        r = requests.get(url=self.url, data=self.data, headers=self.headers, params=self.params)
        return r

    def process_post(self):
        r = requests.post(url=self.url, data=self.data, headers=self.headers, params=self.params)
        return r

    def process_delete(self):
        r = requests.delete(url=self.url, data=self.data, headers=self.headers, params=self.params)
        return r

    def file_post(self):
        r = requests.post(url=self.url,  data=self.data, headers=self.headers, params=self.params, files=self.files)
        return r

    def process_put(self):
        r = requests.put(url=self.url, data=self.data, headers=self.headers, params=self.params)
        return r
