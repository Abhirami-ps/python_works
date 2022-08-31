from sample.models import frameworks
# print(frameworks)


# python frameworks?
#print([fw.get("name") for fw in frameworks if fw.get("language")=="python"])

"""for fw in frameworks:
    if fw.get("language")=="python":
        print(fw.get("name"))"""



# serverside frameworks
# print([fw.get("name") for fw in frameworks if fw.get("side")=="server"])



# top rating framework
# top_rated_framework=max(frameworks,key=lambda fw:fw.get('rating'))
# print(top_rated_framework)



#least rated framework
# least_rated_framework=min(frameworks,key=lambda fw:fw.get('rating'))
# print(least_rated_framework)




# print frameworks whose rating > 3.5
# print([fw.get('name') for fw in frameworks if fw.get("rating")>3.5])



# sort frameworks based on rating order by desc
# frameworks.sort(key=lambda f:f.get('rating'),reverse=True)
# print(frameworks)




# map language name with number of frameworks


# python:2,java:1,dart:1,typescript:1,javascript:1

