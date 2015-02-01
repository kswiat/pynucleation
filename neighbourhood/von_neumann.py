from .neighbourhoods import BaseNeighbourhood


class VonNeumann(BaseNeighbourhood):
    def __init__(self, **kwargs):
        self.field_occupy_flags = (0, 1, 0,
                                   1, 1, 1,
                                   0, 1, 0)
        self.color = '#00ff00'
        super(VonNeumann, self).__init__(**kwargs)
