from collections import defaultdict
from PySide.QtCore import QPoint


class PointsMixin(object):
    # POINTS.keys() are x-coordinates, POINTS.values() are QPoints lists

    def __init__(self):
        self.POINTS = defaultdict(list)

    def get_point(self, x, y):
        point_list = self.POINTS[x]
        for point in point_list:
            if point.y() == y:
                return point

    def add_point(self, point):
        x = point.x()
        point_list = self.POINTS[x]
        if point not in point_list:
            point_list.append(point)


class Occupier(PointsMixin):
    def add_point(self, point):
        super(Occupier, self).add_point(point)
        point.occupier = self
        

class PlaygroundPoint(QPoint):
    def __init__(self, *args):
        super(PlaygroundPoint, self).__init__(*args)
        self._occupier = None
        self.occupied = None

    @property
    def occupied(self):
        return self._occupied

    @occupied.setter
    def occupied(self, value):
        self._occupied = value

    @property
    def occupier(self):
        return self._occupier

    @occupier.setter
    def occupier(self, value):
        self.occupied = True
        self._occupier = value


class Playground(PointsMixin):
    OCCUPIERS = []

    @classmethod
    def occupiers_number(cls):
        return len(cls.OCCUPIERS)

    def add_point(self, point):
        super(Playground, self).add_point(point)
        self.add_occupier(point.occupier)

    @classmethod
    def add_occupier(cls, occupier):
        if occupier and occupier not in cls.OCCUPIERS:
            cls.OCCUPIERS.append(occupier)

