# Oráculo — versão 2: interpretação aprimorada

## O que mudou
- Interpretações contextuais por assunto para vários Arcanos Maiores e cartas do Baralho Cigano.
- Interpretação temática dos Arcanos Menores usando rank + naipe com contexto, como ponto de partida editável.
- Síntese do conjunto com posições para tiragens de 1 a 5 cartas, padrões de naipes, inversões e diálogo entre baralhos.
- O assunto e a pergunta não influenciam o sorteio.

## Como atualizar seu projeto
1. Feche o Streamlit com `Ctrl+C` no terminal.
2. Faça uma cópia da sua pasta atual, se quiser manter a versão anterior.
3. Extraia este ZIP em uma pasta nova ou substitua os arquivos `app.py` e `interpretacoes.py` do projeto existente.
4. Preserve `baralhos.py` e `sorteio.py` se você já os alterou; esta versão usa o cadastro anterior.
5. Execute no terminal do VS Code:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

## Limites atuais
A síntese é baseada em regras simbólicas explícitas, não em um modelo de linguagem. Ela não deve ser entendida como leitura objetiva de acontecimentos ou pensamentos de terceiros. Os Arcanos Menores e parte do Lenormand ainda precisam de revisão editorial carta por carta para chegar a uma base interpretativa mais autoral e profunda.


## Camada visual de ícones (versão 3)
A interface inclui símbolos por Arcano Maior, naipe do Tarot e carta cigana. São marcadores visuais iniciais; não substituem as ilustrações completas das cartas. A função `icone_carta()` em `app.py` permite trocar ou ajustar os símbolos.
