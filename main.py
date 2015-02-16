#!/usr/bin/env python2
# coding=utf-8
import random
from PySide import QtGui, QtCore
import sys
from PySide.QtCore import QPoint
from neighbourhood.hexagonal import HexagonalLeft, HexagonalRight
from neighbourhood.moore import Moore
from neighbourhood.pentagonal import PentagonalBottom, PentagonalTop, PentagonalLeft, PentagonalRight
from neighbourhood.von_neumann import VonNeumann
from points.points import Playground, Occupier, PlaygroundPoint, custom_hex_color

VON_NEUMANN = 1
MOORE = 2
HEXAGONAL_LEFT = 3
HEXAGONAL_RIGHT = 4
PENTAGONAL_TOP = 5
PENTAGONAL_BOTTOM = 6
PENTAGONAL_RIGHT = 7
PENTAGONAL_LEFT = 8

NEIGHBOURHOODS = {
    VON_NEUMANN: 'Von Neumann',
    MOORE: 'Moore',
    HEXAGONAL_LEFT: 'Hexagonal left',
    HEXAGONAL_RIGHT: 'Hexagonal right',
    PENTAGONAL_TOP: 'Pentagonal top',
    PENTAGONAL_BOTTOM: 'Pentagonal bottom',
    PENTAGONAL_RIGHT: 'Pentagonal right',
    PENTAGONAL_LEFT: 'Pentagonal left',
}

INCLUSION_NONE = 10
INCLUSION_ROUNDED = 11
INCLUSION_RECT = 12


INCLUSIONS = {
    INCLUSION_NONE: 'None',
    INCLUSION_RECT: 'Rectangle',
    INCLUSION_ROUNDED: 'Rounded',
}

NEIGHBOURHOOD_CLASSES = (
    VonNeumann,
    Moore,
    HexagonalLeft,
    HexagonalRight,
    PentagonalBottom,
    PentagonalTop,
    PentagonalLeft,
    PentagonalRight,
)


class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.height = 500
        self.width = 1000
        self.view = View(self)
        self.view.setRenderHints(QtGui.QPainter.Antialiasing | QtGui.QPainter.SmoothPixmapTransform)
        self.main_layout = QtGui.QHBoxLayout()
        self.grains_number = 1

        self.controls_container_widget = QtGui.QWidget(self)
        self.controls_container_widget.setFixedWidth(self.width/5.0)
        self.controls_container_widget.setFixedHeight(400)
        self.controls_container_layout = QtGui.QVBoxLayout()
        self.controls_container_widget.setLayout(self.controls_container_layout)
        self.start_button = QtGui.QPushButton("Start")
        self.clear_view_button = QtGui.QPushButton("Clear")

        self.inclusion_combo_label = QtGui.QLabel("Inclusion")
        self.inclusion_combo = QtGui.QComboBox()
        self.inclusion_combo.addItems(INCLUSIONS.values())

        self.neighbourhood_combo = QtGui.QComboBox()
        self.neighbourhood_combo.addItems(NEIGHBOURHOODS.values())

        self.neighbourhood_combo_label = QtGui.QLabel("Neighbourhood")

        self.controls_container_layout.addWidget(self.start_button)
        self.controls_container_layout.addWidget(self.clear_view_button)
        self.controls_container_layout.addWidget(self.inclusion_combo_label)
        self.controls_container_layout.addWidget(self.inclusion_combo)
        self.controls_container_layout.addWidget(self.neighbourhood_combo_label)
        self.controls_container_layout.addWidget(self.neighbourhood_combo)

        self.grains_number_container_layout = QtGui.QHBoxLayout()
        self.grains_number_spin_label = QtGui.QLabel("Grains number")
        self.grains_number_spin = QtGui.QSpinBox()
        self.grains_number_spin.setMinimum(1)
        self.grains_number_spin.setMaximum(20)
        self.grains_number_container_layout.addWidget(self.grains_number_spin_label)
        self.grains_number_container_layout.addWidget(self.grains_number_spin)

        self.controls_container_layout.addLayout(self.grains_number_container_layout)

        self.animation_controls_layout = QtGui.QVBoxLayout()
        self.speed_slider_label = QtGui.QLabel("Animation speed")

        self.speed_slider = QtGui.QSlider()
        self.speed_slider.setMinimum(0)
        self.speed_slider.setMaximum(200)
        # self.speed_slider.setSingleStep(1)
        self.speed_slider.setProperty("value", 100)
        self.speed_slider.setInvertedControls(True)
        self.speed_slider.setOrientation(QtCore.Qt.Horizontal)

        self.animation_controls_layout.addWidget(self.speed_slider_label)
        self.animation_controls_layout.addWidget(self.speed_slider)

        self.controls_container_layout.addLayout(self.animation_controls_layout)

        self.main_layout.addWidget(self.controls_container_widget)
        self.main_layout.addWidget(self.view)

        self.clear_view_button.clicked.connect(self.clear_view_handler)
        self.start_button.clicked.connect(self.start_button_handler)
        # self.inclusion_combo.textChanged.connect(self.inclusion_change_handler)
        # self.neighbourhood_combo.textChanged.connect(self.neighbourhood_handler)
        self.grains_number_spin.valueChanged.connect(self.grains_number_handler)
        self.speed_slider.valueChanged.connect(self.speed_change_handler)
        self.setLayout(self.main_layout)

        self.animation_stopped = True
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.timerEvent)
        self.default_timer_interval = 200.1
        self.timer.setInterval(self.default_timer_interval)
        # self.timer.start(100)


    def disable_widgets(self):
        self.start_button.setEnabled(False)

    def start_button_handler(self):
        if self.animation_stopped:
            self.timer.start()
            self.start_button.setText("Pause")
            self.animation_stopped = False
        else:
            self.timer.stop()
            self.start_button.setText("Start")
            self.animation_stopped = True


    def speed_change_handler(self, value):

        self.timer.setInterval(self.default_timer_interval - value)

    def clear_view_handler(self):
        self.view.scene().clear()

    def grains_number_handler(self, value):
        self.grains_number = value

    def timerEvent(self, *args, **kwargs):
        scene = self.view.scene()
        for i in range(self.grains_number):
            points = []
            for j in range(3):

                x1 = random.randint(-self.width/2, self.width/2)
                y1 = random.randint(-self.height/2, self.height/2)
                point = QPoint(x1, y1)
                # point.setPen(QtGui.QColor(custom_hex_color()))
                points.append(point)

                # x2 = random.randint(-self.width/2, self.width/2)
                # y2 = random.randint(-self.height/2, self.height/2)

            polygon = QtGui.QGraphicsPolygonItem(points)



            # if x == 11:
            #     print 'x==11\n'
            #     if y==123:
            #         print '!!!!!!!!!!!!!!!1!!11'
            # line = QtGui.QGraphicsLineItem(x1, y1, x2, y2)
            # ellipse = QtGui.QGraphicsEllipseItem(QtCore.QRectF(x, y, 100, 100))
            # ellipse.setPen(QtGui.QColor(custom_hex_color()))
            # line.setPen(QtGui.QColor(custom_hex_color()))
            polygon.setBrush(QtGui.QBrush(QtGui.QColor(custom_hex_color())))
            polygon.setPen(QtGui.QPen(QtGui.QColor(custom_hex_color()), 5))
            scene.addItem(polygon)

            # scene.addItems(points)


class View(QtGui.QGraphicsView):
    def __init__(self, parent):
        QtGui.QGraphicsView.__init__(self, parent)
        self.setScene(QtGui.QGraphicsScene(self))
        self.setSceneRect(QtCore.QRectF(self.viewport().rect()))


    def mousePressEvent(self, event):
        self._start = self.mapToScene(event.pos())
        x = self._start.x()
        y = self._start.y()
        text = QtGui.QGraphicsSimpleTextItem("AJ")
        text.setPen(QtGui.QColor(custom_hex_color()))
        text.setPos(self._start)
        ellipse = QtGui.QGraphicsEllipseItem(QtCore.QRectF(x, y, 100, 100))
        # self.scene().addItem(
        #     ellipse,
        # )
        self.scene().addItem(
            text
        )

    # def mouseReleaseEvent(self, event):
    #     start = QtCore.QPointF(self._start)
    #     # start = QtCore.QPointF('12')
    #     end = QtCore.QPointF(self.mapToScene(event.pos()))
    #     self.scene().addItem(
    #         QtGui.QGraphicsLineItem(QtCore.QLineF(start, end)))
    #     for point in (start, end):
    #         text = self.scene().addSimpleText(
    #             '(%d, %d)' % (point.x(), point.y()))
    #         text.setBrush(QtCore.Qt.red)
    #         text.setPos(point)



if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.resize(window.width, window.height)
    window.show()
    sys.exit(app.exec_())