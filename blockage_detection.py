import pandas as pd
import numpy as np

# Importing data from excel file into python
df = pd.read_excel('C:\\Users\\Z0231633\\OneDrive - ZF Friedrichshafen AG\\Documents\\Pull Complaint Valve Data Pat M\\Fixed Blockages\\Valve #1 50% OV.xlsx')
# Round 'sec' column to the nearest 0.1 second
df['rounded_sec'] = df['sec'].round(decimals=1)

# Group by the rounded_sec and average the measurements in each group
df_avg = df.groupby('rounded_sec').mean()


# Calculating the pressure differnce between each measurement and the next
df['Pressure Difference'] = df['Outlet PSI'].diff()

# Function to check the pressure of the escalating pressure between .7 seconds and 2.3 seconds
def check_pressure_increase(row):
    if .7 < row['sec'] < 2.3:
        diff = row['Pressure Difference']
        value = row['Outlet PSI']
        if 8.7 < diff < 14.51:  
            # allows for a tolerance of 8.7 psi increase each step
            print(f"Pressure still increasing at time {row['sec']}. Current pressure: {value}. Current Pressure Difference: {diff}")
            return True
        elif diff < 8.7 or diff > 14.51:
            print(f"Pressure not increasing enough at time {row['sec']}. Current pressure: {value}. Current Pressure Difference: {diff}")
            return False 
    elif 2.3 < row['sec'] < 2.6:
        value = row['Outlet PSI']
        if 136 < value < 146:
            print (f"Pressure stabalized at time {row['sec']}. Current pressure: {value}")
            return True
        else:
            print (f"Pressure not stabalized at time {row['sec']}. Current pressure: {value}")
            return False
    elif 2.6 < row['sec'] < 2.8:
        diff = row['Pressure Difference']
        value = row['Outlet PSI']
        if 17.4 < diff < 29.01:
            print(f"Pressure decreasing at time {row['sec']}. Current pressure: {value}. Current Pressure Difference: {diff}")
            return True
        elif diff < 17.4 or diff > 29.01:
            print(f"Pressure not decreasing enough or too much at time {row['sec']}. Current pressure: {value}, Current Pressure Difference: {diff}")


# Apply the function to each row in the DataFrame
df.apply(check_pressure_increase, axis=1)
