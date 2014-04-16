from wtforms import form


class DataWrapper(dict):

    def __init__(self, handler):
        super(DataWrapper, self).__init__(handler.request.arguments)
        self.getlist = handler.get_arguments
        self.get = handler.get_argument

    def __getitem__(self, name):
        result = super(DataWrapper, self).__getitem__(name)
        if len(result) > 0:
            result = result[-1]
        return result


class Form(form.Form):

    def __init__(self, handler=None, **kwargs):
        if not handler is None:
            kwargs['formdata'] = DataWrapper(handler)
        super(Form, self).__init__(**kwargs)
