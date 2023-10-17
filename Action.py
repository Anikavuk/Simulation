import random
from abc import ABC, abstractmethod

from PathFinder import PathFinder
from SimulationEntity import Grass, Rock, Tree, Predator, Herbivore


class Action(ABC):

    def __init__(self, simulation_map):
        self.map = simulation_map
        self.width = simulation_map.width
        self.height = simulation_map.height

    @abstractmethod
    def perform(self):
        """Метод выполнения действия"""
        pass


class GenerationAction(Action):
    """Класс генерации сущностей"""

    def __init__(self, simulation_map):
        super().__init__(simulation_map)

    def random_empty_coordinates(self):
        """Метод возвращает случайные координаты"""
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.map.is_empty((x, y)) is True:
                break
        return x, y

    def generation(self):
        """Метод сохраняет сгенерированные координаты в __objects_by_coordinates"""
        self.map.add_object(self.random_empty_coordinates(), self.create_object())

    def create_object(self):
        """Метод создания сущности"""
        pass

    def perform(self):
        """Метод вызова функции генерации"""
        for quantity in range(self.map.width * self.map.height // 10):
            self.generation()

    def spawn(self):
        pass


class GenerationActionRock(GenerationAction):
    def __init__(self, simulation_map):
        super().__init__(simulation_map)

    def create_object(self):
        """Метод создания сущности"""
        return Rock(self.map)


class GenerationActionTree(GenerationAction):
    def __init__(self, simulation_map):
        super().__init__(simulation_map)

    def create_object(self):
        """Метод создания сущности"""
        return Tree(self.map)


class GenerationActionGrass(GenerationAction):
    def __init__(self, simulation_map):
        super().__init__(simulation_map)

    def create_object(self):
        """Метод создания сущности"""
        return Grass(self.map)

    def spawn(self):
        """Метод реинкарнации травы"""
        if 0 == self.map.counter_object(Grass):
            self.perform()


class GenerationActionHerbivore(GenerationAction):
    def __init__(self, simulation_map):
        super().__init__(simulation_map)

    def create_object(self):
        """Метод создания сущности"""
        return Herbivore(self.map)

    def spawn(self):
        """Пересмотреть метод - при 0 количестве травоядных, симуляция останавливается"""
        if 0 == self.map.counter_object(Herbivore):
            print('Игра закончилась. Всех травоядных поймали и съели:)')


class GenerationActionPredator(GenerationAction):
    def __init__(self, simulation_map):
        super().__init__(simulation_map)

    def create_object(self):
        """Метод создания сущности"""
        return Predator(self.map)


class MoveCreaturesAction(Action):
    def __init__(self, simulation_map, callback):
        super().__init__(simulation_map)
        self.path_finder = PathFinder(simulation_map)
        self.callback = callback

    def perform(self):
        walking_creatures = []
        for row in range(self.map.height):
            for column in range(self.map.width):
                entity = self.map.get_object((row, column))

                if entity not in walking_creatures:
                    walking_creatures.append(entity)
                    if isinstance(entity, Herbivore):
                        way = self.path_finder.find_path((row, column), Grass)
                        # print(f'Травоядный {(row, column)} имеет путь {way}')
                        self.map.move_entity(way[0], way[1])
                        self.callback()
                    elif isinstance(entity, Predator):
                        way = self.path_finder.find_path((row, column), Herbivore)
                        # print(f'Хищник {(row, column)} имеет путь {way}')
                        self.map.move_entity(way[0], way[1])
                        self.callback()
