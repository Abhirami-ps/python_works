from json import load

with open("bikes.json") as f:
    data=load(f)

print(data)

# bike_names=[bike.get("name") for bike in data ]
# print(bike_names)


# costly_bike=max(data,key=lambda b:b.get("price"))
# print(costly_bike)


# red colored bike
# red_bike=[bike.get("name") for bike in data if "red" in bike.get("colors")]
# print(red_bike)


# tvs bikes
# tvs_bike=[bike for bike in data if bike.get("brand")=="tvs"]
# print(tvs_bike)



