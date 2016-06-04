from DataObject import DataObjectWrapper

from DataObject import Graph
from find_similarities import fill_similarities_weigth, init_weigth, find_objects, find_object_by_id

filepath = "resources/Wine.csv"

graph = Graph(filepath)
init_weigth(graph)
fill_similarities_weigth(graph)
object = find_object_by_id(graph, 3)
# item_list = find_objects(graph,"Ash", "2.61")


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
