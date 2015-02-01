from .neighbourhoods import BaseNeighbourhood


class BasePentagonal(BaseNeighbourhood):
    def __init__(self, **kwargs):
        super(BasePentagonal, self).__init__(**kwargs)


class PentagonalBottom(BaseNeighbourhood):
    def __init__(self, **kwargs):
        self.field_occupy_flags = (1, 1, 1,
                                   1, 1, 1,
                                   1, 0, 1)
        self.color = '#0000ff'
        super(PentagonalBottom, self).__init__(**kwargs)


class PentagonalTop(BaseNeighbourhood):
    def __init__(self, **kwargs):
        self.field_occupy_flags = (1, 0, 1,
                                   1, 1, 1,
                                   1, 1, 1)
        super(PentagonalTop, self).__init__(**kwargs)


class PentagonalLeft(BaseNeighbourhood):
    def __init__(self, **kwargs):
        self.field_occupy_flags = (1, 1, 1,
                                   0, 1, 1,
                                   1, 1, 1)
        super(PentagonalLeft, self).__init__(**kwargs)


class PentagonalRight(BaseNeighbourhood):
    def __init__(self, **kwargs):
        self.field_occupy_flags = (1, 1, 1,
                                   1, 1, 0,
                                   1, 1, 1)
        super(PentagonalRight, self).__init__(**kwargs)
