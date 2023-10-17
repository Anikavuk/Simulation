class SimulationEntity:

    def __init__(self, simulation_map):
        self.map = simulation_map
        self.counter = 0


class Creature(SimulationEntity):

    def __init__(self, simulation_map):
        super().__init__(simulation_map)


class Herbivore(Creature):
    """Класс травоядных существ"""

    def __init__(self, simulation_map):
        super().__init__(simulation_map)
        self.marking = 'H'


class Predator(Creature):
    """Класс хищников"""

    def __init__(self, simulation_map):
        super().__init__(simulation_map)
        self.marking = 'P'


class Tree(SimulationEntity):
    """Класс дерева"""

    def __init__(self, simulation_map):
        super().__init__(simulation_map)
        self.marking = 'T'


class Rock(SimulationEntity):
    """Класс камня"""

    def __init__(self, simulation_map):
        super().__init__(simulation_map)
        self.marking = 'R'


class Grass(SimulationEntity):
    """Класс травы"""

    def __init__(self, simulation_map):
        super().__init__(simulation_map)
        self.marking = 'G'
