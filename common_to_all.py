import json
import requests
import model_api


def request(method, url, header_auth=None, **kwargs):
    mess = method
    r = requests.request(method, url, headers=header_auth, **kwargs)
    check_result(r, mess, url)
    return r


def check_result(r, mess, url):
    try:
        if r.status_code == 200:
            print(mess, url, '| status code:', r.status_code)
            json.dumps(r.json(), indent=4)
        elif r.status_code != 200:
            print(r.text)
            print(r.request)
            for err_key in model_api.err_mess:
                if err_key == str(r.status_code):
                    print(mess, url, '/////', model_api.err_mess[err_key])
    except ValueError:
        print('Decoding JSON has failed')

