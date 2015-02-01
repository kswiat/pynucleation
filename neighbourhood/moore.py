from .neighbourhoods import BaseNeighbourhood


class Moore(BaseNeighbourhood):
    def __init__(self, **kwargs):
        self.field_occupy_flags = (1, 1, 1,
                                   1, 1, 1,
                                   1, 1, 1)
        self.color = '#ff0000'
        super(Moore, self).__init__(**kwargs)
