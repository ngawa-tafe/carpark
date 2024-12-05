from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime
import json


class CarPark:
    def __init__(self, location='unknown', capacity=100, plates=None, sensors=None, displays=None,
                 log_file=Path("log.txt"), config_file=Path("config.json")):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        self.log_file.touch(exist_ok=True)
        self.config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        self.config_file.touch(exist_ok=True)

    def __str__(self):
        return f"Location: {self.location}, Capacity: {self.capacity}"

    def register(self, component):
        """

        registers a component to car park by appending to a list of sensors or displays,
        raises error if component is not an instance of Sensor or Display class.
        :param component: Any
        :return: null
        """

        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        else:
            if isinstance(component, Sensor):
                self.sensors.append(component)
            else:
                self.displays.append(component)

    def update_displays(self):
        """

        updates the display to display available bays and temperature.
        :return: null
        """
        data = {"available_bays": self.available_bays, "temperature": 25}
        for display in self.displays:
            display.update(data)

    def add_car(self, plate):
        """

        Adds a plate to the list of plates, updates display and logs car activity.
        :param plate: str
        :return: null
        """
        self.plates.append(plate)
        self.update_displays()
        self._log_car_activity(plate, "entered")

    def remove_car(self, plate):
        """

        Removes a plate to the list of plates, updates display and logs car activity.
        :param plate:
        :return: str
        """
        self.plates.remove(plate)
        self.update_displays()
        self._log_car_activity(plate, "exited")

    @property
    def available_bays(self):
        if self.capacity - len(self.plates) < 0:
            return 0
        else:
            return self.capacity - len(self.plates)

    def _log_car_activity(self, plate, action):
        """

        logs a car activity with plate, action and datetime information.
        :param plate: str,
        :param action: str
        :return: null
        """
        with self.log_file.open("a") as log_file:
            log_file.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")

    def write_config(self):
        """
        writes the config file to disk.
        :return: null
        """
        with self.config_file.open("w") as config_file:
            json.dump({"location": self.location,
                       "capacity": self.capacity,
                       "log_file": str(self.log_file)}, config_file)

    @classmethod
    def from_config(cls, config_file=Path("config.json")):
        """
        Reads the config file and returns a configured class.
        :param config_file: pathlib.Path
        :return: CarPark
        """
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as f:
            config = json.load(f)
        return cls(config["location"], config["capacity"], log_file=config["log_file"])
