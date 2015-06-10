# Part III WSGI

Basic WSGI example.

## Run

Start Nginx

```
$ cd part-III-wsgi
$ export SECTION=/Users/crempp/projects/presentation-ngw2f/part-III-wsgi
$ nginx -c $SECTION/nginx/config/nginx.conf
```

Start the WSGI server

```
$ cd wsgi
$ python app.py
```

## Demo

```
$ telnet localhost 8080
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
GET / HTTP/1.0
```

## Clean up

```
$ nginx -s stop
```