class BaseNeighbourhood(object):
    OCCUPIED_FIELDS = []

    def __init__(self, **kwargs):
        self.x = kwargs.get('x', 0)
        self.y = kwargs.get('y', 0)
        self.size = kwargs.get('size', 5)
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

        def points(x, y, size):
            p1 = (x-1*size, y+1*size)
            p2 = (x, y+1*size)
            p3 = (x+1*size, y+1*size)
            p4 = (x+2*size, y+1*size)

            p5 = (x-1*size, y)
            p6 = (x, y)
            p7 = (x+1*size, y)
            p8 = (x+2*size, y)

            p9 = (x-1*size, y-1*size)
            p10 = (x, y-1*size)
            p11 = (x+1*size, y-1*size)
            p12 = (x+2*size, y-1*size)

            p13 = (x-1*size, y-2*size)
            p14 = (x, y-2*size)
            p15 = (x+1*size, y-2*size)
            p16 = (x+2*size, y-2*size)

            top_left = [
                p1, p2, p6, p5
            ]

            top_middle = [
                p2, p3, p7, p6
            ]

            top_right = [
                p3, p4, p7, p8
            ]

            middle_left = [
                p5, p6, p10, p9
            ]

            middle = [
                p6, p7, p11, p10
            ]

            middle_right = [
                p7, p8, p12, p11
            ]

            bottom_left = [
                p9, p10, p14, p13
            ]

            bottom_middle = [
                p10, p11, p15, p14
            ]

            bottom_right = [
                p11, p12, p16, p15
            ]

            return (
                top_left, top_middle, top_right,
                middle_left, middle, middle_right,
                bottom_left, bottom_middle, bottom_right
            )

        points = points(self.x, self.y, self.size)
        for rect, flag in zip(points, self.field_occupy_flags):
            if flag:
                occupied_points.append(rect)
        return occupied_points

    def show_occupy_flags(self):
        for i, flag in enumerate(self.field_occupy_flags, start=1):
            sys.stdout.write('%s' % flag)
            if i % 3 == 0:
                print '\n'

    @staticmethod
    def choose_direction():
        return random.randint(1, 8)
