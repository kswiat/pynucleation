#will inherit from QT widget
class BaseField(object):
    def __init__(self, **kwargs):
        self.x = kwargs.get('x')
        self.y = kwargs.get('y')
        self.occupied = False


class Field(BaseField):
    pass


class NeighbourhoodField(object):
    def __init__(self, **kwargs):
        self.occupied = True


#will inherit from QT widget
class FieldSet(object):
    def __init__(self, **kwargs):
        self.cols_number = kwargs.get('cols_number')
        self.rows_number = kwargs.get('rows_number')
        self.fields = []
        self.init_fields()

    def init_fields(self):
        for i in range(self.cols_number):
            for j in range(self.rows_number):
                self.fields.append(Field(x=i, y=j))
