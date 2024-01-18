Regressão Lógistíca



Variável dependente:
Situação da redação do participante
    1-  Sem problemas
    0 - Anulada
        Cópia Texto Motivador
        Em Branco
        Fuga ao tema
        Não atendimento ao tipo textual
        Texto insuficiente
        Parte desconectada



Variáveis independentes:

1 - Cor/raça:
        Não declarado - retirar do dataset
        Não dispõe da informação - retirar do dataset
        
        Branca
        Preta
        Parda
        Amarela
        Indígena

        5 variáveis -> 4 dummies (branca implicito)
    

2 - Sexo - Masculino/Feminino as dummies

3 - Localização (Escola) - Urbano/Rural - Não deu para fazer, 70% das observações não tinha esse dado

Creio eu dado da escola que está sendo aplicada a prova

4 -  Q001 - Até que série seu pai, ou o homem responsável por você, estudou?

    0 - Nunca estudou.
        Não completou a 4ª série/5º ano do Ensino Fundamental.
        Completou a 4ª série/5º ano, mas não completou a 8ª série/9º ano do Ensino Fundamental.
        Completou a 8ª série/9º ano do Ensino Fundamental, mas não completou o Ensino Médio.
    
    1-  Completou o Ensino Médio, mas não completou a Faculdade.
        Completou a Faculdade, mas não completou a Pós-graduação.
        Completou a Pós-graduação.
    
    Não sei. - retirar do dataset

5 - Q002 - Até que série sua mãe, ou a mulher responsável por você, estudou?

    0 - Nunca estudou.
        Não completou a 4ª série/5º ano do Ensino Fundamental.
        Completou a 4ª série/5º ano, mas não completou a 8ª série/9º ano do Ensino Fundamental.
        Completou a 8ª série/9º ano do Ensino Fundamental, mas não completou o Ensino Médio.
    
    1-  Completou o Ensino Médio, mas não completou a Faculdade.
        Completou a Faculdade, mas não completou a Pós-graduação.
        Completou a Pós-graduação.
    
    Não sei. - retirar do dataset


6 - Q006 - Qual é a renda mensal de sua família? (Some a sua renda com a dos seus familiares.)

Nenhuma Renda
Até R$ 1.212,00
De R$ 1.212,01 até R$ 1.818,00.

De R$ 1.818,01 até R$ 2.424,00.
De R$ 2.424,01 até R$ 3.030,00.
De R$ 3.030,01 até R$ 3.636,00.
De R$ 3.636,01 até R$ 4.848,00.
De R$ 4.848,01 até R$ 6.060,00.
De R$ 6.060,01 até R$ 7.272,00.
De R$ 7.272,01 até R$ 8.484,00.
De R$ 8.484,01 até R$ 9.696,00.
De R$ 9.696,01 até R$ 10.908,00.

De R$ 10.908,01 até R$ 12.120,00.
De R$ 12.120,01 até R$ 14.544,00.
De R$ 14.544,01 até R$ 18.180,00.
De R$ 18.180,01 até R$ 24.240,00.
Acima de R$ 24.240,00.



7 - Q025 - Na sua residência tem acesso à Internet?


