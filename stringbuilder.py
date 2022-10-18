def stringbuilder(order_summary):

    message = f"Hi,\n\nWe've completed production of SO#{order_summary['sales_order_number']}, counts as follows:\n"

    i = 0
    for x in order_summary["skus"]:
        message += f"{x['sku_name']}\tTQ: {x['sku_quantity']}\n"
        i += 1
    i = 0
    if order_summary["sku_sleeves"] == True:
        message += f"{order_summary['quantity_sleeves']} sleeves of lids @ {order_summary['quantity_per_sleeve']} lids per sleeve\n"

    message += "\nPackaging:\n"
    total_boxes = 0
    total_weight = 0
    for y in order_summary["boxes"]:
        total_boxes += int(y["count"])
        total_weight += int(y["weight"])*int(y["count"])
        if order_summary["in_house_sleeved"] == True:
            message += f'{y["count"]} pallets\t dim{y["width"]}"x{y["depth"]}"x{y["height"]}" weight {y["weight"]} lbs per pallet\n'
        else:
            message += f'{y["count"]} boxes\t dim{y["width"]}"x{y["depth"]}"x{y["height"]}" weight {y["weight"]} lbs per box\n'

    message += f"\nTotal amount of boxes is: {total_boxes}\n"
    message += f"Total weight is: {total_weight} lbs"

    return message