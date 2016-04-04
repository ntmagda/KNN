import math
from enum import Enum


class IrisType(Enum):
    setosa = 0
    virginica = 1
    versicolor = 2

IrisParams = {}


class DataObject(object):
    def __init__(self, id):
        self.id = id


class Iris(DataObject):
    def __init__(self, iris_id, **kwargs):
        super(Iris, self).__init__(iris_id)
        self.params = {}
        for param_name, param_value in kwargs.iteritems():
            self.params[param_name] = param_value

    def count_distance(self, other_iris):
        sum = 0
        for param_name, param_value in other_iris.params:
            sum += math.pow(other_iris.params[param_name] - self.params[param_name], 2)
        distance = math.sqrt(sum)
        return distance


    def __str__(self):
        return 'iris_id: ' + str(self.id) + '\n' +\
               'leaf-length: ' + str(self.params['leaf-length']) + '\n' +\
               'leaf-width: ' + str(self.params['leaf-width']) + '\n' +\
               'petal-length ' + str(self.params['petal-length']) + '\n' +\
               'petal-width: ' + str(self.params['petal-width']) + '\n' +\
               'type: ' + str(self.params['type']) + '\n'


class Param(object):
    def __init__(self):
        self.attribute_names = {}

    def add_attribute_name(self, attribute_name):
        self.attribute_names[attribute_name] = Attribute_Value()

    def __str__(self):
        return self.attribute_names.__str__()


class Attribute_Value(object):
    def __init__(self):
        self.attribute_values = {}

    def add_value(self, value):
        self.attribute_values[value] = Attribute_ItemList()

    def __str__(self):
        return self.attribute_values.__str__()


class Attribute_ItemList(object):
    def __init__(self):
        self.attribute_itemList = []

    def add_to_itemList(self, item):
        self.attribute_itemList.append(item)

