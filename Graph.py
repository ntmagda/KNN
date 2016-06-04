import csv
import math


class DataObject(object):
    def __init__(self, id):
        self.id = id
        self.similarity_weigth = {} # tablica podobienstw
        self.strong_similarity = {} # tablica identycznosci


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


    def __str__(self): #temp
        return 'iris_id: ' + str(self.id) + '\n' +\
               'leaf-length: ' + str(self.params['leaf-length']) + '\n' +\
               'leaf-width: ' + str(self.params['leaf-width']) + '\n' +\
               'petal-length ' + str(self.params['petal-length']) + '\n' +\
               'petal-width: ' + str(self.params['petal-width']) + '\n' +\
               'type: ' + str(self.params['type']) + '\n'


class Graph(object):
    def __init__(self, filepath):
        self.data_objects = {} # list of items
        self.params = Param()
        id = -1
        attribute_names = [] # tablica z nazwami parametrow
        with open(filepath) as f:
                for row in [content for content in csv.reader(f, delimiter='\n')]:
                    if id == -1:  # pierwszy wiersz i wpisanie attrubite_names do params
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
                            self.data_objects[id] = (DataObjectWrapper(id, **kwargs))
                            id += 1


        for attribute_name in attribute_names:
            self.params.add_attribute_name(str(attribute_name))

        for id in self.data_objects:
            add_object_to_tree(self, id)

# tworzy obiekt o podanych wartosciach argumentow
def create_object(graph, **kwargs):
    #  generate new id for object
    custom_ids = []
    for id in graph.data_objects:
        custom_ids.append(id)
    new_id = max(custom_ids)+1
    graph.data_objects[new_id] = (DataObjectWrapper(new_id, **kwargs))
    return new_id

# dodaje obiekt do drzewa
def add_object_to_tree(graph, id):
    data_object = graph.data_objects[id]
    for attribute_name, attribute_values in graph.params.attribute_names.iteritems():
        try:
            # dodanie na koncu drzewa idikow obiektu w odpowiednim miejscu
            graph.params.attribute_names[attribute_name].attribute_values[data_object.params[attribute_name]].add_to_item_list(data_object.id)
        except:
            graph.params.attribute_names[attribute_name].add_value(data_object.params[attribute_name])
            graph.params.attribute_names[attribute_name].attribute_values[data_object.params[attribute_name]].add_to_item_list(data_object.id)



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

    def get_item_list(self):
        return self.attribute_itemList

    def __str__(self):
        return self.attribute_value
