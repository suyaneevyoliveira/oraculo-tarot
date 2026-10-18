"""Cadastro inicial dos baralhos e significados editáveis."""

NAIPES = {
    "Paus": ["Ás", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Pajem", "Cavaleiro", "Rainha", "Rei"],
    "Copas": ["Ás", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Pajem", "Cavaleiro", "Rainha", "Rei"],
    "Espadas": ["Ás", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Pajem", "Cavaleiro", "Rainha", "Rei"],
    "Ouros": ["Ás", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Pajem", "Cavaleiro", "Rainha", "Rei"],
}

ARCANOS_MAIORES = [
    ("O Louco", "começos, liberdade, espontaneidade e abertura ao desconhecido"),
    ("O Mago", "iniciativa, habilidade, recursos disponíveis e capacidade de agir"),
    ("A Sacerdotisa", "intuição, silêncio, observação e conhecimento interior"),
    ("A Imperatriz", "criatividade, crescimento, cuidado e abundância"),
    ("O Imperador", "estrutura, autoridade, limites e estabilidade"),
    ("O Hierofante", "tradição, aprendizado, valores e orientação"),
    ("Os Enamorados", "escolhas, afinidade, vínculos e alinhamento de valores"),
    ("O Carro", "direção, determinação, autonomia e avanço"),
    ("A Justiça", "equilíbrio, responsabilidade, análise e consequências"),
    ("O Eremita", "introspecção, prudência, estudo e busca de clareza"),
    ("A Roda da Fortuna", "ciclos, mudanças, movimento e fatores fora do controle"),
    ("A Força", "coragem, autocontrole, paciência e firmeza gentil"),
    ("O Enforcado", "pausa, nova perspectiva, espera e revisão de prioridades"),
    ("A Morte", "encerramento de ciclo, transformação e desapego"),
    ("A Temperança", "moderação, integração, adaptação e equilíbrio gradual"),
    ("O Diabo", "apegos, tentações, dependências e padrões que limitam"),
    ("A Torre", "ruptura, revelação, instabilidade e revisão de estruturas"),
    ("A Estrela", "esperança, inspiração, recuperação e confiança gradual"),
    ("A Lua", "incerteza, imaginação, sensibilidade e informações incompletas"),
    ("O Sol", "clareza, vitalidade, reconhecimento e alegria"),
    ("O Julgamento", "avaliação, despertar, chamado e decisões de renovação"),
    ("O Mundo", "conclusão, integração, realização e fechamento de etapa"),
]

def montar_tarot():
    cartas = []
    for nome, significado in ARCANOS_MAIORES:
        cartas.append({
            "nome": nome, "baralho": "Tarot", "categoria": "Arcano Maior",
            "significado": significado,
            "invertido": f"o aspecto desafiador de {significado}, possível bloqueio, excesso ou necessidade de revisão",
        })
    for naipe, ranks in NAIPES.items():
        for rank in ranks:
            # Base semântica explícita por naipe; os números/cortes acrescentam o estágio.
            bases = {
                "Paus": "energia, criatividade, iniciativa, motivação e ação",
                "Copas": "emoções, vínculos, sensibilidade, afeto e imaginação",
                "Espadas": "pensamento, comunicação, conflitos, discernimento e decisões",
                "Ouros": "recursos, trabalho, corpo, segurança e resultados concretos",
            }
            rank_notes = {
                "Ás": "uma oportunidade inicial ou potencial emergente",
                "Dois": "uma escolha, parceria ou necessidade de equilíbrio",
                "Três": "crescimento, colaboração ou primeiros resultados",
                "Quatro": "estabilidade, estrutura ou uma pausa necessária",
                "Cinco": "tensão, mudança ou desafio que pede adaptação",
                "Seis": "ajuste, cooperação, transição ou recuperação",
                "Sete": "avaliação, persistência ou teste de convicções",
                "Oito": "movimento, prática, dedicação ou aceleração",
                "Nove": "maturação, autonomia ou proximidade de um resultado",
                "Dez": "culminação, responsabilidade ou fechamento de ciclo",
                "Pajem": "curiosidade, aprendizado e uma mensagem em desenvolvimento",
                "Cavaleiro": "movimento, busca e expressão ativa da energia do naipe",
                "Rainha": "maturidade receptiva, percepção e domínio interno da energia do naipe",
                "Rei": "liderança, domínio e expressão estruturada da energia do naipe",
            }
            cartas.append({
                "nome": f"{rank} de {naipe}", "baralho": "Tarot",
                "categoria": f"Arcano Menor — {naipe}",
                "significado": f"{rank_notes[rank]}; {bases[naipe]}",
                "invertido": f"atraso, excesso, bloqueio ou dificuldade para expressar {bases[naipe]}",
            })
    return cartas

CIGANO_NOMES = [
    ("1. O Cavaleiro", "notícias, movimento, chegada e iniciativa"),
    ("2. O Trevo", "oportunidade breve, sorte pequena e imprevistos"),
    ("3. O Navio", "distância, viagem, expansão e transição"),
    ("4. A Casa", "lar, segurança, intimidade e estrutura familiar"),
    ("5. A Árvore", "raízes, saúde simbólica, crescimento lento e estabilidade"),
    ("6. As Nuvens", "dúvidas, confusão, ambiguidade e falta de clareza"),
    ("7. A Cobra", "complexidade, estratégia, desejo e situações sinuosas"),
    ("8. O Caixão", "fim de etapa, pausa, perda de impulso e transformação"),
    ("9. O Buquê", "gentileza, convite, prazer, reconhecimento e harmonia"),
    ("10. A Foice", "corte, decisão rápida, separação ou mudança abrupta"),
    ("11. O Chicote", "repetição, discussão, tensão e padrões insistentes"),
    ("12. Os Pássaros", "conversa, ansiedade, troca de ideias e agitação"),
    ("13. A Criança", "começo, curiosidade, simplicidade e algo ainda imaturo"),
    ("14. A Raposa", "cautela, estratégia, trabalho e atenção aos interesses envolvidos"),
    ("15. O Urso", "força, proteção, recursos, influência e controle"),
    ("16. As Estrelas", "esperança, inspiração, orientação e visão de futuro"),
    ("17. A Cegonha", "mudança, renovação, adaptação e melhoria gradual"),
    ("18. O Cão", "amizade, lealdade, apoio e confiança"),
    ("19. A Torre", "instituições, limites, autonomia e distanciamento"),
    ("20. O Jardim", "vida social, comunidade, exposição e encontros"),
    ("21. A Montanha", "obstáculo, demora, resistência e perseverança"),
    ("22. Os Caminhos", "alternativas, escolha, bifurcação e autonomia"),
    ("23. Os Ratos", "desgaste, preocupação, perda gradual e consumo de energia"),
    ("24. O Coração", "afeto, paixão, prazer e envolvimento emocional"),
    ("25. O Anel", "compromisso, contrato, acordo e continuidade"),
    ("26. O Livro", "segredo, estudo, conhecimento e informação ainda não revelada"),
    ("27. A Carta", "mensagem, documento, notícia e comunicação formal"),
    ("28. O Homem", "figura masculina ou papel ativo, conforme a pergunta"),
    ("29. A Mulher", "figura feminina ou papel receptivo, conforme a pergunta"),
    ("30. Os Lírios", "serenidade, maturidade, paz e experiência"),
    ("31. O Sol", "sucesso, clareza, energia e resultado favorável"),
    ("32. A Lua", "sensibilidade, reconhecimento, imaginação e reputação"),
    ("33. A Chave", "solução, acesso, resposta e ponto decisivo"),
    ("34. Os Peixes", "dinheiro, fluxo, abundância e autonomia material"),
    ("35. A Âncora", "estabilidade, persistência, trabalho e segurança"),
    ("36. A Cruz", "responsabilidade, peso, provação e sentido atribuído à experiência"),
]

def montar_cigano():
    return [{
        "nome": nome, "baralho": "Baralho Cigano", "categoria": "Lenormand",
        "significado": significado,
        "invertido": None,
    } for nome, significado in CIGANO_NOMES]

TAROT = montar_tarot()
CIGANO = montar_cigano()
