from math import sqrt


def calc_distance(point1, point2):
    distances = []
    for p1, p2 in zip(point1, point2):
        # Extraire les coordonnées des points
        x1, y1, c1 = p1
        x2, y2, c2 = p2

        # Calculer la distance euclidienne
        distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (c2 - c1) ** 2)

        distances.append(distance)

    return distances


# Exemple d'utilisation
points1 = [(1.0, 1.0, 1.0), (2.0, 2.0, 2.0), (3.0, 3.0, 3.0)]
points2 = [(4.0, 4.0, 4.0), (5.0, 5.0, 5.0), (6.0, 6.0, 6.0)]
distances = calc_distance(points1, points2)

result = ("Le nom de la fonction est: calc_distance\n"
          "\tles arguments suivants : {} et {}.\n"
          "\t{}".format(points1, points2, distances))

print(result)
