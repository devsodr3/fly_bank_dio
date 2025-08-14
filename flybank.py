
def depositar(account):
    valor = float(input(f"\ndigite o valor de deseja para depositar: "))
    if valor < 0: 
        print("\nvalor para deposito invalido")
        return
        
    account["extrato"].append(valor)
    account["saldo"] += valor


def sacar(account):
    valor = float(input(f"\ndigite o valor de deseja para sacar: "))

    err = ["Saldo insuficiente \n" if valor > account["saldo"] else None,
           "Limite de saque excedido \n" if valor > account["limite_por_saque"] else None,
           "Quantidade de saques excedida \n" if account["saques_restantes"] <= 0 else None
        ]
    for errmsg in err: 
        if errmsg: 
            print(errmsg)
            return

    account["saldo"] -= valor
    account["saques_restantes"] -= 1
    account["extrato"].append(-valor)


def extrato(account):
    print("\nimprimindo seu extrato")
    for movimentation in account["extrato"]:
        print(format_number(movimentation))
    print(format_number(account["saldo"]))


def display_hub():
    options = ["depositar", "sacar", "extrato"]
    print(
        f"""Escolha sua operação:
    1 - {options[0]}
    2 - {options[1]}
    3 - {options[2]}
    4 - encerrar\n"""
        )
    return int(input()) - 1

account = {"saldo": 0, "extrato": [], "limite_por_saque": 500, "saques_restantes": 3}
actions = [depositar, sacar, extrato]


def format_number(number: float):
    return f"R${number:.2f}"

def main():
    option = display_hub()
    if option != 3:
        actions[option](account=account)
        main()



main()