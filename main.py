from time import sleep
from Calculator import sales_record
from Show_message import show_record 



#Function main used to call all the other fuctions 
def main():

    welcome = """
╔════════════════════════════════════════════════════════════╗
        WELCOME TO THE SALES RECORD, RIWI STORE!!
╚════════════════════════════════════════════════════════════╝
"""

    for i in welcome:
        print(i, end="", flush=True)
        sleep(0.0005)

#Loop while to make a confirmation for the sell
    continuar = "si"

    while continuar.lower() == "si":
        sales_record()
        continuar = input("Do you want to register this new sell? (s/n): ")
        if continuar == "si":
            show_record()
        else: 
            print ("Sell canceled.")
            exit()


main()