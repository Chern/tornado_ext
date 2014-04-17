import functools
from bson.objectid import ObjectId
from tornado import gen


def provide_user(func):
    @functools.wraps(func)
    @gen.coroutine
    def wrapper(self, *args, **kwargs):
        db = self.settings['db']
        sessionid = self.get_secure_cookie('sessionid')
        if sessionid:
            session = yield db.sessions.find_one({'_id': ObjectId(sessionid)})
            if session:
                user = yield db.users.find_one({'username': session['username']})
                if user:
                    self.current_user = user
        result = func(self, *args, **kwargs)
        if result:
            yield result
    return wrapper
