def find_similar_object(graph, data_object):
    pass

# inicjalizuje tablice podobienstw zerami dla wszystkich obiektow
def init_all_weigth(graph):
    for id in graph.data_objects:
        init_weigth(graph, id)

# inicjalizuje tablice podobienstw zerami dla jednego obiektu o podanym id
def init_weigth(graph, id):
    for id1 in graph.data_objects:
        graph.data_objects[id].similarity_weigth[id1] = 0
        graph.data_objects[id].strong_similarity[id1] = 0

# wypelnia tablice podobienstw dla wszystkich obiektow
def fill_all_similarities_weigth(graph):
    for id in graph.data_objects:
        fill_similarities_weigth(graph, id)

# wypelnia tablice podobienstw dla obiektu o podanym id (obiekt musi sie znajdowac w drzewie)
def fill_similarities_weigth(graph, id):
    data_object = graph.data_objects[id]
    for attribute_name in graph.params.attribute_names:
        object_val = data_object.params[attribute_name]
        # jesli obiekt ma ktorychs z parametrow identyczny jak obiekt badany to dodaje 1
        strong_similar_item_list = graph.params.attribute_names[attribute_name].attribute_values[object_val].get_item_list()
        set_strong_similarity(data_object,strong_similar_item_list)
        for attribute_value in graph.params.attribute_names[attribute_name].attribute_values:
            similarity = count_similarity(graph, attribute_name, object_val, attribute_value)
            similar_item_list = graph.params.attribute_names[attribute_name].attribute_values[attribute_value].get_item_list()
            setAsSimilar(data_object, similar_item_list, similarity)



# bierze obiekt i do tablicy z indeksami i wspolczynnikiem podobienstwa dodaje odpowiednia wartosc podobienstwa
def setAsSimilar(data_object, similar_item_list, similarity):
    for id in similar_item_list:
        data_object.similarity_weigth[id] += similarity

# to samo co wyrzej ale tylko dla tych ktore maja dokladnie ta sama wartosc
def set_strong_similarity(data_object, similar_item_list):
    for id in similar_item_list:
        data_object.strong_similarity[id] += 1

# oblicza podobienstwo
def count_similarity(graph, attribute_name, data_object_value, similar_value):
    attribute_values = graph.params.attribute_names[attribute_name].attribute_values
    return 1 - (abs(float(data_object_value) - float(similar_value)))/(float(max(attribute_values))- float(min(attribute_values)))




