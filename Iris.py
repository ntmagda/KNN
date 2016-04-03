import math
from enum import Enum


class IrisType(Enum):
    setosa = 0
    virginica = 1
    versicolor = 2


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


class Param(object):
    def __init__(self):
        self.attribute_values = {}

    def add_attribute(self, attribute_name):
        self.attribute_values[attribute_name] = Attribute_Value()

    def __str__(self):
        return self.attribute_values.__str__()


class Attribute_Value(object):
    def __init__(self):
        self.value_itemList = {}

    def add_attribute_value(self, value):
        self.value_itemList[value] = Attribute_ItemList()

    def __str__(self):
        return self.value_itemList.__str__()


class Attribute_ItemList(object):
    def __init__(self):
        self.itemList = []

    def add_to_itemList(self, item):
        self.itemList.append(item)

