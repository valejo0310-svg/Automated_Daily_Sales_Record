# Products' data input, lists and dictionary
sells = []

def sales_record():
    
    print("-----ADD A NEW PURCHASE -----".center(60))

    amount = input("\nDo you wish to add new purchases? (s/n): ")

    while amount.lower() in ["s" , "si"]:

        product = input("\nIntroduce the product to purchase: ")
        price = float(input("Introduce the price: "))
        quantity = float(input("Introduce how many products are being purchased: "))
        print("--"*45)

        sell = {
            "product": product,
            "price": price,
            "quantity": quantity,

        }

        sells.append(sell)
        
        amount = input("Do you wish to add another product? (s/n): ")

# Calculate the total amount
def calculate_total():

    total = 0

    for sell in sells:
        total += sell["price"] * sell["quantity"]

    return total