
from config import OUTLET_PSI_RANGES
from test import TEST_PSI_RANGES
import pandas as pd

def check_psi(focus, range):
    print(focus, range)
    
    l, h = range[0], range[1]
    
    if focus >= l and focus <= h:
        print(f"good")
    elif focus < l:
        print(f"Too low")
    elif focus > h:
        print(f"Too high")
    else:
        print(f"Error")
...
def analyze_file(filepath):
    data = pd.read_excel(filepath)  # Use Pandas to read the Excel file
    feedback = ""

    for key in TEST_PSI_RANGES:
        if key in OUTLET_PSI_RANGES:
            focus = TEST_PSI_RANGES[key]
            result = check_psi(focus, OUTLET_PSI_RANGES[key])
            feedback += f"Key: {key}, Result: {result}\n"

    return feedback
...

if __name__ == "__main__":
    file = input("Enter file name: ")
    
    print("This is the main function.")
    for key in TEST_PSI_RANGES:
        if key in OUTLET_PSI_RANGES:
            focus = TEST_PSI_RANGES[key]
            check_psi(focus, OUTLET_PSI_RANGES[key])
            
        
        # check_psi(list(OUTLET_PSI_RANGES.keys())[i], list(OUTLET_PSI_RANGES.values())[i])
