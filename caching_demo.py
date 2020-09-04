
from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/")
@app.route("/query", methods=['GET', 'POST'])
def query_key():
    if request.method == 'POST':
        fetch_data(request.form['fname'])
        return request.form['fname']
    return '<!doctype html><title>Search for Data</title><form action="/query" method=post ' \
           'enctype=multipart/form-data><p><label for="key">Key:</label><input type="text" id="key" ' \
           'name="fname"><br><br><input type=submit value="Get Value"></form> '


@app.route("/getdata/<key>", methods=['GET', 'POST'])
def get_data_with_key(key):
    if request.method == 'GET':
        return fetch_data(key)


def fetch_data(key):
    # Let's try to read the file locally first
    file_from_cache = fetch_from_cache(key)

    if file_from_cache:
        print('Fetched successfully from cache.')
        return file_from_cache
    else:
        print('Not in cache. Fetching from server.')
        file_from_server = fetch_from_server(key)

        if file_from_server:
            save_in_cache(key, file_from_server)
            return file_from_server
        else:
            return None


def fetch_from_cache(key):
    try:
        # Check if we have this data locally
        fin = open('cache' + key)
        content = fin.read()
        fin.close()
        # If we have it, let's send it
        return content
    except IOError:
        return None


def fetch_from_server(key):
    url = 'http://127.0.0.1:5000/getdata/' + key
    try:
        req = requests.post(url, verify=False)
        return req.content
    except requests.HTTPError:
        return None


def save_in_cache(key, content):
    print('Saving a copy of {} in the cache'.format(key))
    cached_file = open('cache' + key, 'w')
    cached_file.write( "".join(map(chr,content)))
    cached_file.close()


if __name__ == "__main__":
    app.run(debug=True)
