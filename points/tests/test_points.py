import unittest
from points.points import Playground, Occupier




# (0, 0)(1, 0)(2, 0)(3, 0)(4, 0)(5, 0)(6, 0)(7, 0)(8, 0)(9, 0)
#
# (0, 1)(1, 1)(2, 1)(3, 1)(4, 1)(5, 1)(6, 1)(7, 1)(8, 1)(9, 1)
#
# (0, 2)(1, 2)(2, 2)(3, 2)(4, 2)(5, 2)(6, 2)(7, 2)(8, 2)(9, 2)
#
# (0, 3)(1, 3)(2, 3)(3, 3)(4, 3)(5, 3)(6, 3)(7, 3)(8, 3)(9, 3)
#
# (0, 4)(1, 4)(2, 4)(3, 4)(4, 4)(5, 4)(6, 4)(7, 4)(8, 4)(9, 4)
#
# (0, 5)(1, 5)(2, 5)(3, 5)(4, 5)(5, 5)(6, 5)(7, 5)(8, 5)(9, 5)
#
# (0, 6)(1, 6)(2, 6)(3, 6)(4, 6)(5, 6)(6, 6)(7, 6)(8, 6)(9, 6)
#
# (0, 7)(1, 7)(2, 7)(3, 7)(4, 7)(5, 7)(6, 7)(7, 7)(8, 7)(9, 7)
#
# (0, 8)(1, 8)(2, 8)(3, 8)(4, 8)(5, 8)(6, 8)(7, 8)(8, 8)(9, 8)
#
# (0, 9)(1, 9)(2, 9)(3, 9)(4, 9)(5, 9)(6, 9)(7, 9)(8, 9)(9, 9)









class TestPoint(unittest.TestCase):
    def setUp(self):
        width = 10
        height = 10
        self.playground = Playground(width=width, height=height)
        self.occupier1 = Occupier(playground=self.playground)
        self.occupier2 = Occupier(playground=self.playground)

    def test_point_is_not_on_boundary(self):
        point_inside = self.playground.get_point(5, 4)
        self.occupier1.add_point(point_inside)
        surrounding_points_coordinates = [
            (4, 5), (5, 5), (6, 5),
            (4, 4),         (6, 4),
            (4, 3), (5, 3), (6, 3)
        ]
        for c in surrounding_points_coordinates:
            self.occupier1.add_point(self.playground.get_point(c[0], c[1]))

        self.assertFalse(point_inside.is_on_boundary())

    def test_point_is_on_boundary(self):
        point_outside = self.playground.get_point(4, 5)
        self.occupier1.add_point(point_outside)
        surrounding_points_coordinates = [
                    (5, 5), (6, 5),
            (4, 4), (5, 4), (6, 4),
            (4, 3), (5, 3), (6, 3)
        ]
        for c in surrounding_points_coordinates:
            self.occupier1.add_point(self.playground.get_point(c[0], c[1]))

        self.assertTrue(point_outside.is_on_boundary())

    def test_occupy(self):
        point = self.playground.get_point(9, 3)
        self.assertFalse(point.occupied)
        self.assertIsNone(point.occupier)
        self.occupier1.add_point(point)
        self.assertTrue(point.occupied)
        self.assertEqual(point.occupier, self.occupier1)


class TestOccupiers(unittest.TestCase):
    def setUp(self):
        width = 10
        height = 10

        self.playground = Playground(width=width, height=height)
        self.occupier1 = Occupier(playground=self.playground)

    def test_get_boundary_point(self):
        points_coordinates = [
            (4, 5), (5, 5), (6, 5),
            (4, 4), (5, 4), (6, 4),
            (4, 3), (5, 3), (6, 3)
        ]
        for c in points_coordinates:
            self.occupier1.add_point(self.playground.get_point(c[0], c[1]))

        expected_boundaries_coordinates = [
            (4, 5), (5, 5), (6, 5),
            (4, 4),         (6, 4),
            (4, 3), (5, 3), (6, 3)
        ]
        expected_boundaries = [self.playground.get_point(c[0], c[1]) for c in expected_boundaries_coordinates]
        real_boundaries = [p for p in self.occupier1.get_boundary_points()]

        self.assertEqual(len(expected_boundaries), len(real_boundaries))

        for point in real_boundaries:
            self.assertIn(point, expected_boundaries)

    def test_get_boundary_point_with_points_out_of_scope(self):
        """
        perspective = [
            (0, 1), (1, 1), (2, 1), (3, 1)
            (0, 2), (1, 2), (2, 2), (3, 2)
            (0, 3), (1, 3), (2, 3), (3, 3)
        ]
        """
        self.occupier1.add_point(self.playground.get_point(0, 1))
        self.occupier1.add_point(self.playground.get_point(0, 2))
        self.occupier1.add_point(self.playground.get_point(0, 3))
        self.occupier1.add_point(self.playground.get_point(1, 1))
        self.occupier1.add_point(self.playground.get_point(1, 2))
        self.occupier1.add_point(self.playground.get_point(1, 3))
        self.occupier1.add_point(self.playground.get_point(2, 1))
        self.occupier1.add_point(self.playground.get_point(2, 2))
        self.occupier1.add_point(self.playground.get_point(2, 3))
        self.occupier1.add_point(self.playground.get_point(3, 1))
        self.occupier1.add_point(self.playground.get_point(3, 2))
        self.occupier1.add_point(self.playground.get_point(3, 3))

        expected_coordinates = [
            (1, 1), (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (3, 3)
        ]

        expected_boundaries = [self.playground.get_point(c[0], c[1]) for c in expected_coordinates]

        real_boundaries = [p for p in self.occupier1.get_boundary_points()]

        self.assertEqual(len(expected_boundaries), len(real_boundaries))

        for point in real_boundaries:
            self.assertIn(point, expected_boundaries)

    def test_points_ready_to_occupy(self):
        """
        perspective = [
            (0, 1),  (1, 1),  (2, 1),  (3, 1), (4, 1)
            (0, 2),  (1, 2), x(2, 2),  (3, 2), (4, 2)
            (0, 3), x(1, 3), x(2, 3), x(3, 3), (4, 3)
            (0, 4),  (1, 4), x(2, 4),  (3, 4), (4, 4)
            (0, 5),  (1, 5),  (2, 5),  (3, 5), (4, 5)
        ]
        """
        self.occupier1.add_point(self.playground.get_point(1, 3))
        self.occupier1.add_point(self.playground.get_point(2, 2))
        self.occupier1.add_point(self.playground.get_point(2, 3))
        self.occupier1.add_point(self.playground.get_point(2, 4))
        self.occupier1.add_point(self.playground.get_point(3, 3))

        points_ready_to_occupy_coordinates = [
            (1, 2), (1, 4),
            (1, 1), (2, 1), (3, 1), (3, 2),
            (3, 4),
            (1, 5), (2, 5), (3, 5),
            (4, 2), (4, 3), (4, 4),
        ]

        expected_points_ready_to_occupy = [self.playground.get_point(c[0], c[1])
                                           for c in points_ready_to_occupy_coordinates]
        real_points_ready_to_occupy = list(self.occupier1.points_ready_to_occupy)

        self.assertEqual(len(expected_points_ready_to_occupy), len(real_points_ready_to_occupy))

        for point in real_points_ready_to_occupy:
            self.assertIn(point, expected_points_ready_to_occupy)

    def test_points_ready_to_occupy_with_other_occupiers(self):
        """
        perspective = [
            (0, 1), y(1, 1),  (2, 1),  (3, 1), (4, 1)
            (0, 2), y(1, 2), x(2, 2),  (3, 2), (4, 2)
            (0, 3), x(1, 3), x(2, 3), x(3, 3), (4, 3)
            (0, 4),  (1, 4), x(2, 4),  (3, 4), (4, 4)
            (0, 5),  (1, 5),  (2, 5), z(3, 5), (4, 5)
        ]
        """
        occupier2 = Occupier(playground=self.playground)
        occupier3 = Occupier(playground=self.playground)

        occupier2.add_point(self.playground.get_point(1, 1))
        occupier2.add_point(self.playground.get_point(1, 2))

        occupier3.add_point(self.playground.get_point(3, 5))

        self.occupier1.add_point(self.playground.get_point(1, 3))
        self.occupier1.add_point(self.playground.get_point(2, 2))
        self.occupier1.add_point(self.playground.get_point(2, 3))
        self.occupier1.add_point(self.playground.get_point(2, 4))
        self.occupier1.add_point(self.playground.get_point(3, 3))

        points_ready_to_occupy_coordinates = [
            (1, 4),
            (2, 1), (3, 1), (3, 2),
            (3, 4),
            (1, 5), (2, 5),
            (4, 2), (4, 3), (4, 4),
        ]

        expected_points_ready_to_occupy = [self.playground.get_point(c[0], c[1])
                                           for c in points_ready_to_occupy_coordinates]
        real_points_ready_to_occupy = list(self.occupier1.points_ready_to_occupy)

        self.assertEqual(len(expected_points_ready_to_occupy), len(real_points_ready_to_occupy))

        for point in real_points_ready_to_occupy:
            self.assertIn(point, expected_points_ready_to_occupy)





        # rozrost
        # wtracenia, kuiste wtracenia, wtracenia po rozroscie
        # periodyczne warunki brzegowe
        # algorytm rozrostu metoda monte carlo