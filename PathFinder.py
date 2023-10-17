class PathFinder:
    """Класс поиска пути"""

    def __init__(self, simulation_map):
        """
        :param simulation_map: объект класса Map
        :param node_list: список координат карты
        """

        self.map = simulation_map
        self.node_list = [[(row, col) for col in range(self.map.width)] for row in
                          range(self.map.height)]

    def adjacent_cells(self, coord):
        """
        Метод поиска координат соседних клеток
        :param coord: точка координаты, у которой надо найти соседей
        :return список координат соседних клеток от точки в coord
        """
        vertexes = []
        for column in range(-1, 2):
            for row in range(-1, 2):
                if abs(column) != abs(row) and coord[0] != coord[0] - column or coord[1] != coord[1] - row:
                    if len(self.node_list[0]) > coord[1] - row >= 0 and len(self.node_list) > coord[
                        0] - column >= 0:
                        vertexes.append(self.node_list[coord[0] - column][coord[1] - row])
        return vertexes

    def find_path(self, start, target_class):
        """
       Метод поиска пути
       :param start: точка, от которой начинается поиск жертвы
       :param target_class: объект класса (травы или травоядного), который надо найти
       :return список координат, по которому можно добраться к target_class
       """
        new_path = []
        queue = []  # очередь
        visited = set()  # посещенные вершины
        queue.append([start])
        while queue:
            path = queue.pop(0)  # достаем из очереди первый элемент пути
            path_last_node = path[-1]  # берем последний элемент
            for adjacent_cell in self.adjacent_cells(path_last_node):  # ищем соседей
                if adjacent_cell not in visited:
                    visited.add(adjacent_cell)
                    if isinstance(self.map.get_object(adjacent_cell), target_class):
                        path.append(adjacent_cell)
                        return path
                    if self.map.is_empty(adjacent_cell):  # если координата пустая
                        new_path = list(path)  # clone path
                        new_path.append(adjacent_cell)
                        queue.append(new_path)
        return new_path
