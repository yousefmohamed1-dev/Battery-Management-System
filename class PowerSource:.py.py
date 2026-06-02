class PowerSource:
    def __init__(self):
        self.type = "Electrical"

class LithiumBattery(PowerSource):
    def __init__(self, capacity, percentage, charging_state):
        super().__init__()
        self.capacity = capacity
        self.percentage = percentage
        self.charging_state = charging_state

    def charge(self, minutes):
        counter = 0
        while counter < minutes:
            if self.percentage >= 100:
                self.percentage = 100
                break
            self.percentage += 1
            counter += 1

        return f"Charging finished. Current Percentage: {self.percentage}%"

my_battery = LithiumBattery(5000, 85, "Charging")
print(my_battery.charge(20))