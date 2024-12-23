#!/usr/bin/python3

import time
import queue
import threading
import random
import sys


class Interrupcao:
    """Representa uma interrupção com tipo e prioridade."""
    def __init__(self, tipo, prioridade):
        self.tipo = tipo
        self.prioridade = prioridade

    def __lt__(self, outro):
        """Define a comparação entre interrupções com base na prioridade."""
        return self.prioridade < outro.prioridade


class GerenciadorDeInterrupcoes:
    """Gerencia e despacha interrupções com base em prioridades."""
    def __init__(self):
        self.fila_de_interrupcoes = queue.PriorityQueue()
        self.executando = True  

    def adicionar_interrupcao(self, interrupcao):
        """Adiciona uma interrupção na fila."""
        self.fila_de_interrupcoes.put(interrupcao)

    def despachar(self):
        """Despacha interrupções em ordem de prioridade."""
        while self.executando or not self.fila_de_interrupcoes.empty():
            try:
                interrupcao = self.fila_de_interrupcoes.get(timeout=0.1) # Timeout evitando bloqueios
                self.tratar_interrupcao(interrupcao)
                self.fila_de_interrupcoes.task_done()
            except queue.Empty:
                continue
            except Exception as e:
                print(f"> Erro no despacho: {e}")

    def tratar_interrupcao(self, interrupcao):
        """Identifica e chama o manipulador correto para uma interrupção."""
        try:
            print("\n")
            print("=" * 100)
            print(f"\n> Processando interrupção: {interrupcao.tipo} (Prioridade: {interrupcao.prioridade})")
            if interrupcao.tipo == 'temporizador':
                self.tratar_temporizador()
            elif interrupcao.tipo == 'io':
                self.tratar_io()
            elif interrupcao.tipo == 'erro':
                self.tratar_erro()
        except Exception as e:
            print(f"> Erro inesperado no tratamento: {e}")
        finally:
            print(f"> Interrupção processada: {interrupcao.tipo}")

    def tratar_temporizador(self):
        """Manipulador para interrupções de temporizador."""
        print("\n> Tratando interrupção de temporizador...")
        time.sleep(2)
        print("> Interrupção de temporizador finalizada!")

    def tratar_io(self):
        """Manipulador para interrupções de entrada/saída."""
        print("\n< Tratando interrupção de I/O, você tem 5 segundos para inserir dados:")
        sys.stdout.flush()
        
        thread_entrada = threading.Thread(target=self._obter_entrada)
        thread_entrada.daemon = True
        thread_entrada.start()
        
        thread_entrada.join(timeout=5)  # Limita o tempo para a entrada
        
        if thread_entrada.is_alive():
            print("\n> Tempo limite atingido. Interrupção de I/O ignorada.")

    def _obter_entrada(self):
        """Captura entrada do usuário."""
        try:
            dados = input()
            print(f"> Dados recebidos: {dados}")
        except Exception as e:
            print(f"> Erro ao capturar entrada: {e}")

    def tratar_erro(self):
        """Manipulador para interrupções de erro."""
        try:
            print("\n> Simulando interrupção de erro...")
            x = 9 / 0  # Simulando erro
            print(f"Divisão: 9 / 0 = {x}")
        except ZeroDivisionError as zde:
            print("\n> ZeroDivisionError tratado!")
            print(f" - Detalhes do erro: {zde}")
        finally:
            print("> Manipulador de erro finalizado.")

    def aguardar(self):
        """Espera até que todas as interrupções sejam tratadas."""
        self.executando = False  # Finaliza o loop de despacho
        self.fila_de_interrupcoes.join()  # Aguarda processamento da fila


def simular_interrupcoes(gerenciador, quantidade=10):
    """Simula interrupções em intervalos aleatórios."""
    tipos = ['temporizador', 'io', 'erro']
    for _ in range(quantidade):
        tipo = random.choice(tipos)
        prioridade = random.randint(0, 10)  # Prioridades aleatórias
        gerenciador.adicionar_interrupcao(Interrupcao(tipo, prioridade))
        time.sleep(random.uniform(0.5, 2))  # Intervalo aleatório


def main():
    # Criando o gerenciador de interrupções
    gerenciador = GerenciadorDeInterrupcoes()

    # Criando thread para simular interrupções
    thread_simulacao = threading.Thread(target=simular_interrupcoes, args=(gerenciador, 10))
    thread_simulacao.start()

    # Criando thread para despachar interrupções
    thread_despacho = threading.Thread(target=gerenciador.despachar)
    thread_despacho.start()

    # Aguarda a conclusão das threads
    thread_simulacao.join()
    gerenciador.aguardar()
    
    # Aguarda o término do despachador antes de finalizar o programa
    gerenciador.executando = False
    thread_despacho.join()

    print("\n")
    print("=" * 100)
    print("\n> Todas as interrupções foram processadas com sucesso!")
    exit()


if __name__ == "__main__":
    main()

