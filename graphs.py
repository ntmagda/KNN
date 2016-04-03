from Iris import Iris
import csv
from Iris import Param, Attribute_ItemList, Attribute_Value

filepath = "resources/Iris.csv"
iris_objects = list() # list of items
iris_id = 0

with open(filepath) as f:
        for row in [content for content in csv.reader(f, delimiter='\n')]:
            for object in row:
                iris_objects.append(Iris(iris_id,
                                         float(object.split(',')[0]), float(object.split(',')[1]),
                                         float(object.split(',')[2]), float(object.split(',')[3]),
                                         str(object.split(',')[4])))
                iris_id += 1


params = Param()
params.add_attribute('x')
params.add_attribute('y')
params.add_attribute('z')
params.add_attribute('w')
params.add_attribute('type')

for iris in iris_objects:

    try:
        params.attribute_values['x'].value_itemList[iris.x].add_to_itemList(iris)
    except:
        params.attribute_values['x'].add_attribute_value(iris.x)
        params.attribute_values['x'].value_itemList[iris.x].add_to_itemList(iris)

    try:
        params.attribute_values['y'].value_itemList[iris.y].add_to_itemList(iris)
    except:
        params.attribute_values['y'].add_attribute_value(iris.y)
        params.attribute_values['y'].value_itemList[iris.y].add_to_itemList(iris)

    try:
        params.attribute_values['z'].value_itemList[iris.z].add_to_itemList(iris)
    except:
        params.attribute_values['z'].add_attribute_value(iris.z)
        params.attribute_values['z'].value_itemList[iris.z].add_to_itemList(iris)

    try:
        params.attribute_values['w'].value_itemList[iris.w].add_to_itemList(iris)
    except:
        params.attribute_values['w'].add_attribute_value(iris.w)
        params.attribute_values['w'].value_itemList[iris.w].add_to_itemList(iris)

    try:
        params.attribute_values['type'].value_itemList[iris.type].add_to_itemList(iris)
    except:
        params.attribute_values['type'].add_attribute_value(iris.type)
        params.attribute_values['type'].value_itemList[iris.type].add_to_itemList(iris)


def identical(**kwargs):
    item_sets_list = []
    counter = 0
    for attribute_name, attribute_value in kwargs.iteritems():
        item_sets_list.append(set())
        for item in params.attribute_values[attribute_name].value_itemList[attribute_value].itemList:
            item_sets_list[counter].add(item)
        counter += 1
    return set.intersection(*item_sets_list)


kwargs = {'x': 5.1, 'y': 3.3, 'z': 1.7}
try:
    for item in identical(**kwargs):
        print(item)
except:
    print("Nie ma elementu o podanych atrybutach")






kwargs = {'y' : 3.5}
identical(**kwargs)
