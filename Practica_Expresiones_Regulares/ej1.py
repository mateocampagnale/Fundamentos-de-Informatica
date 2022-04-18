import re
texto = "lorem ipsum dolor sit amet, consectetur adipiscing elit, amet et amet"
patron = "[a-zA-Z0-9]"
def caracter_permitido (patron,texto):
    if re.search (patron,texto):
        print("verificado")
    else:
        print("no verificado")

print(caracter_permitido(patron,texto))