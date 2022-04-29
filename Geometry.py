
#  Description: This program uses inputted coordinates of 3D geometric shapes and computes different attributes such as area, volume, intersection, etc.

import math
import sys

class Point (object):
    # constructor with default values
    def __init__ (self, x = 0, y = 0, z = 0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    # create a string representation of a Point
    def __str__ (self):
        return '(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'

    # get distance to another Point object
    def distance (self, other):
        return math.hypot(self.x - other.x, self.y - other.y, self.z - other.z)

    # test for equality between two points
    def __eq__ (self, other):
        tol = 10e-6
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol) and (abs(self.z - other.z) < tol))

class Sphere (object):
    # constructor with default values
    def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
        self.center = Point(x, y, z)
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.radius = float(radius)

    # returns string representation of a Sphere of the form:
    def __str__ (self):
        return 'Center: (' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + '), Radius: ' + str(self.radius)

    # compute surface area of Sphere
    def area (self):
        area = 4 * math.pi * (self.radius ** 2)
        return area

    # compute volume of a Sphere
    def volume (self):
        volume = (4/3) * math.pi * (self.radius ** 3)
        return volume

    # determines if a Point is strictly inside the Sphere
    def is_inside_point (self, p):
        return self.center.distance(p) < self.radius

    # determine if another Sphere is strictly inside this Sphere
    def is_inside_sphere (self, other):
        dist_centers = self.center.distance(other.center)
        return (dist_centers + other.radius) < self.radius

    # determine if another Sphere is strictly outside this Sphere
    def is_outside_sphere (self, other):
        dist_centers = self.center.distance(other.center)
        return dist_centers > self.radius + other.radius

    # determine if a Cube is strictly inside this Sphere
    def is_inside_cube (self, a_cube):
        for point in a_cube.vertices_of_cube():
            if not self.is_inside_point(point):
                return False
        return True

    # determine if a Cube is strictly outside this Sphere
    def is_outside_cube (self, a_cube):
        for point in a_cube.vertices_of_cube():
            if self.is_inside_point(point):
                return False
        return True

    # determine if a Cylinder is strictly inside this Sphere
    def is_inside_cyl (self, a_cyl):
        a_cyl_box = a_cyl.cylinder_as_box()
        
        for point in a_cyl_box:
            if not self.is_inside_point(point):
                return False
        return True
            
    # determine if another Sphere intersects this Sphere
    def does_intersect_sphere (self, other):
        return (not self.is_inside_sphere(other) and not self.is_outside_sphere(other))

    # determine if a Cube intersects this Sphere
    def does_intersect_cube (self, a_cube):
        return (not self.is_inside_cube(a_cube) and not self.is_outside_cube(a_cube))

    # return the largest Cube object that is inscribed by this Sphere
    def circumscribe_cube (self):
        side_of_cube = (2 * self.radius) / math.sqrt(3)
        return Cube(self.x, self.y, self.z, side_of_cube)

    # put a sphere in a box
    def sphere_as_cube (self):
        return Cube(self.x, self.y, self.z, self.radius)

class Cube (object):
    # Cube is defined by its center (which is a Point object) and side. 
    def __init__ (self, x = 0, y = 0, z = 0, side = 1):
        self.center = Point(x, y, z)
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.side = float(side)

    # string representation of a Cube of the form: 
    def __str__ (self):
        return 'Center: (' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + '), Side: ' + str(self.side)

    # compute the total surface area of Cube (all 6 sides)
    def area (self):
        area = 6 * (self.side ** 2)
        return area

    # compute volume of a Cube
    def volume (self):
        volume = self.side ** 3
        return volume

    # determines if a Point is strictly inside this Cube
    def is_inside_point (self, p):
        min_x, min_y, min_z, max_x, max_y, max_z = self.min_and_max()

        if min_x < p.x < max_x and min_y < p.y < max_y and min_z < p.z < max_z:
            return True
        else:
            return False

    # determine if a Sphere is strictly inside this Cube 
    def is_inside_sphere (self, a_sphere):
        cube_sphere = a_sphere.sphere_as_cube()
        cube_sphere_coord = cube_sphere.vertices_of_cube()

        for point in cube_sphere_coord:
           if not self.is_inside_point(point):
                return False
        return True
        
    # determine if another Cube is strictly inside this Cube
    def is_inside_cube (self, other):
        other_coord = other.vertices_of_cube()

        for point in other_coord:
            if not self.is_inside_point(point):
                return False
        return True

    # determine if another Cube is strictly outside this Cube
    def is_outside_cube (self, other):
        other_coord = other.vertices_of_cube()

        for point in other_coord:
            if self.is_inside_point(point):
                return False
        return True

    # determine if a Cylinder is strictly inside this Cube
    def is_inside_cylinder (self, a_cyl):
        a_cyl_box = a_cyl.cylinder_as_box()

        for point in a_cyl_box:
            if not self.is_inside_point(point):
                return False
        return True

    # determine if another Cube intersects this Cube
    def does_intersect_cube (self, other):
        return not(self.is_outside_cube(other) and other.is_outside_cube(self))
        

    # determine the volume of intersection if this Cube 
    def intersection_volume (self, other):
        min_x, min_y, min_z, max_x, max_y, max_z = self.min_and_max()
        min_x2, min_y2, min_z2, max_x2, max_y2, max_z2 = other.min_and_max()

        volume = max(min(max_x, max_x2) - max(min_x, min_x2), 0) * max(min(max_y, max_y2) - max(min_y, min_y2), 0) * max(min(max_z, max_z2) - max(min_z, min_z2), 0)
        return volume

    # return the largest Sphere object that is inscribed by this Cube
    def inscribe_sphere (self):
        radius = self.side / 2
        return Sphere(self.x, self.y, self.z, radius)

    # returns the 8 vertices of a cube
    def vertices_of_cube(self):
        diff = self.side / 2
        vertex1 = Point(self.x + diff, self.y - diff, self.z - diff)
        vertex2 = Point(self.x - diff, self.y - diff, self.z - diff)
        vertex3 = Point(self.x + diff, self.y + diff, self.z - diff)
        vertex4 = Point(self.x - diff, self.y + diff, self.z - diff)
        vertex5 = Point(self.x + diff, self.y - diff, self.z + diff)
        vertex6 = Point(self.x - diff, self.y - diff, self.z + diff)
        vertex7 = Point(self.x + diff, self.y + diff, self.z + diff)
        vertex8 = Point(self.x - diff, self.y + diff, self.z + diff)

        return [vertex1, vertex2, vertex3, vertex4, vertex5, vertex6, vertex7, vertex8]

    # returns min and max values of 8 vertices
    def min_and_max(self):
        points = self.vertices_of_cube()

        min_x = min(points[0].x, points[1].x, points[2].x, points[3].x, points[4].x, points[5].x, points[6].x, points[7].x)
        min_y = min(points[0].y, points[1].y, points[2].y, points[3].y, points[4].y, points[5].y, points[6].y, points[7].y)
        min_z = min(points[0].z, points[1].z, points[2].z, points[3].z, points[4].z, points[5].z, points[6].z, points[7].z)
        max_x = max(points[0].x, points[1].x, points[2].x, points[3].x, points[4].x, points[5].x, points[6].x, points[7].x)
        max_y = max(points[0].y, points[1].y, points[2].y, points[3].y, points[4].y, points[5].y, points[6].y, points[7].y)
        max_z = max(points[0].z, points[1].z, points[2].z, points[3].z, points[4].z, points[5].z, points[6].z, points[7].z)

        return min_x, min_y, min_z, max_x, max_y, max_z

class Cylinder (object):
    # Cylinder is defined by its center (which is a Point object), radius, and height.
    def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
        self.center = Point(x, y, z)
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.radius = float(radius)
        self.height = float(height)

    # returns a string representation of a Cylinder of the form: 
    def __str__ (self):
        return 'Center: (' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + '), Radius: ' + str(self.radius) + ', Height: ' + str(self.height)

    # compute surface area of Cylinder
    def area (self):
        area = (2 * math.pi * self.radius * self.height) + (2 * math.pi * (self.radius ** 2))
        return area

    # compute volume of a Cylinder
    def volume (self):
        volume = math.pi * (self.radius ** 2) * self.height
        return volume

    # determine if a Point is strictly inside this Cylinder
    def is_inside_point (self, p):
        min_x, min_y, min_z, max_x, max_y, max_z = self.min_and_max_cyl()
        
        if min_x < p.x < max_x and min_y < p.y < max_y and min_z < p.z < max_z:
            return True
        else:
            return False

    # determine if a Sphere is strictly inside this Cylinder
    def is_inside_sphere (self, a_sphere):
        a_sphere_box = a_sphere.sphere_as_cube()

        for point in a_sphere_box.vertices_of_cube():
            if not self.is_inside_point(point):
                return False
        return True

    # determine if a Cube is strictly inside this Cylinder
    def is_inside_cube (self, a_cube):

        for point in a_cube.vertices_of_cube():
            if not self.is_inside_point(point):
                return False
        return True

    # determine if another Cylinder is strictly inside this Cylinder
    def is_inside_cylinder (self, other):
        
        for point in other.cylinder_as_box():
            if not self.is_inside_point(point):
                return False
        return True

    # determine if another Cylinder is strictly outside this Cylinder
    def is_outside_cylinder (self, other):
        
        for point in other.cylinder_as_box():
            if self.is_inside_point(point):
                return False
        return True

    # determine if another Cylinder intersects this Cylinder
    def does_intersect_cylinder (self, other):
        return not (self.is_inside_cylinder(other) or other.is_inside_cylinder(self) or self.is_outside_cylinder(other) or other.is_outside_cylinder(self))

    # returns coordinates of Cylinder in a box
    def cylinder_as_box(self):
        side_length = self.radius
        height_length = self.height / 2

        vertex1 = Point(self.x + side_length, self.y - side_length, self.z - height_length)
        vertex2 = Point(self.x - side_length, self.y - side_length, self.z - height_length)
        vertex3 = Point(self.x + side_length, self.y + side_length, self.z - height_length)
        vertex4 = Point(self.x - side_length, self.y + side_length, self.z - height_length)
        vertex5 = Point(self.x + side_length, self.y - side_length, self.z + height_length)
        vertex6 = Point(self.x - side_length, self.y - side_length, self.z + height_length)
        vertex7 = Point(self.x + side_length, self.y + side_length, self.z + height_length)
        vertex8 = Point(self.x - side_length, self.y + side_length, self.z + height_length)

        return [vertex1, vertex2, vertex3, vertex4, vertex5, vertex6, vertex7, vertex8, vertex8]

    # returns min and max values of 8 Cylinder box vertices
    def min_and_max_cyl(self):
        points = self.cylinder_as_box()
        

        min_x = min(points[0].x, points[1].x, points[2].x, points[3].x, points[4].x, points[5].x, points[6].x, points[7].x)
        min_y = min(points[0].y, points[1].y, points[2].y, points[3].y, points[4].y, points[5].y, points[6].y, points[7].y)
        min_z = min(points[0].z, points[1].z, points[2].z, points[3].z, points[4].z, points[5].z, points[6].z, points[7].z)
        max_x = max(points[0].x, points[1].x, points[2].x, points[3].x, points[4].x, points[5].x, points[6].x, points[7].x)
        max_y = max(points[0].y, points[1].y, points[2].y, points[3].y, points[4].y, points[5].y, points[6].y, points[7].y)
        max_z = max(points[0].z, points[1].z, points[2].z, points[3].z, points[4].z, points[5].z, points[6].z, points[7].z)

        return min_x, min_y, min_z, max_x, max_y, max_z
        
def main():
    # read the coordinates of the first Point p
    p_coord = sys.stdin.readline().split()

    # create a Point object
    p_x = float(p_coord[0])
    p_y = float(p_coord[1])
    p_z = float(p_coord[2])
    p = Point(p_x, p_y, p_z)

    # read the coordinates of the second Point q
    q_coord = sys.stdin.readline().split()

    # create a Point object
    q_x = float(q_coord[0])
    q_y = float(q_coord[1])
    q_z = float(q_coord[2])
    q = Point(q_x, q_y, q_z)

    # read the coordinates of the center and radius of sphereA
    sphereA_coord = sys.stdin.readline().split()

    # create a Sphere object
    sphereA_x = float(sphereA_coord[0])
    sphereA_y = float(sphereA_coord[1])
    sphereA_z = float(sphereA_coord[2])
    sphereA_radius = float(sphereA_coord[3])
    sphereA = Sphere(sphereA_x, sphereA_y, sphereA_z, sphereA_radius)

    # read the coordinates of the center and radius of sphereB
    sphereB_coord = sys.stdin.readline().split()
    
    # create a Sphere object
    sphereB_x = float(sphereB_coord[0])
    sphereB_y = float(sphereB_coord[1])
    sphereB_z = float(sphereB_coord[2])
    sphereB_radius = float(sphereB_coord[3])
    sphereB = Sphere(sphereB_x, sphereB_y, sphereB_z, sphereB_radius)
    
    # read the coordinates of the center and side of cubeA
    cubeA_coord = sys.stdin.readline().split()

    # create a Cube object
    cubeA_x = float(cubeA_coord[0])
    cubeA_y = float(cubeA_coord[1])
    cubeA_z = float(cubeA_coord[2])
    cubeA_side = float(cubeA_coord[3])
    cubeA = Cube(cubeA_x, cubeA_y, cubeA_z, cubeA_side)

    # read the coordinates of the center and side of cubeB
    cubeB_coord = sys.stdin.readline().split()

    # create a Cube object 
    cubeB_x = float(cubeB_coord[0])
    cubeB_y = float(cubeB_coord[1])
    cubeB_z = float(cubeB_coord[2])
    cubeB_side = float(cubeB_coord[3])
    cubeB = Cube(cubeB_x, cubeB_y, cubeB_z, cubeB_side)
    
    # read the coordinates of the center, radius and height of cylA
    cylA_coord = sys.stdin.readline().split()

    # create a Cylinder object
    cylA_x = float(cylA_coord[0])
    cylA_y = float(cylA_coord[1])
    cylA_z = float(cylA_coord[2])
    cylA_radius = float(cylA_coord[3])
    cylA_height = float(cylA_coord[4])
    cylA = Cylinder(cylA_x, cylA_y, cylA_z, cylA_radius, cylA_height)

    # read the coordinates of the center, radius and height of cylB
    cylB_coord = sys.stdin.readline().split()
    
    # create a Cylinder object
    cylB_x = float(cylB_coord[0])
    cylB_y = float(cylB_coord[1])
    cylB_z = float(cylB_coord[2])
    cylB_radius = float(cylB_coord[3])
    cylB_height = float(cylB_coord[4])
    cylB = Cylinder(cylB_x, cylB_y, cylB_z, cylB_radius, cylB_height)

    # print if the distance of p from the origin is greater than the distance of q from the origin
    origin = Point(0, 0, 0)
    dist_p = p.distance(origin)
    dist_q = q.distance(origin)
    if dist_p > dist_q:
        print("Distance of Point p from the origin is greater than the distance of Point q from the origin")
    else:
        print("Distance of Point p from the origin is not greater than the distance of Point q from the origin")
    
    # print if Point p is inside sphereA
    if sphereA.is_inside_point(p):
        print("Point p is inside sphereA")
    else:
        print("Point p is not inside sphereA")

    # print if sphereB is inside sphereA
    if sphereA.is_inside_sphere(sphereB):
        print("sphereB is inside sphereA")
    else:
        print("sphereB is not inside sphereA")

    # print if cubeA is inside sphereA
    if sphereA.is_inside_cube(cubeA):
        print("cubeA is inside sphereA")
    else:
        print("cubeA is not inside sphereA")

    # print if cylA is inside sphereA
    if sphereA.is_inside_cyl(cylA):
        print("cylA is inside sphereA")
    else:
        print("cylA is not inside sphereA")

    # print if sphereA intersects with sphereB
    if sphereB.does_intersect_sphere(sphereA):
        print("sphereA does intersect sphereB")
    else:
        print("sphereA does not intersect sphereB")

    # print if cubeB intersects with sphereB
    if sphereB.does_intersect_cube(cubeB):
        print("cubeB does intersect sphereB")
    else:
        print("cubeB does not intersect sphereB")

    # print if the volume of the largest Cube that is circumscribed by sphereA is greater than the volume of cylA
    if sphereA.circumscribe_cube().volume() > cylA.volume():
        print("Volume of the largest Cube that is circumscribed by sphereA is greater than the volume of cylA")
    else:
        print("Volume of the largest Cube that is circumscribed by sphereA is not greater than the volume of cylA")

    # print if Point p is inside cubeA
    if cubeA.is_inside_point(p):
        print("Point p is inside cubeA")
    else:
        print("Point p is not inside cubeA")

    # print if sphereA is inside cubeA
    if cubeA.is_inside_sphere(sphereA):
        print("sphereA is inside cubeA")
    else:
        print("sphereA is not inside cubeA")

    # print if cubeB is inside cubeA
    if cubeA.is_inside_cube(cubeB):
        print("cubeB is inside cubeA")
    else:
        print("cubeB is not inside cubeA")

    # print if cylA is inside cubeA
    if cubeA.is_inside_cylinder(cylA):
        print("cylA is inside cubeA")
    else:
        print("cylA is not inside cubeA")

    # print if cubeA intersects with cubeB
    if cubeB.does_intersect_cube(cubeA):
        print("cubeA does intersect cubeB")
    else:
        print("cubeA does not intersect cubeB")

    # print if the intersection volume of cubeA and cubeB is greater than the volume of sphereA
    if cubeA.intersection_volume(cubeB) > sphereA.volume():
        print("Intersection volume of cubeA and cubeB is greater than the volume of sphereA")
    else:
        print("Intersection volume of cubeA and cubeB is not greater than the volume of sphereA")

    # print if the surface area of the largest Sphere object inscribed by cubeA is greater than the surface area of cylA
    if cubeA.inscribe_sphere().area() > cylA.area():
        print("Surface area of the largest Sphere object inscribed by cubeA is greater than the surface area of cylA")
    else:
        print("Surface area of the largest Sphere object inscribed by cubeA is not greater than the surface area of cylA")

    # print if Point p is inside cylA
    if cylA.is_inside_point(p):
        print("Point p is inside cylA")
    else:
        print("Point p is not inside cylA")

    # print if sphereA is inside cylA
    if cylA.is_inside_sphere(sphereA):
        print("sphereA is inside cylA")
    else:
        print("sphereA is not inside cylA")

    # print if cubeA is inside cylA
    if cylA.is_inside_cube(cubeA):
        print("cubeA is inside cylA")
    else:
        print("cubeA is not inside cylA")

    # print if cylB is inside cylA
    if cylA.is_inside_cylinder(cylB):
        print("cylB is inside cylA")
    else:
        print("cylB is not inside cylA")

    # print if cylB intersects with cylA
    if cylA.does_intersect_cylinder(cylB):
        print("cylB does intersect cylA")
    else:
        print("cylB does not intersect cylA")

if __name__ == "__main__":
  main()
