from tornado import web
from tornado_ext.auth.decorators import provide_user


class RequestHandler(web.RequestHandler):
    
    @provide_user
    def prepare(self):
        pass
