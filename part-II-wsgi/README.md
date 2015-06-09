# Part II Gunicorn

Basic Gunicorn example.

## Run

Start the WSGI server

```
$ cd wsgi
$ python app.py
```

In a new window start nginx

```
$ export SECTION=/Users/crempp/projects/presentation-ngw2f/part-II-wsgi
$ nginx -c $SECTION/nginx/config/nginx.conf
$ nginx -s stop
```

Go to WSGI directly: http://127.0.0.1:8000/

Go to WSGI through Nginx: http://127.0.0.1:8080/

or

```
$ telnet localhost 8080
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
GET / HTTP/1.0
```