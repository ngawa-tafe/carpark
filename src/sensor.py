import random
from abc import ABC, abstractmethod


class Sensor(ABC):
    def __init__(self, id, car_park, is_active=False):
        self.id = id
        self.car_park = car_park
        self.is_active = is_active

    def __str__(self):
        return f'{self.id}: {self.is_active}'

    @abstractmethod
    def update_car_park(self, plate):
        ...

    def _scan_plate(self):
        """

        returns a random number plate with format FAke-000
        :return: str
        """
        return 'Fake-' + format(random.randint(0, 999), "03d")

    def detect_vehicle(self):
        """

        scans a plate and updates the car park.
        :return: null
        """
        plate = self._scan_plate()
        self.update_car_park(plate)


class EntrySensor(Sensor):
    def update_car_park(self, plate):
        """

        Adds a car to the car park and prints a message.
        :param plate: str
        :return: null
        """
        self.car_park.add_car(plate)
        print(f"Incoming vehicle detected. Plate: {plate}")


class ExitSensor(Sensor):
    def update_car_park(self, plate):
        """
        Removes a car from the car park and prints a message.
        :param plate: str
        :return: null
        """
        self.car_park.remove_car(plate)
        print(f"Outgoing vehicle detected. Plate: {plate}")

    def _scan_plate(self):
        """

        returns a random plate from the car park's list of plates.
        :return: str
        """
        return random.choice(self.car_park.plates)
