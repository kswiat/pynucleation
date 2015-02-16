from collections import defaultdict
import random
from PySide import QtCore, QtGui


def custom_hex_color():
    r = lambda: random.randint(0, 255)
    return '#%02X%02X%02X' % (r(), r(), r())


class PointsMixin(object):
    # POINTS.keys() are x-coordinates, POINTS.values() are QPoints lists

    POINTS_NOT_ADDED = 0

    def __init__(self):
        self.POINTS = defaultdict(list)
        self.point_list = []

    def get_point(self, x, y, **kwargs):
        point_list = self.POINTS[x]
        for point in point_list:
            if point.y == y:
                return point

    def get_points(self, points_coordinates):
        for c in points_coordinates:
            yield self.get_point(c[0], c[1])

    def add_point(self, point, **kwargs):
        if point:
            point_list = self.POINTS[point.x]
            if point and self.point_is_legal(point) and point not in point_list:
                point_list.append(point)
                return True
            PointsMixin.POINTS_NOT_ADDED += 1
            return False

    def add_points(self, points):
        for point in points:
            self.add_point(point)

    def point_is_legal(self, point):
        if not (self.width > point.x >= 1 and self.height > point.y >= 1):
            return False
        return True


class Occupier(PointsMixin, QtGui.QGraphicsItem):
    def __init__(self, **kwargs):
        self.playground = kwargs.get('playground', None)
        self.playground.OCCUPIERS.append(self)
        self.color = custom_hex_color()
        self.initialized = False
        self.finished = False
        self.width = self.playground.width
        self.height = self.playground.height
        self.points_ready_to_occupy_list = []
        super(Occupier, self).__init__()

    def add_point(self, point, **kwargs):
        point = self.playground.get_point(point.x, point.y)
        point_added = super(Occupier, self).add_point(point, **kwargs)
        if point_added:
            point.occupier = self

    def point_is_legal(self, point):
        point_is_legal = super(Occupier, self).point_is_legal(point)
        if point_is_legal \
                and (point.occupied and point.occupier != self) \
                or (point.pre_occupied and point.pre_occupier != self):
            return False
        return True

    def get_boundary_points(self):
        points = []
        for point_list in self.POINTS.values():
            for point in point_list:
                if point.is_on_boundary():
                    points.append(point)
        return points

    def points_ready_to_occupy(self):
        points_ready = []
        seen = set()
        for boundary_point in self.get_boundary_points():
            surrounding_points = [self.playground.get_point(c[0], c[1])
                                  for c in boundary_point.surrounding_coordinates]
            random.shuffle(surrounding_points)
            for point in surrounding_points:
                if point and point not in seen and point not in self.POINTS[point.x] and not (point.pre_occupied or point.occupied):
                    point.pre_occupier = self
                    point.pre_occupied = True
                    # yield point
                    points_ready.append(point)
                    seen.add(point)

        if not points_ready:
            self.finished = True
        return points_ready


class PlaygroundPoint(object):
    def __init__(self, x, y, *args):
        super(PlaygroundPoint, self).__init__(*args)
        self._occupied = None
        self._occupier = None
        self._pre_occupied = None
        self._pre_occupier = None
        self._x = x
        self._y = y

    def __repr__(self):
        return u"(%s, %s)" % (self.x, self.y)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

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

    @property
    def pre_occupied(self):
        return self._pre_occupied

    @pre_occupied.setter
    def pre_occupied(self, value):
        self._pre_occupied = value

    @property
    def pre_occupier(self):
        return self._pre_occupier

    @pre_occupier.setter
    def pre_occupier(self, value):
        self._pre_occupier = value

    def is_on_boundary(self):
        """
        Return True if there is at least one surrounding point,
        that is not occupied by self.occupier
        """
        if self.occupied:
            for c in self.surrounding_coordinates:
                point = self.occupier.get_point(c[0], c[1])
                if not point:
                    return True
        return False

    @property
    def surrounding_coordinates(self):
        x = self.x
        y = self.y

        return [(x-1, y+1), (x, y+1), (x+1, y+1),
                (x-1, y),             (x+1, y),
                (x-1, y-1), (x, y-1), (x+1, y-1)]


class Playground(PointsMixin):
    OCCUPIERS = []
    WIDTH = 0
    HEIGHT = 0
    
    def __init__(self, **kwargs):
        super(Playground, self).__init__()
        self.width = kwargs.get('width', 0)
        self.height = kwargs.get('height', 0)
        self.finished_occupiers = 0
        self.fill_playground_with_points()

    def fill_playground_with_points(self):
        for y in range(1, self.height):
            for x in range(1, self.width):
                self.add_point(PlaygroundPoint(x, y))

    @classmethod
    def get_occupiers_number(cls):
        return len(cls.OCCUPIERS)

    def add_point(self, point, **kwargs):
        super(Playground, self).add_point(point, **kwargs)
        self.add_occupier(point.occupier)

    @classmethod
    def add_occupier(cls, occupier):
        if occupier and occupier not in cls.OCCUPIERS:
            cls.OCCUPIERS.append(occupier)

    @classmethod
    def is_done(cls):
        """
        If there is at least one occupier, that is not fished,
        Playground is not done
        """
        if cls.get_occupiers_number():
            for occupier in cls.OCCUPIERS:
                if not occupier.finished:
                    return False
        return True
