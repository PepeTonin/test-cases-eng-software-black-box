class ControladorLogin:
    def __init__(self):
        self.tentativas = 0
        self.usuario_bloqueado = False
        self.senha = "senha123"

    def login(self, senha_informada):
        if senha_informada == self.senha:
            self.tentativas = 0  # Reseta tentativas em caso de sucesso
            return "Login bem-sucedido!"
        else:
            self.tentativas += 1
            if self.tentativas >= 3:
                self.usuario_bloqueado = True
                return "Usuário bloqueado após 3 tentativas incorretas."
            return f"Senha incorreta! Tentativa {self.tentativas}/3."
