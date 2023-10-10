items=[
    {"id":1,"name":"sugar","price":40,"avl_qty":10},
    {"id":2,"name":"milk","price":45,"avl_qty":20},
    {"id":3,"name":"teapowder","price":30,"avl_qty":30},
    {"id":4,"name":"tomato","price":140,"avl_qty":40},
    {"id":5,"name":"potato","price":40,"avl_qty":50},
   
]

#all_product_names=[i.get("name") for i in items]
#print(all_product_names)

#in_stock_products=[ i.get("name") for i in items if i.get("avl_qty")>0 ]
#print(in_stock_products)

#price_filter=[ i.get("name") for i in items if i.get("price")>=50 ]
#print(price_filter)
range_filter=[i.get("name") for i in items if i.get("price") in range(20,51)]
print(range_filter)

#costly_product=max(items,key=lambda i:i.get("price"))
#print(costly_product)

#product_sort=sorted(items,reverse=True,key=lambda i:i.get("avl_qty"))
#print(product_sort)

