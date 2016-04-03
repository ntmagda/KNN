import math

class Iris(object):
    def __init__(self, iris_id, x, y, z, w, type):
        self.iris_id = iris_id
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.type = type

    def count_distance(self, other_iris):
        distance = math.sqrt(math.pow(other_iris.x - self.x, 2) +
                             math.pow(other_iris.y - self.y, 2) +
                             math.pow(other_iris.z - self.z, 2) +
                             math.pow(other_iris.w - self.w, 2))
        return distance


    def __str__(self):
        return 'iris_id: ' + str(self.iris_id) + '\n' +\
               'x: ' + str(self.x) + '\n' +\
               'y: ' + str(self.y) + '\n' +\
               'z: ' + str(self.z) + '\n' +\
               'w: ' + str(self.w) + '\n' +\
               'type: ' + str(self.type) + '\n'


iris1 = Iris(1,1,2,3,4,"iris1")
iris2 = Iris(2,2,3,4,5,"iris2")

iris1.count_distance(iris2)

