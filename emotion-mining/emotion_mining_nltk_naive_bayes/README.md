# Mineração de Emoção Com Naive Bayes
Foco no estudo da mineração de Emoção utilizando a abordagem estatística
em python.

<br/><br/>
# Abordagem Estatística Para Mineração de Texto (Frequência)
* Classificação por Polaridade
    * Classificação de texto em Positivo, Neutro ou Negativo

* Classificação por Emoção
    * Classificação de texto em Surpresa, Raiva, Tristeza, Alegria, Medo e Nojo

<br/><br/>
# Etapas Básicas
* Entrada/Coleta da Base de Dados (Frases)
* Remoção de Stop Words
* Redução de Dimensionalidade através do Radical das Palavras (**STEAMING**)
* Distribuição de Frequências
* Montagem de Dados para Classificação
* Criação da estrutura (Apply Features do NLTK)

        hoje  | me | sinto | feliz | acordei | assustado | noite | muito | Classe
        ------|----|-------|-------|---------|-----------|-------|-------|-------
           1  | 1  |   1   |   1   |    0    |     0     |   0   |   1   |  Alegria
           0  | 0  |   0   |   0   |    1    |     1     |   1   |   1   |  Medo

<br/><br/>
# Processo de Classificação (Aprendizado Supervisionado)


* Com Base nos **Atributos Previsores** e sua **Classe Correspondente**
determinos

Fase 1                              |       |Fase 2
---------                           |-------|------
Atributos previsores + Classe       |       |Atributos previsores sem classe
Sistema de Aprendizado (Algoritmo)  |       |Classificador (Modelo)
Classificador (Modelo)              |       |Decisão

<br/><br/>
# Exemplo com Histórico de Crédito (Apenas para memorização do contexto)
## Base
Risco       | Histórico     | Garantia | Renda Anual
------------|---------------|----------|------------
Alto        | Ruim          |  Não     |   < 5.000
Alto        | Desconhecido  |  Não     |   >= 5.000 <= 10.00
Baixo       | Bom           |  Sim     |   > 10.00
Moderado    | Ruim          |  Sim     |   > 10.00
Baixo       | Bom           |  Sim     |   >= 5.000 <= 10.00
Moderado    | Desconhecido  |  Não     |   > 10.00
Baixo       | Bom           |  Sim     |   >= 5.000 <= 10.00

<br/><br/>
## Tabulação e Captura do Modelo
Risco (7 registros)| Bom (3) | Desconhecido (2) | Ruim (2) | Não (3) | Sim (4) | < 5.000 (1) | >= 5.000 <= 10.00 (3) |  > 10.00 (3)
-------------------|---------|------------------|----------|---------|---------|-------------|-----------------------|----------
Alto        2/6    |    0    |     1/2          |    1/2   |   2/3   |   0     |     1/1     |          1/3          |      0
Moderado    2/6    |    0    |     1/2          |    1/2   |   1/3   |   1/4   |     0       |          0            |      2/3
Baixo       3/6    |    3/3  |     0            |     0    |   0     |   3/4   |     0       |          2/3          |      1/3


<br/><br/>
## Apicação do Modelo (Neste caso não tem correção Laplaciana)
Exemplo de uma nova Entrada a ser Classificada
Risco       | Histórico     | Garantia | Renda Anual
------------|---------------|----------|------------  
   ???      | Bom           |  Não     |   < 5.000

<br/><br/> 0.22 + 0.11 + 0.50 = 0.8333 (100%)

<br/>p(Alto) - 2/6 * 0 * 2/3 * 1/1 = 0.2222 / 0.8333 = 26.66%
<br/>p(Moderado) - 2/6 * 0 * 1/3 * 0 = 0.1111 / 0.8333 = 13,34%
<br/>p(Baixo) - 3/6 * 3/3 * 0 * 0 = 0.5000 / 0.8333 = 60.00%


<br/><br/>
# Matriz de Confusão

-           | Alto   | Moderado | Baixo
------------|--------|----------|-------
Alto        |  *28   |    7     | 3
Moderado    |   6    |   *32    | 2
Baixo       |   5    |    8     | *25  

* acertos: 28 + 32 + 25 = 85
* erros: 7 + 3 + 6 + 2 + 5 + 5

<br/><br/>
# Artigos de referência
* Mineração de Texto: https://www.researchgate.net/publication/317912973_Mineracao_de_texto_-_Conceitos_e_aplicacoes_praticas
