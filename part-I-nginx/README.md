# Part I

Basic Nginx example.

## Run

```
$ cd part-I-nginx/
$ export SECTION=/Users/crempp/projects/presentation-ngw2f/part-I-nginx
$ nginx -c $SECTION/nginx/config/nginx.conf
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
