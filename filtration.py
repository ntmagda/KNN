from Graph import create_object, add_object_to_tree
from find_similarities import init_weigth, fill_similarities_weigth

# znajduje obiekt o podanej wartosci danego atrybutu
def find_objects(graph, attribute_name, attribute_value):
    return graph.params.attribute_names[attribute_name].attribute_values[attribute_value].get_item_list()

# filtruje po podanych wartosciach argumentow
def filter_objects(graph, **kwargs):
    item_list = []
    for id, data_object in graph.data_objects.iteritems():
        item_list.append(data_object.id)
    for param_name, param_value in kwargs.iteritems():
        item_list = set(item_list).intersection(graph.params.attribute_names[param_name].attribute_values[param_value].get_item_list())
    return item_list

# znajduje obiekt po jego id
def find_object_by_id(graph, id):
    return graph.data_objects[id]

# znajduje najbardziej podobne obikety do obiektu o podanym id
def get_the_most_similar_by_id(graph, data_object_id, quantity):
    import operator
    item_list = graph.data_objects[data_object_id].similarity_weigth
    sorted_item_list = sorted(item_list.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_item_list[:quantity]

# znajduje najbardziej podobne obiekty do obiektu o podanych wartosciach atrybutow
def get_the_most_similar(graph, quantity, **kwargs):
    id = create_object(graph, **kwargs)
    add_object_to_tree(graph, id)
    init_weigth(graph, id)
    fill_similarities_weigth(graph,id)
    return get_the_most_similar_by_id(graph, id, quantity)

# znajduje najmniej podobne obiekty do obiektu o podanych wartosciach atrybutow
def get_the_most_different(graph, data_object_id, quantity):
    import operator
    item_list = graph.data_objects[data_object_id].similarity_weigth
    sorted_item_list = sorted(item_list.items(), key=operator.itemgetter(1))
    return sorted_item_list[:quantity]

