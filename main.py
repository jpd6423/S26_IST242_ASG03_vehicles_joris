from manufacturer import Manufacturer
from auto_model import AutoModel

def main():
    original_list = [2020, 2021]
    am = AutoModel("F150", True, original_list)

    print(am)
    pass

if __name__ == "__main__":
    main()