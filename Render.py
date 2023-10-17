from colorama import init, Fore
from SimulationEntity import Grass, Herbivore, Predator, Tree, Rock


init(autoreset=True)


class Render:
    """
    Класс визуализации карты
    """
    def __init__(self, simulation_map):
        self.map = simulation_map

    def render(self):
        """Метод отрисовки карты по __objects_by_coordinates"""
        print("- " * self.map.width)
        for row in range(self.map.height):
            for column in range(self.map.width):
                entity = self.map.get_object((row, column))
                if entity is None:
                    print('*', end=' ')
                else:
                    if isinstance(entity, Grass):
                        print(Fore.GREEN + entity.marking, end=' ')
                    if isinstance(entity, Herbivore):
                        print(Fore.CYAN + entity.marking, end=' ')
                    if isinstance(entity, Predator):
                        print(Fore.RED + entity.marking, end=' ')
                    if isinstance(entity, Tree):
                        print(Fore.YELLOW + entity.marking, end=' ')
                    if isinstance(entity, Rock):
                        print(entity.marking, end=' ')
            print()
        print("- " * self.map.width)
