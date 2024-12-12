# case 1: todos corretos
# case 2: erro em algum validador
# case 3: erro na integração


from case_3 import (
    criar_conta,
    validar_email,
    validar_senha,
)


def testar_validar_email():
    assert (
        validar_email("teste@exemplo.com") == True
    ), "Teste falhou: e-mail válido não foi aceito."
    assert (
        validar_email("teste.exemplo@dominio.org") == True
    ), "Teste falhou: e-mail válido não foi aceito."
    assert (
        validar_email("teste@dominio") == False
    ), "Teste falhou: e-mail sem domínio não foi rejeitado."
    assert (
        validar_email("teste@.com") == False
    ), "Teste falhou: e-mail inválido não foi rejeitado."
    assert (
        validar_email("@exemplo.com") == False
    ), "Teste falhou: e-mail sem parte local não foi rejeitado."
    print("Todos os testes de validar_email passaram.")


def testar_validar_senha():
    assert (
        validar_senha("Senha123") == True
    ), "Teste falhou: senha válida não foi aceita."
    assert (
        validar_senha("senha123") == False
    ), "Teste falhou: senha sem letra maiúscula não foi rejeitada."
    assert (
        validar_senha("SENHA123") == False
    ), "Teste falhou: senha sem letra minúscula não foi rejeitada."
    assert (
        validar_senha("Senha!") == False
    ), "Teste falhou: senha sem número não foi rejeitada."
    assert (
        validar_senha("12345678") == False
    ), "Teste falhou: senha sem letras não foi rejeitada."
    print("Todos os testes de validar_senha passaram.")


def testar_criar_conta():
    assert (
        criar_conta("teste@exemplo.com", "Senha123") == "Conta criada"
    ), "Teste falhou: conta válida não foi criada."
    assert (
        criar_conta("teste@dominio", "Senha123") == "E-mail inválido."
    ), "Teste falhou: conta com e-mail inválido foi criada."
    assert (
        criar_conta("teste@exemplo.com", "senha") == "Senha inválida."
    ), "Teste falhou: conta com senha inválida foi criada."
    print("Todos os testes de criar_conta passaram.")


if __name__ == "__main__":
    testar_validar_email()
    testar_validar_senha()
    testar_criar_conta()
