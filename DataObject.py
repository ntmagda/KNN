import math


class DataObject1(object):
    def __init__(self, id):
        self.id = id


class DataObject(DataObject1):
    def __init__(self, id, **kwargs):
        super(DataObject, self).__init__(id)
        self.params = {}
        for param_name, param_value in kwargs.iteritems():
            self.params[param_name] = param_value

    def count_distance(self, other_object):
        sum = 0
        for param_name, param_value in other_object.params:
            sum += math.pow(other_object.params[param_name] - self.params[param_name], 2)
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
        self.attribute_names[attribute_name] = AttributeValue()

    def __str__(self):
        return self.attribute_names.__str__()


class AttributeValue(object):
    def __init__(self):
        self.attribute_values = {}

    def add_value(self, value):
        self.attribute_values[value] = AttributeItemList()

    def __str__(self):
        return self.attribute_values.__str__()


class AttributeItemList(object):
    def __init__(self):
        self.attribute_itemList = []

    def add_to_item_list(self, item):
        self.attribute_itemList.append(item)

