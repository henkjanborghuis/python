class Car():
    def __init__(self, color, fuel_remaining, **kwargs):
        self.laps = 0
        self.color = color
        self.fuel_remaining = fuel_remaining

        for key, value in kwargs.items():
            setattr(self, key, value)


class RaceCar(Car):
    def __init__(self, color, fuel_remaining, turbo = True, **kwargs):
        super().__init__(color, fuel_remaining, **kwargs)
        self.turbo = turbo
        
    def run_lap(self, length):
        self.fuel_remaining = self.fuel_remaining - length * 0.125
        self.laps +=1
