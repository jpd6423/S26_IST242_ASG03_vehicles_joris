# This represents a vehicle manufacturer

class Manufacturer:
    # Docstring
    
    # Constructor
    def __init__(self, name: str, country: str):
        self._name = name
        self._country = country

    # Properties
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def country(self) -> str:
        return self._country
    
    # Printing out the manufacturer's objects
    def __str__(self) -> str:
        return f"({self._name}, {self._country})"