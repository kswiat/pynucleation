from .neighbourhoods import BaseNeighbourhood


class BasePentagonal(BaseNeighbourhood):
    def __init__(self, **kwargs):
        super(BasePentagonal, self).__init__(**kwargs)


class PentagonalBottom(BaseNeighbourhood):
    def __init__(self, **kwargs):
        super(PentagonalBottom, self).__init__(**kwargs)
        self.field_occupy_flags = ((1, 1, 1),
                                   (1, 1, 1),
                                   (1, 0, 1))


class PentagonalTop(BaseNeighbourhood):
    def __init__(self, **kwargs):
        super(PentagonalTop, self).__init__(**kwargs)
        self.field_occupy_flags = ((1, 0, 1),
                                   (1, 1, 1),
                                   (1, 1, 1))


class PentagonalLeft(BaseNeighbourhood):
    def __init__(self, **kwargs):
        super(PentagonalLeft, self).__init__(**kwargs)
        self.field_occupy_flags = ((1, 1, 1),
                                   (0, 1, 1),
                                   (1, 1, 1))


class PentagonalRight(BaseNeighbourhood):
    def __init__(self, **kwargs):
        super(PentagonalRight, self).__init__(**kwargs)
        self.field_occupy_flags = ((1, 1, 1),
                                   (1, 1, 0),
                                   (1, 1, 1))
