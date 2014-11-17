#!/usr/bin/env python2
# coding=utf-8
import os
from PySide import QtGui
import sys
from neighbourhood.hexagonal import HexagonalLeft, HexagonalRight
from neighbourhood.moore import Moore
from neighbourhood.pentagonal import PentagonalBottom, PentagonalTop, PentagonalLeft, PentagonalRight
from neighbourhood.von_neumann import VonNeumann

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


def main():
    QtGui.QApplication(sys.argv)


if __name__ == '__main__':
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

    for neighbourhood_class in NEIGHBOURHOOD_CLASSES:
        neighbourhood = neighbourhood_class()







