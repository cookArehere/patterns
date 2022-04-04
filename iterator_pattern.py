from collections.abc import Iterator, Iterable


class DepthFirstSearch(Iterator):

    def __init__(self, graf, vertex):
        self.__graf = graf
        self.used = set()
        self.neighbour = None
        self.vertex = vertex

    def __next__(self):

        if self.vertex in self.used:
            self.vertex = self.neighbour
        return self.enumeration_vertex(self.vertex, self.__graf, self.used)

    def enumeration_vertex(self, vertex, graf, used):

        self.used.add(vertex)
        for neighbour in graf[vertex]:
            if neighbour is not used:
                self.neighbour = neighbour
                return neighbour


class Graf(Iterable):

    def __init__(self, first_vertex=None):
        self.graf = {}
        self.first_vertex = first_vertex

    def __iter__(self):
        return DepthFirstSearch(self.graf, self.first_vertex)

    def add_vertex(self, vertex, neighbour: list):
        self.graf[vertex] = neighbour

    def counts_vertex(self):
        return len(self.graf)


class Station:

    def __init__(self, name, coordinates, buses: list):
        self.name = name
        self.coordinates = coordinates
        self.buses = buses

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


if __name__ == '__main__':

    station_0 = Station("station_0", "00.00.00", [203, 185, 56])
    station_1 = Station("station_1", "01.01.01", [203, 185, 56])
    station_2 = Station("station_2", "02.02.02", [78, 185, 56])
    station_3 = Station("station_3", "03.03.03", [203, 9, 56])
    station_4 = Station("station_4", "04.04.04", [111, 35, 56])
    station_5 = Station("station_5", "05.05.05", [203, 185, 56])
    station_6 = Station("station_6", "06.06.06", [203, 185, 56])
    station_7 = Station("station_7", "07.07.07", [203, 185, 56])
    station_8 = Station("station_8", "08.08.08", [203, 185, 56])
    station_9 = Station("station_9", "09.09.09", [203, 185, 56])

    fid_for_graf = {
        station_0: [station_1, station_2],
        station_1: [station_0, station_3, station_7],
        station_2: [station_0, station_3],
        station_3: [station_1, station_2, station_4],
        station_4: [station_3, station_5, station_6],
        station_5: [station_4],
        station_6: [station_4, station_8],
        station_7: [station_1, station_8, station_9],
        station_8: [station_6, station_7],
        station_9: [station_7]
    }

    graf = Graf()

    for key, value in fid_for_graf.items():
        graf.add_vertex(key, value)

    graf.first_vertex = station_0

    for i in graf:
        print(i)
