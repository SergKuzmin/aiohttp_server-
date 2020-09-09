import requests
import os
API_URL = 'http://{}:{}/api'.format('192.168.0.150', '8463')


def send_massage(file_paths):
    files = {}
    for i, f in enumerate(file_paths):
        files['file{}'.format(i)] = open(f, 'rb')

    rp = requests.post('{}/{}'.format(API_URL, 'convert'), files=files)
    return rp


if __name__ == '__main__':
    input_path = '/Users/sergejkuzminyh/Desktop/GitHubProjects/aiohttp_server/aiohttp_server-/src/module_class/input/'
    file_name = 'rose-blue-flower-rose-blooms-67636.jpeg'
    file_name = os.path.join(input_path, file_name)
    paths = [file_name]
    rp = send_massage(file_paths=paths)
    print(rp.content)