from abc import ABC, abstractmethod
import logging

# Налаштування логування
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


# 1. Абстрактний базовий клас Vehicle
class Vehicle(ABC):
    def __init__(self, make, model, spec):
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self):
        pass


# 2. Модифіковані класи Car та Motorcycle
class Car(Vehicle):
    def start_engine(self):
        logger.info(f"{self.make} {self.model} ({self.spec} Spec): Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self):
        logger.info(f"{self.make} {self.model} ({self.spec} Spec): Мотор заведено")


# 3. Абстрактний клас VehicleFactory
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make, model) -> Motorcycle:
        pass


# 4. Реалізація фабрик для США та ЄС
class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model) -> Car:
        return Car(make, model, "US")

    def create_motorcycle(self, make, model) -> Motorcycle:
        return Motorcycle(make, model, "US")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model) -> Car:
        return Car(make, model, "EU")

    def create_motorcycle(self, make, model) -> Motorcycle:
        return Motorcycle(make, model, "EU")


# 5. Код для використання фабрик
if __name__ == "__main__":
    # Фабрика для США
    us_factory = USVehicleFactory()
    us_car = us_factory.create_car("Ford", "Mustang")
    us_motorcycle = us_factory.create_motorcycle("Harley-Davidson", "Sportster")

    us_car.start_engine()
    us_motorcycle.start_engine()

    # Фабрика для ЄС
    eu_factory = EUVehicleFactory()
    eu_car = eu_factory.create_car("BMW", "320i")
    eu_motorcycle = eu_factory.create_motorcycle("Ducati", "Panigale V4")

    eu_car.start_engine()
    eu_motorcycle.start_engine()
