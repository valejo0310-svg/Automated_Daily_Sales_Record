# Products' data input, lists and dictionary

ventas = []

def registrar_ventas():
    
    print("-----Registrar nueva venta -----".center(60))

    amount = int(input("\nPlease indicate how many products are being purchased today: "))

    for i in range(amount):

        product = input("\nIntroduce the product to purchase: ")
        price = float(input("Introduce the price: "))
        quantity = int(input("Introduce how many products are being purchased: "))

        if amount >= 2:
            print("--"*45)

        venta = {
            "producto": product,
            "precio": price,
            "cantidad": quantity
        }

        ventas.append(venta)


# Calculate the total amount
def calcular_total():

    total = 0

    for venta in ventas:
        total += venta["precio"] * venta["cantidad"]

    return total