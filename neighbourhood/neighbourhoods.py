# coding=utf-8
import random
import sys
from PySide.QtCore import QPoint


class BaseNeighbourhood(object):
    OCCUPIED_FIELDS = []

    def __init__(self, **kwargs):
        self.x = kwargs.get('x', 0)
        self.y = kwargs.get('y', 0)
        self.points = self.get_occupied_points()
        self.color = kwargs.get('color', '#ff0000')
        self.occupied_fields = []


    # def paintEvent(self, event, *args, **kwargs):
    #     qp = QtGui.QPainter()
    #     qp.begin(self)
    #     if not self.occupied_fields:
    #         self.draw_neighbourhood(qp)
    #     qp.end()

    # def draw_neighbourhood(self, qp):
    #     qp.setPen(QtGui.QColor(168, 34, 3))
    #     for field_row in self.fields:
    #         for field in field_row:
    #             if field.occupied:
    #                 qp.drawPoint(field.x, field.y)
    #                 self.occupied_fields.append(field)

    def get_occupied_points(self):
        occupied_points = []
        points = (
            QPoint(self.x - 1, self.y + 1), QPoint(self.x, self.y + 1), QPoint(self.x + 1, self.y + 1),
            QPoint(self.x - 1, self.y), QPoint(self.x, self.y), QPoint(self.x + 1, self.y),
            QPoint(self.x - 1, self.y - 1), QPoint(self.x, self.y - 1), QPoint(self.x + 1, self.y - 1),
        )
        for point, flag in zip(points, self.field_occupy_flags):
            if flag:
                occupied_points.append(point)
        return occupied_points

    def show_occupy_flags(self):
        for i, flag in enumerate(self.field_occupy_flags, start=1):
            sys.stdout.write('%s' % flag)
            if i % 3 == 0:
                print '\n'

    @staticmethod
    def choose_direction():
        return random.randint(1, 8)
