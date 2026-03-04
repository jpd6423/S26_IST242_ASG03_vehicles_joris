from vehicle import Vehicle

class Garage:
    # A garage stores the vehicles

    # constructor is initializing an empty list
    def __init__(self):
        self._vehicles: list[Vehicle] = []

    # getter
    # returns a copy of the internal list
    @property
    def vehicles(self) -> list[Vehicle]:
        return list(self._vehicles)

    # adding a vehicle to the list
    def add_vehicle(self, vehicle: Vehicle):
        self._vehicles.append(vehicle)

    # clears garage of vehicles
    def empty_garage(self):
        self._vehicles.clear()

    def sort_by_release_year(self):
        self._vehicles.sort()

    # returns each vehicle as a new line
    def __str__(self) -> str:
        return "\n".join(str(v) for v in self._vehicles) # str1.join(str2)