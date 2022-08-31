from json import load

with open("countrydata.json",encoding="UTF-8") as f:
    data=load(f)
print(len(data))


all_country_names=[c.get("name") for c in data]
print(all_country_names)


def get_country_details(name):
    return [c for c in data if c.get("name")==name][0]
details=get_country_details("India")
print(details)




def curr(name):
    return [c.get('currencies')[0].get("name") for c in data if c.get("name")==name][0]
currency=curr("Pakistan")
print(currency)




def get_country_capital(name):
    c_data=get_country_details(name)
    if c_data:
        return c_data.get("capital")
print(get_country_capital("Pakistan"))


def get_capital(name):
    return [c.get("capital") for c in data if c.get("name")==name][0]
print(get_capital("India"))






def get_country_population(name):
    c_data=get_country_details(name)
    if c_data:
        return c_data.get("population")
print(get_country_population("India"))

def get_population(name):
    return [c.get("population") for c in data if c.get("name")==name][0]
print(get_population("India"))
#
#
#
#

def get_country_languages(name):
    c_data=get_country_details(name)
    return [ l.get("name")for l in c_data.get("languages")]
print(get_country_languages("India"))


#
#
"""def get_country_currencyname(name):
    c_data=get_country_details(name)
    if c_data:
        return c_data.get("currencies")[0].get("name")
print(get_country_currencyname("India"))
#
#
#
#
#
# border shared countries--afghanistan-borders--country name
def get_country_border_list_names(name):
    c_data=get_country_details(name)
    border_list=c_data.get("borders")
    b_names=[c.get("name") for c in data if c.get("alpha3Code") in border_list]
    return b_names

print(get_country_border_list_names("India"))





def get_max_populated_country():
    c_data=max(data,key=lambda c:c.get("population"))
    return c_data.get('name')
print(get_max_populated_country())




def get_min_populated_country():
    c_data=min(data,key=lambda c:c.get("population"))
    return c_data.get('name')
print(get_min_populated_country())



max_populated_country=max(data,key=lambda c:c.get("population"))
print(max_populated_country)"""

