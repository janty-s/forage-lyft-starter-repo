import unittest
from datetime import date

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


class Test_Nubbin_Battery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2020-20-20")
        last_service_date = date.fromisoformat("2010-10-10")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2020-20-20")
        last_service_date = date.fromisoformat("2010-10-10")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())


class Test_Spindler_Battery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2020-20-20")
        last_service_date = date.fromisoformat("2010-10-10")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2020-20-20")
        last_service_date = date.fromisoformat("2010-10-10")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())