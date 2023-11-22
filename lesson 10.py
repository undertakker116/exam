import pandas as pd
import random

lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Получаем уникальные категории
categories = data['whoAmI'].unique()

# Для каждой категории создаем столбец и заполняем его
for category in categories:
    data[category] = (data['whoAmI'] == category).astype(int)

print(data.head())


