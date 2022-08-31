# from products.models import bikes

# list
# detail
# update
# create
# remove
# class Bikes:
#     def list(self,*args,**kwargs):
#         return bikes
#
#     def retrieve(self,*args,**kwargs):
#         code=kwargs.get("code")
#         bike=[b for b in bikes if b.get("code")==code]
#         return bike
#     def create(self,*args,**kwargs):
#         bike=kwargs.get("data")
#         bikes.append(bike)
#         return bike
#     def update(self,*args,**kwargs):
#         code=kwargs.get("code")
#         data=kwargs.get("data")
#         instance=[b for b in bikes if b.get("code")==code][0]
#         instance.update(data)
#         return instance
#     def destroy(self,*args,**kwargs):
#         code=kwargs.get("code")
#         instance=[b for b in bikes if b.get('code')==code][0]
#         bikes.remove(instance)
#         return instance
#
#
# b=Bikes()
# print(b.list())
# print(b.retrieve(code=1002))
# data={"code": 1006, "name": "ray",
#       "colors": ["red","white"],
#       "price": 100000, "brand": "yamaha",
#       "fuel_type": "petrol"}
# print(b.create(data=data))
# print(b.list())

# print(b.retrieve(code=1002))
# data={"code": 1002, "name": "hynes", "colors": ["red", "blue", "grey","white"], "price": 260000, "brand": "honda","fuel_type": "petrol"}
# code=1002
# print(b.update(code=1002,data=data))

# print(b.destroy(code=1002))
# print(b.list())




# from products.models import items
# class Items:
    # def list(self,*args,**kwargs):
    #     return items


    # def retrieve(self, *args, **kwargs):
    #     id=kwargs.get("id")
    #     item=[b for b in items if b.get("id")==id]
    #     return item

    # def create(self, *args, **kwargs):
    #     item=kwargs.get("data")
    #     items.append(item)
    #     return item

    # def update(self, *args, **kwargs):
    #     id=kwargs.get("id")
    #     data=kwargs.get("data")
    #     instance=[b for b in items if b.get("id")==id][0]
    #     instance.update(data)
    #     return instance

    # def destroy(self, *args, **kwargs):
    #     id=kwargs.get("id")
    #     instance=[b for b in items if b.get('id')==id][0]
    #     items.remove(instance)
    #     return instance

# b=Items()
# print(b.list())
# print(b.retrieve(id=5))
# data=  {
#     "id": 21,
#     "title": "Raven - Foldsack No. 1 Backpack, Fits 15 Laptops",
#     "price": 110.95,
#     "description": "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday",
#     "category": "women's clothing",
#     "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg",
#     "rating": {
#       "rate": 4.5,
#       "count": 100
#     }
#   }
# print(b.create(data=data))
# print(b.list())


# print(b.retrieve(id=2))
# data=  {
#     "id": 2,
#     "title": "Mens Casual Premium Slim Fit T-Shirts ",
#     "price": 25,
#     "description": "Slim-fitting style, contrast raglan long sleeve, three-button henley placket, light weight & soft fabric for breathable and comfortable wearing. And Solid stitched shirts with round neck made for durability and a great fit for casual fashion wear and diehard baseball fans. The Henley style round neckline includes a three-button placket.",
#     "category": "men's clothing",
#     "image": "https://fakestoreapi.com/img/71-3HjGNDUL._AC_SY879._SX._UX._SY._UY_.jpg",
#     "rating": {
#       "rate": 4.5,
#       "count": 259
#     }
#   }
# id=2
# print(b.update(id=2,data=data))

# print(b.destroy(id=3))
# print(b.list())