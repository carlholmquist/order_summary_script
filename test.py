order_summary = {
    "sales_order_number" : "152345",
    "number_of_skus":2,
    "skus" : [
        {
            "sku_name" : "Chameleon Black",
            "sku_quantity" : 20000,
            "sku_sleeves" : False,
            "quantity_sleeves": 0,
            "quantity_per_sleeve" : 0,
        },
        {
            "sku_name" : "Chameleon Vanilla",
            "sku_quantity" : 30000,
            "sku_sleeves" : False,
            "quantity_sleeves": 0,
            "quantity_per_sleeve" : 0,
        }
    ],
}

for x in order_summary["skus"]:
    x["sku_name"] = input("change name: ")

print(order_summary["skus"])