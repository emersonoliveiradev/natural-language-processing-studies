# Mineração de Emoção Com Na
Foco no estudo da mineração de Emoção utilizando a abordagem estatística
em python.

# Etapas Básicas
* Entrada/Coleta da Base de Dados (Frases)
* Remoção de Stop Words
* Redução de Dimensionalidade através do Radical das Palavras (**STEAMING**)
* Distribuição de Frequências
* Montagem de Dados para Classificação

        hoje  | me | sinto | feliz | acordei | assustado | noite | muito | Classe
        ------|----|-------|-------|---------|-----------|-------|-------|-------
           1  | 1  |   1   |   1   |    0    |     0     |   0   |   1   |  Alegria
           0  | 0  |   0   |   0   |    1    |     1     |   1   |   1   |  Medo



# Abordagem Estatística Para Mineração de Texto (Frequência)
* Classificação por Polaridade
    * Classificação de texto em Positivo, Neutro ou Negativo

* Classificação por Emoção
    * Classificação de texto em Surpresa, Raiva, Tristeza, Alegria, Medo e Nojo





# Processo de Classificação (Aprendizado Supervisionado)


* Com Base nos **Atributos Previsores** e sua **Classe Correspondente**
determinos

Fase 1                              |       |Fase 2
---------                           |-------|------
Atributos previsores + Classe       |       |Atributos previsores sem classe
Sistema de Aprendizado (Algoritmo)  |       |Classificador (Modelo)
Classificador (Modelo)              |       |Decisão



# Artigos de referência
* Mineração de Texto: https://www.researchgate.net/publication/317912973_Mineracao_de_texto_-_Conceitos_e_aplicacoes_praticas
