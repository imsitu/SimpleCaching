# SimpleCaching

This is a Flask app to demonstrate simple casching mechanism.

the caching mechanism being :

1. Client requests item
2. Cache server checks if it’s stored in the cache
3. The item is not found
4. The cache server requests the item from the main server
5. The main server sends the item back
6. The cache server saves a copy of the item
7. The cache server sends the client the item

I Didn’t have the time to configure a databse with which I could have written CRUD operations.



Log :

/Users/situ/PycharmProjects/caching/venv/bin/python /Users/714061/PycharmProjects/caching/test.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Serving Flask app "test" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
127.0.0.1 - - [04/Sep/2020 16:09:57] "POST /query HTTP/1.1" 200 -
Fetched successfully from cache.
127.0.0.1 - - [04/Sep/2020 16:10:05] "GET / HTTP/1.1" 200 -
Not in cache. Fetching from server.
Saving a copy of dthdf in the cache
