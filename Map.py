class Map:
    def __init__(self, width, height):
        """
        Принимает ширину и высоту карты
        :param __objects_by_coordinates: Словарь хранения ключ - координаты, значение - объект сущности
        """
        self.width = width
        self.height = height
        self.__objects_by_coordinates = {}

    def add_object(self, coords, entity):
        """Сохранение объекта и его координаты в словаре __objects_by_coordinates"""
        if coords is not None:
            self.__objects_by_coordinates[coords] = entity

    def del_object(self, coords):
        """Функция для удаления объекта по заданным координатам"""
        self.__objects_by_coordinates.pop(coords)

    def is_empty(self, coords):
        """Функция проверка координат на наличие на этих координатах объекта"""
        if coords not in self.__objects_by_coordinates:
            return True
        else:
            return False

    def get_object(self, coords) -> object:
        """Функция возвращает объект по координатам"""
        if not self.is_empty(coords):
            return self.__objects_by_coordinates[coords]

        return None

    def show_dictionary(self):
        """Метод, который показывает содержимое в __objects_by_coordinates"""
        return self.__objects_by_coordinates

    def counter_object(self, train_class):
        """Счетчик сущностей одного вида"""
        counter = 0
        for value in self.__objects_by_coordinates.values():
            if isinstance(value, train_class):
                counter += 1
        return counter

    def move_entity(self, old_coord, new_coord):
        """
        Метод перемещения существа с одной координаты на другую на 1 клетку
        :param old_coord - from
        :param new_coord - to
        """
        self.add_object(new_coord, self.get_object(old_coord))
        self.del_object(old_coord)
