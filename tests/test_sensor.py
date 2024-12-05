import unittest
from sensor import EntrySensor, ExitSensor
from car_park import CarPark


class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark()
        self.entry_sensor = EntrySensor(id=1, car_park=self.car_park, is_active=True)
        self.exit_sensor = ExitSensor(id=2, car_park=self.car_park, is_active=True)

    def test_entry_sensor_initialized_with_all_attributes(self):
        self.assertEqual(self.entry_sensor.id, 1)
        self.assertIsInstance(self.entry_sensor.car_park, CarPark)
        self.assertTrue(self.entry_sensor.is_active)

    def test_exit_sensor_initialized_with_all_attributes(self):
        self.assertEqual(self.exit_sensor.id, 2)
        self.assertIsInstance(self.exit_sensor.car_park, CarPark)
        self.assertTrue(self.exit_sensor.is_active)

    def test_entry_sensor_detect_vehicle_method(self):
        self.entry_sensor.detect_vehicle()

        self.assertEqual(1, len(self.car_park.plates))

    def test_exit_sensor_detect_vehicle_method(self):
        self.entry_sensor.detect_vehicle()
        number_of_cars = len(self.car_park.plates)

        self.exit_sensor.detect_vehicle()

        self.assertEqual(number_of_cars - 1, len(self.car_park.plates))


if __name__ == "__main__":
    unittest.main()
