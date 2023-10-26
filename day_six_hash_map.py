# -*- coding:latin1 -*-

class Jogo:

    def __init__(self):
        self.pontuacao = {}

    def adiciona_jogador(self, nome_usuario):
        self.pontuacao[nome_usuario] = 0

    def atualiza_pontos(self, usuario, pontos):
        if usuario in self.pontuacao:
            self.pontuacao[usuario] = pontos
        else:
            return print("Este usuário não existe")

    def lista_jogadores(self):
        maior_pontuacao = max(self.pontuacao.values())
        ranking_jogadores = sorted(self.pontuacao.items(), key=lambda x:x[1], reverse=True)
        
        for usuario, pontos in ranking_jogadores:
            if(pontos == maior_pontuacao):
                print(f"User: {usuario} | Pts: {pontos} Vencedor!")
            else:
                print(f"User: {usuario} | Pts: {pontos}")

    def remove_jogador(self, usuario):
        
        if usuario in self.pontuacao:
            del self.pontuacao[usuario]
        else:
            return print("Este usuário não existe")


add_jogador = Jogo()
add_jogador.adiciona_jogador("NoobMaster69") 
add_jogador.adiciona_jogador("Mr.Noobot")
add_jogador.adiciona_jogador("GodNoob96")  
add_jogador.atualiza_pontos("NoobMaster69", 12)
add_jogador.atualiza_pontos("Mr.Noobot", 18)
add_jogador.atualiza_pontos("GodNoob96", 14)
add_jogador.lista_jogadores()
