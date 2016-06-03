from DataObject import DataObject

from DataObject import Graph

filepath = "resources/Iris.csv"

graph = Graph(filepath)

print('koniec')

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
