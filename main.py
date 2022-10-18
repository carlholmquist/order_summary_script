from script import mailsender
from prettytable import PrettyTable
from prettytable import MSWORD_FRIENDLY
order_summary = {
    "sales_order_number" : "",
    "number_of_skus":0,
    "sku_sleeves" : False,
    "in_house_sleeved" : False,
    "skus" : [],
    "quantity_sleeves": 0,
    "quantity_per_sleeve" : 0,
    "boxes" : []
}

order_summary["sales_order_number"] = input("What is the SO#: ")
sleeved = input("Is this order sleeved in house? (y/n): ")

if sleeved == "y":
    order_summary["in_house_sleeved"] = True
    lids = input("Does this order require lids? (y/n)")
    if lids == "y":
        order_summary["quantity_per_sleeve"] = input("How many lids are there per sleeve?")
        order_summary["quantity_sleeves"] = input("How many sleeves of lids: ")
        order_summary["sku_sleeves"] = True

order_summary["number_of_skus"] = input("How many skus are there: ")

n= 0
while n < int(order_summary["number_of_skus"]):
    order_summary["skus"].append({
        "sku_name" : "",
        "sku_quantity" : 0,
    })
    n += 1

for x in order_summary["skus"]:
    x["sku_name"] = input(f"SKU name: ")
    x["sku_quantity"] = input(f"SKU Quantity: ")
    
if order_summary["in_house_sleeved"] == True:
    box_types = input("how many pallet variations: ")
else:   
    box_types = input("how many box variations: ")
m = 0
while m < int(box_types):
    order_summary["boxes"].append({
        "count" : 0,
        "weight" : 0,
        "width" : 0,
        "depth" : 0,
        "height" : 0
    })
    m += 1
for y in order_summary["boxes"]:
    y["count"] = input("How many boxes in this variation")
    y["weight"] = input("weight")
    y["width"] = input("width")
    y["depth"] = input("depth")
    y["height"] = input("height")

print(f"Hi,\nWe've completed production of SO#{order_summary['sales_order_number']}, counts as follows:")

i = 0
for x in order_summary["skus"]:
    print(f"{x['sku_name']}\tTQ: {x['sku_quantity']}")
    i += 1
i = 0
if order_summary["sku_sleeves"] == True:
    print(f"{order_summary['quantity_sleeves']} sleeves of lids @ {order_summary['quantity_per_sleeve']} lids per sleeve")

print("\nPackaging:")
total_boxes = 0
total_weight = 0
for y in order_summary["boxes"]:
    total_boxes += int(y["count"])
    total_weight += int(y["weight"])*int(y["count"])
    if order_summary["in_house_sleeved"] == True:
        print(f'{y["count"]} pallets\t dim{y["width"]}"x{y["depth"]}"x{y["height"]}" weight {y["weight"]}lbs per pallet')
    else:
        print(f'{y["count"]} boxes\t dim{y["width"]}"x{y["depth"]}"x{y["height"]}" weight {y["weight"]}lbs per box')

print(f"\nTotal amount of boxes is: {total_boxes}")
print(f"Total weight is: {total_weight} lbs")

sku_table = PrettyTable()
sku_table.field_names = ["SKU","Quantity"]

i=0
while i< int(order_summary["number_of_skus"]):
    sku_table.add_row([order_summary["skus"][i]["sku_name"],order_summary["skus"][i]["sku_quantity"]])
    i += 1
sku_table.set_style(MSWORD_FRIENDLY)
print(sku_table)

#mailsender(order_summary)