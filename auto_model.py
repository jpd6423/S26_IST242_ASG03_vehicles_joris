class AutoModel:
    def __init__(
            self,
            name: str,
            in_production: bool,
            years: list[int]):
        if not years:
            raise ValueError("Years list cannot be empty")
        self._name = name 
        self._in_production = in_production
        self._years = list(years) # copy

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def in_production(self) -> str:
        return self._in_production
    
    @property
    def years(self) -> str:
        return list(self._years)
    
    @property
    def first_year(self) -> int:
        return min(self._years)
    
    def __str__(self) -> str:
        return f"{self._name} in production = {self._in_production},  release year: {self._years[0]}"
    
    