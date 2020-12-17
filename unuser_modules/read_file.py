import pandas as pd

data = pd.read_csv('/home/bohdanm/Documents/mini_project_first_semester/sources/author/titles.csv')
# print(list(data.columns))
# print(data.columns)
# print(data[['Title', 'Type of resource']])
# print(set(data['Type of resource']))
# certain_type = data.loc[data['Type of resource'] == 'Monograph']

# print(certain_type)
# print(list(data.columns))
print(set(data['Languages']))

