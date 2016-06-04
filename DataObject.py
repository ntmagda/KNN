import csv
import math


class DataObject(object):
    def __init__(self, id):
        self.id = id
        self.similarity_weigth = {}
        self.strong_similarity = {}


class DataObjectWrapper(DataObject):
    def __init__(self, id, **kwargs):
        super(DataObjectWrapper, self).__init__(id)
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


class Graph(object):
    def __init__(self, filepath):
        self.data_objects = list() # list of items
        self.params = Param()
        id = -1
        attribute_names = [] # tablica z nazwami parametrow
        with open(filepath) as f:
                for row in [content for content in csv.reader(f, delimiter='\n')]:
                    if id == -1:  #pierwszy wiersz i wpisanie attrubite_names do params
                        for object in row:
                            for attribute_name in object.split(','):
                                attribute_names.append(attribute_name) # wpisanie atteibute_name do tablicy z nazwami paramterow
                        id += 1
                    else:
                        for object in row:
                            kwargs = {}
                            i = 0
                            for attribute_name in attribute_names: # przygotowanie argumentow do wpisania do obiektu
                                kwargs[attribute_name] = str(object.split(',')[i])
                                i += 1
                            self.data_objects.append(DataObjectWrapper(id, **kwargs))
                            id += 1


        for attribute_name in attribute_names:
            self.params.add_attribute_name(str(attribute_name))

        for data_object in self.data_objects:
            for attribute_name, attribute_values in self.params.attribute_names.iteritems():
                try:
                    # dodanie na koncu drzewa idikow obiektu w odpowiednim miejscu
                    self.params.attribute_names[attribute_name].attribute_values[data_object.params[attribute_name]].add_to_item_list(data_object.id)
                except:
                    self.params.attribute_names[attribute_name].add_value(data_object.params[attribute_name])
                    self.params.attribute_names[attribute_name].attribute_values[data_object.params[attribute_name]].add_to_item_list(data_object.id)


class Param(object):
    def __init__(self):
        self.attribute_names = {}

    def add_attribute_name(self, attribute_name):
        self.attribute_names[attribute_name] = AttributeName(attribute_name)

    def __str__(self):
        return "PARAM"


class AttributeName(object):
    def __init__(self, attribute_name):
        self.attribute_values = {}
        self.attribute_name = attribute_name

    def add_value(self, value):
        self.attribute_values[value] = AttributeValue(value)

    def __str__(self):
        return self.attribute_name


class AttributeValue(object):
    def __init__(self, value):
        self.attribute_itemList = []
        self.attribute_value = value

    def add_to_item_list(self, item):
        self.attribute_itemList.append(item)

    def __str__(self):
        return self.attribute_value

    def get_item_list(self):
        return self.attribute_itemList

