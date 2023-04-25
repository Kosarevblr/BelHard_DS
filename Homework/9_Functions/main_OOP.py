
from abc import ABC, abstractmethod



class Transport(ABC):
    engine: str
    model: str
    color: str
    age: str
    max_speed: int

    def __init__(self, engine, model, color, age, max_speed):
        self.engine = engine
        self.model = model
        self.color = color
        self.age = age
        self.max_speed = max_speed

    @abstractmethod
    def move(self, distance):
        print(f'я продвинулся на {distance}')

    @abstractmethod
    def stop(self, stopped):
        print(f'Я остановился за {stopped} секунд')


class AirTransport(Transport):
    max_height: int
    seats: int
    wings: bool
    wheels: int

    def __init__(self, engine, model, color, age, max_speed, max_height, seats, wings, wheels):
        super().__init__(engine, model, color, age, max_speed)
        self.max_height = max_height
        self.seats = seats
        self.wings = wings
        self.wheels = wheels

    def fly(self):
        print(f'I can fly')

    def move(self, distance):
        pass

    def stop(self, stopped):
        pass

class GroundTransport(Transport):
    taxi: bool

    def __init__(self, engine, model, color, age, max_speed, taxi):
        super().__init__(engine, model, color, age, max_speed)
        self.taxi = False

    def become_taxi(self):
        self.taxi = True

    def move(self, distance):
        pass

    def stop(self, stopped):
        pass

class WaterTransport(Transport):
    warship: bool

    def __init__(self, engine, model, color, age, max_speed, warship):
        super().__init__(engine, model, color, age, max_speed)
        self.warship = warship

    def up(self):
        print('swim up!')

    def down(self):
        print('go bottom!')

    def move(self, distance):
        pass

    def stop(self, stopped):
        pass

class Helicopter(AirTransport):
    pilot: str
    crew: int

    def __init__(self, engine, model, color, age, max_speed, max_height, seats, wings, wheels, pilot, crew):
        super().__init__(engine, model, color, age, max_speed, max_height, seats, wings, wheels)
        self.pilot = pilot
        self.crew = crew


