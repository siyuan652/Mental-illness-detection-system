import pandas as pd

read_file = pd.read_excel (r'C:\Users\Admin\Desktop\AIROST\Data Gait table.xlsx')
read_file.to_csv (r'C:\Users\Admin\Desktop\AIROST\Data Gait table.csv', index = None, header = True)