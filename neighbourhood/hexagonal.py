from .neighbourhoods import BaseNeighbourhood


class BaseHexagonal(BaseNeighbourhood):
    def __init__(self, **kwargs):
        super(BaseHexagonal, self).__init__(**kwargs)


class HexagonalLeft(BaseHexagonal):
    def __init__(self, **kwargs):
        self.field_occupy_flags = (0, 1, 1,
                                   1, 1, 1,
                                   1, 1, 0)
        super(HexagonalLeft, self).__init__(**kwargs)


class HexagonalRight(BaseHexagonal):
    def __init__(self, **kwargs):
        self.field_occupy_flags = (1, 1, 0,
                                   1, 1, 1,
                                   0, 1, 1)
        super(HexagonalRight, self).__init__(**kwargs)
