import pandas as pd

# Чтение данных из файла
df = pd.read_csv('heats.csv')

# Отбор опоздавших участников
late_comers = df[df['heat'] == 0]

# Вывод опоздавших участников
for index, row in late_comers.iterrows():
    print(f"{row['id']},{index+1},{index+3}")


    
