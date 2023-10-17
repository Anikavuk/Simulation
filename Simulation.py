import os
import time

from Action import GenerationActionTree, \
                   GenerationActionRock, \
                   GenerationActionGrass, \
                   GenerationActionHerbivore, \
                   GenerationActionPredator,\
                   MoveCreaturesAction
from Map import Map
from Render import Render
from SimulationEntity import Herbivore, Grass


class Simulation:
    def __init__(self, width, height):
        self.map = Map(width, height)
        self.render = Render(self.map)

        self.__init_gen__actions()
        self.__init_turn_actions()

        self.days = 0

    def __init_gen__actions(self):
        self.__gen_actions = [
            GenerationActionTree(self.map),
            GenerationActionRock(self.map),
            GenerationActionGrass(self.map),
            GenerationActionHerbivore(self.map),
            GenerationActionPredator(self.map)
        ]

    def __init_turn_actions(self):
        self.__turn_actions = [
            MoveCreaturesAction(
                self.map,
                lambda: self.__render_map()
            )
        ]

    def start(self):
        for action in self.__gen_actions:
            action.perform()

        self.__start_simulation_loop()

    def __start_simulation_loop(self):
        """
        Запуск жизни симуляции
        """

        self.__render_map()

        while True:
            self.days += 1

            for action in self.__turn_actions:
                action.perform()

            if self.map.counter_object(Herbivore) == 0:
                print('Game over')
                break

            self.__render_map()

    def __render_map(self):
        os.system('cls')

        print(f'Симуляция живет {self.days} день')
        print(f'Всего травоядных {self.map.counter_object(Herbivore)} штук')
        print(f'Всего травы {self.map.counter_object(Grass)} штук')
        self.render.render()

        time.sleep(0.5)
