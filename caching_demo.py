
from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/")
@app.route("/query", methods=['GET', 'POST'])
def query_key():
    if request.method == 'POST':
        return fetch_data(request.form['fname'])
    return '<!doctype html><title>Search for Data</title><form action="/query" method=post ' \
           'enctype=multipart/form-data><p><label for="key">Key:</label><input type="text" id="key" ' \
           'name="fname"><br><br><input type=submit value="Get Value"></form> '


@app.route("/getdata/<data>", methods=['GET', 'POST'])
def get_data_with_key(data):
    if request.method == 'GET':
        return fetch_data(data)


def fetch_data(data):
    # Let's try to read the file locally first
    file_from_cache = fetch_from_cache(data)

    if file_from_cache:
        print('Fetched successfully from cache.')
        return file_from_cache
    else:
        print('Not in cache. Fetching from server.')
        file_from_server = fetch_from_server(data)

        if file_from_server:
            save_in_cache(data, file_from_server)
            return file_from_server
        else:
            return None


def fetch_from_cache(data):
    try:
        # Check if we have this data locally
        fin = open('cache' + data)
        content = fin.read()
        fin.close()
        # If we have it, let's send it
        return content
    except IOError:
        return None


def fetch_from_server(data):
    url = 'http://127.0.0.1:5000/getdata/' + data
    try:
        req = requests.post(url, verify=False)
        return req
    except requests.HTTPError:
        return None


def save_in_cache(data, content):
    print('Saving a copy of {} in the cache'.format(data))
    cached_file = open('cache' + data, 'w')
    cached_file.write(content)
    cached_file.close()


if __name__ == "__main__":
    app.run()
