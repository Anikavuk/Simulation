from Simulation import Simulation


def main():
    print('Добро пожаловать в страну Matrix2077!')
    print('Мир травоядных и хищников')

    height = int(input('Введите количество рядов карты: '))
    width = int(input('Введите количество колонок карты: '))

    simulation = Simulation(width, height)
    simulation.start()


if __name__ == "__main__":
    main()
