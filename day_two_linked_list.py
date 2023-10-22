# -*- coding: latin1 -*-


class Paciente:

    def __init__(self, id, nome, estado_de_saude) -> None:
        self.id = id
        self.nome = nome
        self.estado_do_paciente = estado_de_saude
        self.proximo = None


class AdicionaPacientes:

    def __init__(self): 
        self.head = None
        self.tail = None
    
    def adicionar_paciente(self, id, nome, estado_saude):
        novo_paciente = Paciente(id, nome, estado_saude)

        if self.head is None:
            self.head = novo_paciente
            self.tail = novo_paciente
        else:
            self.tail.proximo = novo_paciente
            self.tail = novo_paciente
    
    def exibir_pacientes(self):
        paciente_atual = self.head

        while paciente_atual is not None:
            print(paciente_atual.id, paciente_atual.nome, paciente_atual.estado_do_paciente, end="\n")
            paciente_atual = paciente_atual.proximo
        print("None")

    def remover_paciente(self, id):
        paciente_atual = self.head

        if paciente_atual is not None and paciente_atual == id:
            self.head = paciente_atual.proximo

            if paciente_atual.proximo is None:
                self.tail = None
            
            return
        
        anterior = None

        while paciente_atual is not None:
            if paciente_atual.id == id:
                anterior.proximo = paciente_atual.proximo

                if paciente_atual.proximo is None:
                    self.tail = anterior
                return

            anterior = paciente_atual
            paciente_atual = paciente_atual.proximo

adicionar_paciente = AdicionaPacientes()
adicionar_paciente.adicionar_paciente("123654", "Marcos Lino", "estável")
adicionar_paciente.adicionar_paciente("123655", "Joao Beluga", "critico")
adicionar_paciente.adicionar_paciente("123656","Felisberto Lopes", "estável")
adicionar_paciente.adicionar_paciente("123567", "Adenor Medeiros", "em tratamento")
adicionar_paciente.exibir_pacientes()
adicionar_paciente.remover_paciente("123656")
adicionar_paciente.exibir_pacientes()