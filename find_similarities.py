def find_similar_object(graph, data_object):
    pass

def init_weigth(graph):
    for data_object in graph.data_objects:
        for data_object1 in graph.data_objects:
            data_object.similarity_weigth[data_object1.id] = 0
            data_object.strong_similarity[data_object1.id] = 0


# bierze obiekt i do tablicy z indeksami i wspolczynnikiem podobienstwa dodaje 1 dla tych ktore sa podobne
def setAsSimilar(data_object, similar_item_list, similarity):
    for id in similar_item_list:
        data_object.similarity_weigth[id] += similarity

def set_strong_similarity(data_object, similar_item_list):
    for id in similar_item_list:
        data_object.strong_similarity[id] += 1

def count_similarity(graph, attribute_name, data_object_value, similar_value):
    attribute_values = graph.params.attribute_names[attribute_name].attribute_values
    return 1 - (abs(float(data_object_value) - float(similar_value)))/(float(max(attribute_values))- float(min(attribute_values)))


def fill_similarities_weigth(graph):
    for data_object in graph.data_objects:
        for attribute_name in graph.params.attribute_names:
            object_val = data_object.params[attribute_name]
            # jesli obiekt ma ktorychs z parametrow identyczny jak obiekt badany to dodaje 1
            strong_similar_item_list = graph.params.attribute_names[attribute_name].attribute_values[object_val].get_item_list()
            set_strong_similarity(data_object,strong_similar_item_list)
            for attribute_value in graph.params.attribute_names[attribute_name].attribute_values:
                similarity = count_similarity(graph, attribute_name, object_val, attribute_value)
                similar_item_list = graph.params.attribute_names[attribute_name].attribute_values[attribute_value].get_item_list()
                setAsSimilar(data_object, similar_item_list, similarity)

def find_objects(graph, attribute_name, attribute_value):
    return graph.params.attribute_names[attribute_name].attribute_values[attribute_value].get_item_list()


def find_object_by_id(graph, id):
    for data_object in graph.data_objects:
        if data_object.id == id:
            return data_object