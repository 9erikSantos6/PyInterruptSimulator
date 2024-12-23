# Simulador de Interrupções em Python

Este projeto simula a gestão e o processamento de interrupções com base em prioridades. Ele usa o conceito de fila de prioridade para tratar diferentes tipos de interrupções em ordem de prioridade. O script pode ser utilizado como base para sistemas que precisam simular ou gerenciar interrupções de maneira assíncrona, como sistemas embarcados ou simuladores de tempo real.

## Funcionalidade

O script simula três tipos de interrupções:
- **Temporizador:** Uma interrupção de temporizador que simula o processamento de um evento de tempo.
- **I/O:** Uma interrupção de entrada/saída, onde o usuário tem 5 segundos para fornecer dados.
- **Erro:** Uma interrupção de erro, simulando um erro de divisão por zero.

As interrupções são processadas em ordem de prioridade, com a prioridade mais baixa sendo processada primeiro.

## Como Funciona

1. **Criação de interrupções**: O script cria interrupções aleatórias com diferentes tipos e prioridades.
2. **Gerenciamento de interrupções**: Um gerenciador de interrupções mantém uma fila de interrupções. Cada interrupção é processada conforme sua prioridade.
3. **Processamento das interrupções**:
   - **Temporizador**: Simula o tempo de execução de uma tarefa.
   - **I/O**: Aguarda a entrada do usuário e simula um tempo limite de 5 segundos.
   - **Erro**: Simula uma falha de execução (divisão por zero).
4. **Threading**: As interrupções e o despacho de interrupções são executados em threads separadas para simular um ambiente assíncrono.

## Dependências

Este script usa a biblioteca padrão do Python, então não é necessário instalar dependências externas. As bibliotecas usadas são:
- `time`
- `queue`
- `threading`
- `random`
- `sys`

## Como Executar

Para executar o script, basta rodá-lo diretamente no terminal:

```bash
$ python3 pyinterrupt.py
```

## Explicação do Código

### Classes

- **Interrupcao**: Representa uma interrupção com tipo e prioridade. Implementa o método `__lt__` para permitir a comparação de interrupções com base na prioridade.
- **GerenciadorDeInterrupcoes**: Gerencia e despacha as interrupções, garantindo que elas sejam processadas em ordem de prioridade. A fila de interrupções (`fila_de_interrupcoes`) usa uma `PriorityQueue`, onde as interrupções com maior prioridade (menor valor de `prioridade`) são processadas primeiro.

### Métodos

- **adicionar_interrupcao**: Adiciona uma nova interrupção à fila de interrupções.
- **despachar**: Despacha as interrupções em ordem de prioridade.
- **tratar_interrupcao**: Chama o manipulador correspondente para cada tipo de interrupção.
- **aguardar**: Aguarda o término do processamento de todas as interrupções.
- **simular_interrupcoes**: Simula a adição de interrupções aleatórias à fila.

## Exemplo de Saída

Ao executar o script, você verá algo semelhante a:

```bash
> Processando interrupção: erro (Prioridade: 1)

> Simulando interrupção de erro...

> ZeroDivisionError tratado!
 - Detalhes do erro: division by zero
> Manipulador de erro finalizado.
> Interrupção processada: erro

> Processando interrupção: temporizador (Prioridade: 2)

> Tratando interrupção de temporizador...
> Interrupção de temporizador finalizada!
> Interrupção processada: temporizador

...

> Todas as interrupções foram processadas com sucesso!
```

## Observações

- O script utiliza threads para simular a execução assíncrona das interrupções.
- As interrupções são tratadas com base na sua prioridade, e o tipo de interrupção determina qual manipulador será invocado.

## Contribuição

Contribuições são bem-vindas! Se você tiver melhorias ou sugestões, por favor, envie um pull request ou abra uma issue.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.