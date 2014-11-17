# coding=utf-8
import random
from field.fields import FieldSet, NeighbourhoodField


class BaseNeighbourhood(object):
    def __init__(self, **kwargs):
        self.field_neighbourhood_settings = kwargs.get('field_neighbourhood_settings')
        self.fieldset = FieldSet()
        x = kwargs.get('center_x', 0)
        y = kwargs.get('center_y', 0)
        field = NeighbourhoodField
        self.field_occupy_flags = ()
        self.parent = None

        self.fields = (
            (field(x=x-1, y=y+1), field(x=x, y=y+1), field(x=x+1, y=y+1)),
            (field(x=x-1, y=y),   field(x=x, y=y),   field(x=x+1, y=y)),
            (field(x=x-1, y=y-1), field(x=x, y=y-1), field(x=x+1, y=y-1))
        )
        self.set_field_occupy_flags()

    def set_field_occupy_flags(self):
        for field_row, flag_row in zip(self.fields, self.field_occupy_flags):
            for field, flag in zip(field_row, flag_row):
                field.occupied = flag

    def show_field_occupy_flags(self):
        for field_row in self.fields:
            for field in field_row:
                print "%s" % field.occupied
            print "\n"

    @staticmethod
    def choose_direction():
        return random.randint(1, 8)
