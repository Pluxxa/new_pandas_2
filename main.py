import pandas as pd

data = {
    'Names' : ['Анна', 'Мария', 'Игорь', 'Виктор', 'Иван', 'Марат', 'Кирилл', 'Ольга', 'Василий', 'Николай'],
    'Mathematics' : [5, 4, 3, 4, 5, 3, 4, 5, 4, 3],
    'Geography' : [5, 5, 4, 5, 4, 4, 5, 4, 3, 4],
    'Biology' : [4, 5, 5, 4, 4, 5, 4, 4, 5, 5],
    'Literature' : [5, 3, 3, 4, 4, 3, 3, 4, 5, 4],
    'History' : [5, 5, 4, 4, 5, 4, 3, 3, 5, 4]
}

df = pd.DataFrame(data)
print(df.head())
print()
for i in df:
    if i == 'Names':
        continue
    else:
        print(f"Средняя оценка по предмету {i} - {df[i].mean()}")
print()
for i in df:
    if i == 'Names':
        continue
    else:
        print(f"Медианная оценка по предмету {i} - {df[i].median()}")

Q1 = df['Mathematics'].quantile(0.25)
Q3 = df['Mathematics'].quantile(0.75)
IQR = Q3 - Q1
print()
print(f"Стандартное отклонение оценок по Mathematics - {df['Mathematics'].std()}")