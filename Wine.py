
from Iris import DataObject
from Iris import Iris
import math

class Wine(DataObject):
    def __init__(self, iris_id, type, *args):
        super(Wine, self).__init__(iris_id, type)
        self.alcohol = args[0]
        self.malic_acid = args[1]
        self.ash = args[2]
        self.alcalinity_of_ash = args[3]
        self.magnesium = args[4]
        self.total_phenols = args[5]
        self.flavanoids = args[6]
        self.nonflavanoid_phenols = args[7]
        self.proanthocyanins = args[8]
        self.color_intensity = args[9]
        self.hue = args[10]
        self.od_od_of_diluted_wines = args[12]
        self.proline = args[12]

    def count_distance(self, other_wine):
        distance = math.sqrt(math.pow(other_wine.alcohol - self.alcohol, 2) +
                             math.pow(other_wine.alcalinity_of_ash - self.alcalinity_of_ash, 2) +
                             math.pow(other_wine.ash - self.ash, 2) +
                             math.pow(other_wine.color_intensity - self.color_intensity, 2) +
                             math.pow(other_wine.flavanoids - self.flavanoids, 2) +
                             math.pow(other_wine.hue - self.hue, 2) +
                             math.pow(other_wine.od_od_of_diluted_wines - self.od_od_of_diluted_wines, 2) +
                             math.pow(other_wine.magnesium - self.magnesium, 2) +
                             math.pow(other_wine.malic_acid - self.malic_acid, 2) +
                             math.pow(other_wine.total_phenols - self.total_phenols, 2) +
                             math.pow(other_wine.proline - self.proline, 2) +
                             math.pow(other_wine.proanthocyanins- self.proanthocyanins, 2) +
                             math.pow(other_wine.nonflavanoid_phenols - self.nonflavanoid_phenols, 2))
        return distance

    def __str__(self):
        return 'alcohol: ' + str(self.alcohol) + '\n' +\
               'proanthocyanins: ' + str(self.proanthocyanins) + '\n' +\
               'nonflavanoid_phenols: ' + str(self.nonflavanoid_phenols) + '\n' +\
               'proline: ' + str(self.proline) + '\n' +\
               'total_phenols: ' + str(self.total_phenols) + '\n' +\
               'malic_acid: ' + str(self.malic_acid) + '\n' +\
               'alcalinity_of_ash: ' + str(self.alcalinity_of_ash) + '\n' +\
               'ash ' + str(self.ash) + '\n' +\
               'color_intensity: ' + str(self.color_intensity) + '\n' +\
               'flavanoids: ' + str(self.flavanoids) + '\n' +\
               'hue: ' + str(self.hue) + '\n' +\
               'magnesium: ' + str(self.magnesium) + '\n' +\
               'od_od_of_diluted_wines: ' + str(self.od_od_of_diluted_wines) + '\n' +\
               'type: ' + str(self.type) + '\n'