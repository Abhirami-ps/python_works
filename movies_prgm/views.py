from json import load

with open("movies.json",encoding="UTF-8") as f:
    data=load(f)

print(len(data))




genres_names=[c.get('genres') for c in data]

unique_genres_names=[]
for i in genres_names:
    if i not in unique_genres_names:
        unique_genres_names.append(i)
print(unique_genres_names)







movies_released_in_2015=[c.get('title') for c in data if c.get('year')==2015]
print(movies_released_in_2015)







