import csv
from DataObject import DataObject
from DataObject import IrisType



filepath = "resources/Iris.csv"
iris_obejcts = list() # list of items
iris_id = 0
k = 10 # licznosc zbioru testowego
distance_to_classes = [[0 for x in range(3)] for x in range(k)]
with open(filepath) as f:
        for row in [content for content in csv.reader(f, delimiter='\n')]:
            for object in row:
                iris_obejcts.append(DataObject(iris_id,
                                               float(object.split(',')[0]), float(object.split(',')[1]),
                                               float(object.split(',')[2]), float(object.split(',')[3]),
                                               str(object.split(',')[4])))
                iris_id += 1

points = 0
for test_iris in iris_obejcts[0:k]:
    setosa_counter = 0
    virginica_counter = 0
    versicolor_counter = 0

    setosa_distance = 0.0
    virginica_distance = 0.0
    versicolor_distance = 0.0
    for iris in iris_obejcts[k:]:
        # class Iris-Setosa distance
        if iris.type == 'Iris-setosa':
            setosa_distance += test_iris.count_distance(iris)
            setosa_counter += 1
        elif iris.type == 'Iris-virginica':
            virginica_distance += test_iris.count_distance(iris)
            virginica_counter += 1
        elif iris.type == 'Iris-versicolor':
            versicolor_distance += test_iris.count_distance(iris)
            versicolor_counter += 1

    distance_to_classes[test_iris.iris_id][IrisType.setosa.value] = setosa_distance
    distance_to_classes[test_iris.iris_id][IrisType.virginica.value] = virginica_distance
    distance_to_classes[test_iris.iris_id][IrisType.versicolor.value] = versicolor_distance

    min_value = min((distance_to_classes[test_iris.iris_id]))

    # test zgodnosci
    if ((test_iris.type == 'Iris-setosa' and distance_to_classes[test_iris.iris_id].index(min_value) == IrisType.setosa.value) or
       (test_iris.type == 'Iris-virginica' and distance_to_classes[test_iris.iris_id].index(min_value) == IrisType.virginica.value) or
       (test_iris.type == 'Iris-versicolor' and distance_to_classes[test_iris.iris_id].index(min_value) == IrisType.versicolor.value)):
            points += 1

print('points')
print(points)



