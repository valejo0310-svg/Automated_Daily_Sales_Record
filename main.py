from time import sleep
from Calculator import registrar_ventas
from Show_message import mostrar_resumen




def main():

    welcome = """
╔════════════════════════════════════════════════════════════╗
        WELCOME TO THE SALES RECORD RIWI STORE!!
╚════════════════════════════════════════════════════════════╝
"""

    for i in welcome:
        print(i, end="", flush=True)
        sleep(0.0005)


    continuar = "s"

    while continuar.lower() == "s":
        registrar_ventas()
        continuar = input("¿Desea registrar otra venta? (s/n): ")

    mostrar_resumen()


main()