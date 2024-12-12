import re


def validar_email(email):
    padrao_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]"
    return re.match(padrao_email, email) is not None


def validar_senha(senha):
    if (
        len(senha) >= 8
        and re.search(r"[A-Z]", senha)
        and re.search(r"[a-z]", senha)
        and re.search(r"[0-9]", senha)
    ):
        return True
    return False


def validar_senha_erro(senha):
    if (
        len(senha) >= 8
        and re.search(r"[A-Z]", senha)
        and re.search(r"[a-z]", senha)
        and re.search(r"[0-9]", senha)
    ):
        return True
    return False


def criar_conta(email, senha):
    if not validar_email(email):
        return "E-mail inválido."

    if not validar_senha(senha):
        return "Senha inválida."

    return "Conta criada"


if __name__ == "__main__":
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")
    print(criar_conta(email, senha))
