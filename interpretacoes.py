"""Interpretações temáticas e síntese relacional para Tarot e Baralho Cigano.

A base é simbólica e editável. Regras de síntese não substituem leitura humana.
"""
from collections import Counter

TEMAS = {
    "Amor": {
        "foco": "reciprocidade, comunicação, disponibilidade emocional, limites e compatibilidade entre atitudes e expectativas",
        "acao": "observe comportamentos consistentes e converse diretamente sobre expectativas e limites",
        "abertura": "No campo afetivo, a tiragem pode ser lida como um retrato simbólico das dinâmicas, escolhas e necessidades em jogo — não como prova do que outra pessoa sente.",
    },
    "Família": {
        "foco": "papéis familiares, pertencimento, comunicação, limites e padrões que se repetem",
        "acao": "identifique o que depende de você, estabeleça limites claros e priorize conversas respeitosas",
        "abertura": "No contexto familiar, a tiragem convida a observar vínculos, responsabilidades e padrões de convivência sem presumir que uma única pessoa seja a causa de tudo.",
    },
    "Trabalho": {
        "foco": "prioridades, colaboração, reconhecimento, recursos, autonomia e decisões profissionais",
        "acao": "transforme a reflexão em um próximo passo verificável, como alinhar expectativas, organizar prioridades ou buscar informação",
        "abertura": "No trabalho, as cartas podem funcionar como lentes para examinar ambiente, estratégia, relações profissionais e escolhas disponíveis.",
    },
    "Estudos": {
        "foco": "método, constância, concentração, gestão do tempo, confiança e apoio disponível",
        "acao": "defina uma ação concreta, como praticar questões, revisar um tópico ou ajustar o cronograma",
        "abertura": "Nos estudos, a leitura pode ajudar a refletir sobre método, motivação, obstáculos e recursos que podem ser mobilizados.",
    },
    "Geral": {
        "foco": "padrões recorrentes, recursos disponíveis, contexto, escolhas e aspectos sob seu controle",
        "acao": "confronte as hipóteses sugeridas pela leitura com os fatos e escolha um próximo passo realista",
        "abertura": "Em uma leitura geral, o conjunto é tratado como um convite para observar tendências simbólicas, tensões e possibilidades de ação.",
    },
}

# Leituras por tema para cartas centrais. As demais recebem interpretação temática
# específica a partir de suas descrições e de seus elementos simbólicos.
TEMA_CARTAS = {
    "O Louco": {
        "Amor": "abertura a uma experiência afetiva nova, espontaneidade ou necessidade de não confundir liberdade com falta de responsabilidade",
        "Família": "mudança de papel ou tentativa de se relacionar sem repetir expectativas antigas",
        "Trabalho": "explorar uma oportunidade ou experimentar uma abordagem nova, avaliando antes os riscos práticos",
        "Estudos": "começar uma etapa com curiosidade, sem dispensar planejamento e constância",
    },
    "O Mago": {
        "Amor": "iniciativa e comunicação podem aproximar pessoas; avalie se palavras e atitudes estão alinhadas",
        "Família": "há espaço para agir de forma propositiva e melhorar a comunicação",
        "Trabalho": "uso estratégico de habilidades, recursos e articulação para tirar uma ideia do papel",
        "Estudos": "capacidade de organizar recursos e transformar intenção em prática deliberada",
    },
    "A Sacerdotisa": {
        "Amor": "sentimentos não verbalizados, reserva ou necessidade de observar antes de concluir; silêncio, sozinho, não confirma interesse",
        "Família": "assuntos pouco discutidos ou necessidade de escutar antes de reagir",
        "Trabalho": "análise discreta, pesquisa e leitura cuidadosa do contexto antes de expor uma decisão",
        "Estudos": "aprofundamento, pesquisa e concentração em vez de buscar respostas rápidas",
    },
    "Os Enamorados": {
        "Amor": "afinidade e atração podem coexistir com uma escolha importante; compatibilidade também exige atitudes e valores alinhados",
        "Família": "escolhas que pedem consideração por vínculos sem abandonar a própria autonomia",
        "Trabalho": "decisão entre caminhos ou necessidade de alinhar valores e parceria",
        "Estudos": "escolha de prioridade, curso ou método que combine com objetivos reais",
    },
    "A Justiça": {
        "Amor": "reciprocidade, acordos claros e avaliação honesta do equilíbrio entre dar e receber",
        "Família": "responsabilidades e limites precisam ser distribuídos com clareza",
        "Trabalho": "critérios, acordos, prestação de contas e consequências das decisões",
        "Estudos": "avaliação objetiva, critérios explícitos e responsabilidade pelo processo",
    },
    "O Eremita": {
        "Amor": "espaço para compreender necessidades; distanciamento pode significar muitas coisas e deve ser esclarecido por diálogo",
        "Família": "necessidade de privacidade, reflexão ou redução temporária de ruído",
        "Trabalho": "autonomia, especialização e análise cuidadosa antes de agir",
        "Estudos": "estudo individual, aprofundamento e ritmo sustentável",
    },
    "A Roda da Fortuna": {
        "Amor": "uma dinâmica pode estar mudando; observe o que se altera na prática em vez de presumir um destino fixo",
        "Família": "mudanças de fase podem exigir adaptação de papéis e expectativas",
        "Trabalho": "condições variáveis, oportunidade ou mudança de contexto que pede flexibilidade",
        "Estudos": "oscilações de ritmo e resultados pedem revisão do método, não fatalismo",
    },
    "A Força": {
        "Amor": "paciência, coragem emocional e limites gentis; não significa tolerar desrespeito",
        "Família": "firmeza sem escalada de conflito e cuidado com reações impulsivas",
        "Trabalho": "perseverança, regulação emocional e influência exercida sem agressividade",
        "Estudos": "consistência e tolerância à frustração ao aprender algo difícil",
    },
    "A Morte": {
        "Amor": "fim de uma dinâmica ou transformação de expectativas; não determina literalmente separação",
        "Família": "um padrão familiar pode precisar ser encerrado ou reorganizado",
        "Trabalho": "fechamento de ciclo, mudança de função ou abandono de uma estratégia que não serve mais",
        "Estudos": "deixar um método ineficaz e construir outro mais adequado",
    },
    "A Temperança": {
        "Amor": "ajuste de ritmos, diálogo e integração de diferenças sem apagar necessidades individuais",
        "Família": "mediação, paciência e busca de acordos possíveis",
        "Trabalho": "coordenação entre pessoas e processos, com ajustes graduais",
        "Estudos": "distribuição equilibrada do esforço e combinação de métodos",
    },
    "A Torre": {
        "Amor": "uma expectativa pode ser questionada; procure fatos e converse antes de interpretar uma ruptura como inevitável",
        "Família": "tensões ou estruturas antigas podem precisar ser revistas com cuidado",
        "Trabalho": "mudança brusca, falha de processo ou percepção que exige reavaliar um plano",
        "Estudos": "reconhecer uma estratégia que não está funcionando e corrigir a rota",
    },
    "A Estrela": {
        "Amor": "recuperação da confiança e abertura emocional gradual, sem ignorar sinais concretos",
        "Família": "esperança de entendimento e reconstrução de confiança por ações consistentes",
        "Trabalho": "visão de futuro, inspiração e reconexão com objetivos",
        "Estudos": "retomar confiança, visualizar metas e avançar passo a passo",
    },
    "A Lua": {
        "Amor": "sensibilidade e incerteza; evite transformar receios ou intuições em certezas sobre outra pessoa",
        "Família": "mal-entendidos ou emoções difíceis de nomear pedem esclarecimento",
        "Trabalho": "informação incompleta, percepção subjetiva ou necessidade de confirmar suposições",
        "Estudos": "ansiedade ou falta de clareza podem atrapalhar; divida o problema e verifique o que já sabe",
    },
    "O Sol": {
        "Amor": "clareza, alegria e expressão aberta; procure reciprocidade observável",
        "Família": "convivência mais transparente e reconhecimento do que funciona",
        "Trabalho": "visibilidade, clareza de objetivos e oportunidade de demonstrar competência",
        "Estudos": "compreensão que se consolida, confiança e percepção mais clara do progresso",
    },
    "O Mundo": {
        "Amor": "integração e conclusão de uma etapa, com clareza sobre o que se deseja levar adiante",
        "Família": "fechamento de ciclo e reorganização de vínculos ou responsabilidades",
        "Trabalho": "conclusão, integração de competências e reconhecimento de uma etapa realizada",
        "Estudos": "consolidação de aprendizagem, conclusão ou passagem a uma nova etapa",
    },
    "O Coração": {
        "Amor": "afeto, desejo e importância emocional; a carta não comprova reciprocidade, que precisa ser percebida nas atitudes",
        "Família": "carinho e vínculo, com atenção para expressar cuidado de modo concreto",
        "Trabalho": "envolvimento pessoal com uma atividade ou motivação ligada a valores",
        "Estudos": "interesse genuíno pode sustentar a dedicação, desde que acompanhado de método",
    },
    "O Anel": {
        "Amor": "compromisso, acordo ou continuidade; examine se a relação é definida e recíproca na prática",
        "Família": "pacto, responsabilidade compartilhada ou expectativa de continuidade",
        "Trabalho": "contrato, parceria ou obrigação que exige clareza sobre termos",
        "Estudos": "compromisso com uma rotina, grupo ou meta de longo prazo",
    },
    "A Raposa": {
        "Amor": "cautela e atenção a inconsistências; não é prova de traição ou mentira",
        "Família": "interesses diferentes ou comunicação estratégica pedem observação sem acusação precipitada",
        "Trabalho": "planejamento, autoproteção e leitura dos incentivos presentes no ambiente",
        "Estudos": "estratégia, atenção a detalhes e escolha inteligente de como investir esforço",
    },
    "As Nuvens": {
        "Amor": "ambiguidade ou dúvida; evite preencher lacunas com suposições e procure esclarecimento",
        "Família": "comunicação confusa ou emoções misturadas que pedem tempo e conversa",
        "Trabalho": "falta de informação ou prioridade pouco definida; confirme os fatos",
        "Estudos": "conteúdo confuso ou excesso de tarefas pede divisão em partes menores",
    },
    "Os Caminhos": {
        "Amor": "uma escolha sobre limites, disponibilidade ou direção do vínculo",
        "Família": "alternativas para lidar com uma questão, sem assumir que existe apenas uma saída",
        "Trabalho": "decisão entre caminhos profissionais e avaliação de custos e benefícios",
        "Estudos": "escolha de foco, estratégia ou prioridade conforme o objetivo",
    },
    "A Chave": {
        "Amor": "um ponto decisivo pode ser a conversa, a clareza ou o reconhecimento do que é essencial",
        "Família": "uma solução prática pode surgir ao identificar o problema central",
        "Trabalho": "identificação de um recurso ou decisão que destrava uma questão",
        "Estudos": "descobrir o conceito-chave ou método que torna o conteúdo mais compreensível",
    },
}

ELEMENTOS = {
    "Paus": {
        "Amor": "iniciativa, desejo, ritmo e energia colocada no vínculo",
        "Família": "movimento, iniciativa e energia para mudar a convivência",
        "Trabalho": "motivação, criatividade, ação e impulso para começar",
        "Estudos": "energia inicial, curiosidade e disposição para praticar",
    },
    "Copas": {
        "Amor": "sentimentos, conexão, sensibilidade e expectativas afetivas",
        "Família": "afetos, pertencimento, cuidado e necessidades emocionais",
        "Trabalho": "clima relacional, empatia e envolvimento com o que se faz",
        "Estudos": "motivação emocional, interesse e relação subjetiva com o aprendizado",
    },
    "Espadas": {
        "Amor": "conversa, pensamentos, dúvidas, limites e conflitos que precisam de nome",
        "Família": "comunicação, desacordos, decisões e clareza de limites",
        "Trabalho": "análise, comunicação, negociação e decisões difíceis",
        "Estudos": "raciocínio, análise crítica, dúvidas e organização conceitual",
    },
    "Ouros": {
        "Amor": "constância, segurança, demonstrações concretas e investimento de tempo",
        "Família": "recursos, responsabilidades práticas e segurança cotidiana",
        "Trabalho": "recursos, estabilidade, execução e resultados concretos",
        "Estudos": "rotina, prática, recursos e construção gradual de competência",
    },
}

RANKS = {
    "Ás": "início, potencial ou oportunidade que ainda precisa ser desenvolvida",
    "Dois": "escolha, parceria, equilíbrio ou tensão entre duas alternativas",
    "Três": "crescimento, colaboração, expressão ou primeiros resultados",
    "Quatro": "estrutura, estabilidade, proteção ou necessidade de pausa",
    "Cinco": "desafio, atrito, perda de equilíbrio ou mudança necessária",
    "Seis": "ajuste, cooperação, transição ou recuperação",
    "Sete": "avaliação, persistência, estratégia ou teste de convicções",
    "Oito": "movimento, repetição, dedicação ou aceleração",
    "Nove": "maturação, autonomia, culminação próxima ou avaliação interna",
    "Dez": "culminação, excesso de responsabilidade ou encerramento de ciclo",
    "Pajem": "aprendizado, curiosidade, mensagem ou habilidade em formação",
    "Cavaleiro": "busca ativa, movimento, impulso ou modo de perseguir um objetivo",
    "Rainha": "maturidade, percepção e domínio interno da energia do naipe",
    "Rei": "gestão, liderança e expressão estruturada da energia do naipe",
}

def _tema_carta(carta, assunto):
    nome = carta["nome"]
    if nome in TEMA_CARTAS and assunto in TEMA_CARTAS[nome]:
        return TEMA_CARTAS[nome][assunto]
    if carta["baralho"] == "Tarot":
        for naipe in ELEMENTOS:
            sufixo = f" de {naipe}"
            if nome.endswith(sufixo):
                rank = nome[:-len(sufixo)]
                rank_desc = RANKS.get(rank, "um estágio de desenvolvimento")
                elemento = ELEMENTOS[naipe][assunto]
                return f"{rank_desc}; no tema {assunto.lower()}, isso direciona a atenção para {elemento}"
    # Para o Lenormand, o significado individual é combinado com o foco temático,
    # sem transformar uma carta em previsão literal.
    return f"{carta['significado'].capitalize()}; no tema {assunto.lower()}, observe como isso se relaciona a {TEMAS[assunto]['foco']}"

def interpretar(carta, assunto, posicao=None):
    tema = TEMAS.get(assunto, TEMAS["Geral"])
    invertida = carta["baralho"] == "Tarot" and carta.get("orientacao") == "Invertida"
    significado_base = carta.get("significado", "")
    if invertida:
        significado_base = carta.get("invertido") or f"expressão bloqueada, excessiva ou pouco integrada de {significado_base}"
    contextual = _tema_carta(carta, assunto)
    if invertida:
        contextual = f"Em posição invertida, considere um bloqueio, excesso, atraso ou expressão interna dessa dinâmica: {contextual}."
    else:
        contextual = contextual[0].upper() + contextual[1:] + "."
    posicao_texto = f"**Posição na tiragem:** {posicao}. " if posicao else ""
    return {
        "titulo": f'{carta["nome"]} — {carta.get("orientacao", "Normal")}',
        "significado": significado_base,
        "contexto": contextual,
        "reflexao": f"{posicao_texto}Que fatos, escolhas ou padrões da sua situação se conectam a esse símbolo?",
        "acao": tema["acao"],
    }

def _grupo_semantico(carta):
    nome = carta["nome"]
    if carta["baralho"] == "Tarot":
        for naipe in ELEMENTOS:
            if nome.endswith(f" de {naipe}"):
                return naipe
        return "Arcano Maior"
    # Grupos amplos para a síntese Lenormand: temas não são previsões fixas.
    grupos = {
        "relacional": ["O Coração", "O Anel", "O Cão", "O Buquê", "Os Pássaros", "O Jardim", "O Homem", "A Mulher"],
        "mudança": ["O Cavaleiro", "O Navio", "A Cegonha", "Os Caminhos", "A Foice", "O Caixão", "A Roda da Fortuna"],
        "clareza": ["As Nuvens", "A Lua", "O Livro", "A Carta", "A Chave", "As Estrelas", "O Sol"],
        "recursos": ["Os Peixes", "A Âncora", "O Urso", "A Casa", "A Árvore", "A Montanha"],
        "tensão": ["A Cobra", "A Raposa", "Os Ratos", "O Chicote", "A Cruz"],
    }
    for grupo, nomes in grupos.items():
        if any(n in nome for n in nomes):
            return grupo
    return "tema geral"

def _posicoes_para(n):
    if n == 1:
        return ["Tema central"]
    if n == 2:
        return ["Situação", "Ponto de atenção"]
    if n == 3:
        return ["Contexto", "Dinâmica atual", "Possível direção"]
    if n == 4:
        return ["Contexto", "O que ajuda", "O que desafia", "Próximo passo"]
    if n == 5:
        return ["Contexto", "O que está em jogo", "Ponto forte", "Ponto de atenção", "Próximo passo"]
    return [f"Carta {i+1}" for i in range(n)]

def sintetizar(cartas, assunto, pergunta=""):
    if not cartas:
        return "Nenhuma carta foi selecionada."
    tema = TEMAS.get(assunto, TEMAS["Geral"])
    grupos = Counter(_grupo_semantico(c) for c in cartas)
    nomes = [c["nome"] for c in cartas]
    posicoes = _posicoes_para(len(cartas))

    linhas = [tema["abertura"]]
    if pergunta.strip():
        linhas.append(f"**Pergunta registrada:** {pergunta.strip()}")
    linhas.append(f"**Eixo principal:** a leitura deve ser examinada em relação a {tema['foco']}.")

    # Interpretação de percurso: posições explícitas para tiragens de 1 a 5.
    linhas.append("**Percurso da tiragem:**")
    for i, carta in enumerate(cartas):
        resumo = _tema_carta(carta, assunto)
        if carta.get("orientacao") == "Invertida" and carta["baralho"] == "Tarot":
            resumo = "Possível bloqueio ou expressão pouco integrada: " + resumo
        linhas.append(f"- **{posicoes[i]} — {carta['nome']}** ({carta['baralho']}): {resumo}.")

    # Padrões de naipes no Tarot, sem inferir destino ou sentimentos de terceiros.
    tarot = [c for c in cartas if c["baralho"] == "Tarot"]
    naipes = Counter(next((n for n in ELEMENTOS if c["nome"].endswith(f" de {n}")), "Arcano Maior")
                     for c in tarot)
    if tarot and naipes:
        max_count = max(naipes.values())
        dominantes = [n for n, count in naipes.items() if count == max_count and count >= 2]
        if dominantes:
            descricoes = {
                "Paus": "iniciativa, desejo e ação",
                "Copas": "emoções, vínculos e expectativas afetivas",
                "Espadas": "pensamento, comunicação e decisões",
                "Ouros": "constância, recursos e resultados concretos",
                "Arcano Maior": "temas amplos, estruturais ou de desenvolvimento pessoal",
            }
            if len(dominantes) == 1:
                n = dominantes[0]
                linhas.append(f"**Ênfase simbólica:** há repetição de {n}, o que coloca em destaque {descricoes[n]}. Isso é uma ênfase interpretativa, não uma prova ou uma previsão.")
            else:
                linhas.append("**Ênfase simbólica:** há mais de um grupo recorrente, sugerindo que a leitura pede integrar diferentes dimensões: " +
                              "; ".join(f"{n} ({descricoes[n]})" for n in dominantes) + ".")

    # Tensão entre cartas invertidas e normais.
    invertidas = [c for c in tarot if c.get("orientacao") == "Invertida"]
    normais = [c for c in tarot if c.get("orientacao") == "Normal"]
    if invertidas and normais:
        linhas.append(f"**Tensão interna:** {len(invertidas)} carta(s) do Tarot saíram invertidas e {len(normais)} na posição normal. Uma leitura possível é observar onde existe facilidade de expressão e onde pode haver hesitação, excesso ou necessidade de revisão; o significado específico depende das cartas envolvidas.")
    elif invertidas:
        linhas.append("**Tônica de revisão:** todas as cartas do Tarot nesta tiragem saíram invertidas. Considere se o tema pede pausa, revisão de pressupostos ou atenção a aspectos ainda não integrados; não interprete isso automaticamente como algo negativo.")

    # Relação entre os dois sistemas, quando ambos foram usados.
    tarot_groups = {_grupo_semantico(c) for c in cartas if c["baralho"] == "Tarot"}
    lenormand_groups = {_grupo_semantico(c) for c in cartas if c["baralho"] == "Baralho Cigano"}
    if tarot_groups and lenormand_groups:
        overlap = tarot_groups & lenormand_groups
        if overlap:
            linhas.append("**Diálogo entre os baralhos:** há aproximação de temas simbólicos em " +
                          ", ".join(sorted(overlap)) +
                          ". Leia essa aproximação como um ponto para investigar na sua situação, não como confirmação independente de um acontecimento.")
        else:
            linhas.append("**Diálogo entre os baralhos:** os sistemas enfatizam aspectos diferentes. Isso pode ajudar a olhar para a situação por mais de uma perspectiva; não é necessário forçar uma conclusão única.")

    linhas.append(f"**Síntese prática:** a tiragem destaca questões ligadas a {tema['foco']}. {tema['acao'].capitalize()}. Use a leitura para formular perguntas melhores e refletir sobre alternativas; confronte qualquer hipótese com fatos observáveis.")
    return "\n\n".join(linhas)
