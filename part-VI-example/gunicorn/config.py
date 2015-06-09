import pprint

def on_starting(server):
    print("on_starting")

def on_reload(server):
    print("on_reload")

def when_ready(server):
    print("when_ready")

def pre_fork(server, worker):
    print("pre_fork")

def post_fork(server, worker):
    print("post_fork")

def post_worker_init(worker):
    print("post_worker_init")

def worker_init(worker):
    print("worker_init")

def worker_abort(worker):
    print("worker_abort")

def pre_exec(server):
    print("pre_exec")

def pre_request(worker, req):
    print("pre_request")
    pprint.pprint(req.parse(req.unreader))

def post_request(worker, req, environ, resp):
    print("post_request")

def worker_exit(server, worker):
    print("worker_exit")

def nworkers_changed(server, new_value, old_value):
    print("nworkers_changed")

def on_exit(server):
    print("on_exit")