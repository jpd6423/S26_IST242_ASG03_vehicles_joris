from manufacturer import Manufacturer
from auto_model import AutoModel
from sedan import Sedan
from truck import Truck
from garage import Garage

def main():
    f150 = Truck(
            Manufacturer("Ford", "USA"),
            AutoModel("F150", True, list(range(2020,2022))),
            20.0
        )
    tundra = Truck(
            Manufacturer("Toyota", "Japan"),
            AutoModel("Tundra", False, list(range(1987, 1988))),
            30.0,
            is_dually = True
        )
    civic = Sedan(Manufacturer("Honda","Japan"),
                  AutoModel("Civic",False,list(range(1996,1998))),
                  28)
    bmw = Sedan(Manufacturer("BMW","Germany"),
                  AutoModel("M3 Limited",False,list(range(2015,2018))),
                  30)
    
    g = Garage() # empty list is initiated
    g.add_vehicle(f150)
    g.add_vehicle(civic)
    g.add_vehicle(bmw)
    g.add_vehicle(tundra)

    print("Before sorting:")
    print(g,"\n")
    g.sort_by_release_year()
    print("After sorting:")
    print(g)

if __name__ == "__main__":
    main()