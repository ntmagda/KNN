from DataObject import DataObject
import csv
from DataObject import Param, AttributeItemList, AttributeValue

filepath = "resources/Wine.csv"
data_objects = list() # list of items
id = -1

params = Param()
attribute_names = [] # tablica z nazwami parametrow
with open(filepath) as f:
        for row in [content for content in csv.reader(f, delimiter='\n')]:
            if id == -1: # pierwszy wiersz i wpisanie attrubite_names do params
                for object in row:
                    for attribute_name in object.split(','):
                        attribute_names.append(attribute_name) #wpisanie atteibute_name do tablicy z nazwami paramterow
                id += 1
            else:
                for object in row:
                    kwargs = {}
                    i = 0
                    for attribute_name in attribute_names: # przygotowanie argumentow do wpisania do obiektu
                        kwargs[attribute_name] = str(object.split(',')[i])
                        i += 1
                    data_objects.append(DataObject(id, **kwargs))
                    id += 1

for attribute_name in attribute_names:
    params.add_attribute_name(str(attribute_name))

for data_object in data_objects:
    for attribute_name, attribute_values in params.attribute_names.iteritems():
        try:
            params.attribute_names[attribute_name].attribute_values[data_object.params[attribute_name]].add_to_item_list(data_object)
        except:
            params.attribute_names[attribute_name].add_value(data_object.params[attribute_name])
            params.attribute_names[attribute_name].attribute_values[data_object.params[attribute_name]].add_to_item_list(data_object)

# def identical(**kwargs):
#     item_sets_list = []
#     counter = 0
#     for attribute_name, attribute_value in kwargs.iteritems():
#         item_sets_list.append(set())
#         for item in params.attribute_names[attribute_name].value_itemList[attribute_value].itemList:
#             item_sets_list[counter].add(item)
#         counter += 1
#     return set.intersection(*item_sets_list)
#
#
# kwargs = {'x': 5.1, }
# try:
#     for item in identical(**kwargs):
#         print(item)
# except:
#     print("Nie ma elementu o podanych atrybutach")
#
# kwargs = {'y' : 3.5}
# identical(**kwargs)
