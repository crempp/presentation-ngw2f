# Part I

Basic Nginx example.

## Run

```
$ export SECTION=/Users/crempp/projects/presentation-ngw2f/part-I-nginx
$ nginx -c $SECTION/nginx/config/nginx.conf
$ nginx -s stop
```

Go to: http://127.0.0.1:8080/

or

```
$ telnet localhost 8080
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
GET / HTTP/1.0
```