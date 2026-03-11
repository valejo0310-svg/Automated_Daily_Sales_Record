from Calculator import calculate_total, sells
#Show the record of the purchase
def show_record():

    print("="*60)
    print("TOTAL PURCHASE".center(60))
    print("="*60)
#This part allows all that was added on the dictionary be shown here

    for sell in sells:
        print("Product:", sell["product"])
        print("Quantity sold:", sell["quantity"])
        
    total = calculate_total()
    print("Final amount: $", total)