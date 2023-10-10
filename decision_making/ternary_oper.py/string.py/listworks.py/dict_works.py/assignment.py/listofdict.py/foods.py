foods=[
    {"id":1,"name":"ghee-roast","price":70,"category":"veg"},
    {"id":2,"name":"chicken-roast","price":170,"category":"non-veg"},
    {"id":3,"name":"cb","price":170,"category":"non-veg"},
    {"id":4,"name":"bb","price":190,"category":"non-veg"},
    {"id":5,"name":"fried-rice","price":140,"category":"veg"},
    {"id":6,"name":"chicken-friedrice","price":170,"category":"non-veg"},
    {"id":7,"name":"nan","price":70,"category":"veg"},
    {"id":8,"name":"alfam","price":370,"category":"non-veg"},
]

#total_number=[i.get("id") for i in foods]
#print(total_number)
print(len(foods))


#category_veg=[i.get("name")for i in foods if i.get ("category")=="veg"]
#print(category_veg)

#food_names=[i.get("name")for i in foods if i.get("price")<100]
#print(food_names)

#costly_product=max(foods,key=lambda i:i.get("price"))
#print(costly_product)

non_vegfoods=[f for f in foods if f.get("category")=="non-veg"]
costly_nonveg=max(non_vegfoods,key=lambda f:f.get("price"))
print(costly_nonveg)


categories={f.get("category") for f in foods}
print(categories)
