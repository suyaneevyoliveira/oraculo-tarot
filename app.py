import streamlit as st
from baralhos import TAROT, CIGANO
from sorteio import sortear_cartas
from interpretacoes import interpretar, sintetizar

st.set_page_config(
    page_title="Oráculo | Tarot & Baralho Cigano",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Manrope:wght@300;400;500;600;700&display=swap');
.stApp {
  background: radial-gradient(ellipse at 50% -10%, rgba(103, 44, 88, .30), transparent 45%),
              linear-gradient(160deg, #100d16 0%, #17101e 55%, #100d16 100%);
  color: #f4eee4; font-family: 'Manrope', sans-serif;
}
h1, h2, h3 { font-family: 'Cormorant Garamond', serif !important; color: #f4dfad !important; }
.hero { border: 1px solid rgba(216,182,106,.35); border-radius: 20px; padding: 28px 30px; margin-bottom: 22px;
        background: linear-gradient(120deg, rgba(91,34,65,.35), rgba(28,19,35,.7)); }
.eyebrow { text-transform: uppercase; letter-spacing: .24em; color: #d8b66a; font-size: .72rem; }
.hero h1 { font-size: 3rem; margin: .2rem 0; }
.hero p { color: #d3c8d4; max-width: 760px; margin-bottom: 0; }
div.stButton > button { background: linear-gradient(100deg, #8c3154, #632641); color: #fff7e8;
  border: 1px solid rgba(216,182,106,.65); border-radius: 12px; font-weight: 600; }
div.stButton > button:hover { border-color: #f0d38c; color: white; }
.card { min-height: 178px; padding: 18px 12px; border-radius: 14px; border: 1px solid rgba(216,182,106,.65);
  background: linear-gradient(155deg, #382039, #1b1523 72%); box-shadow: 0 8px 24px rgba(0,0,0,.24);
  text-align: center; display:flex; flex-direction:column; justify-content:center; }
.card .symbol { color: #d8b66a; font-size: 1.25rem; margin-bottom: 10px; }
.card .card-icon { font-size: 2rem; line-height: 1.15; margin: 3px 0 12px; filter: drop-shadow(0 0 10px rgba(216,182,106,.16)); }
.card .name { font-family: 'Cormorant Garamond', serif; font-size: 1.3rem; color: #f6e5ba; line-height: 1.15; }
.card .orientation { font-size: .72rem; letter-spacing: .12em; color: #d7c5d7; margin-top: 9px; text-transform: uppercase; }
section[data-testid="stSidebar"] { background: #120e18; border-right: 1px solid rgba(216,182,106,.18); }
</style>
""", unsafe_allow_html=True)


def icone_carta(carta):
    """Símbolo visual temporário por carta; pode ser substituído por ilustrações licenciadas/originais."""
    nome = carta["nome"]
    if carta["baralho"] == "Tarot":
        arcanos = {
            "O Louco": "🪶", "O Mago": "🪄", "A Sacerdotisa": "☾",
            "A Imperatriz": "❀", "O Imperador": "♜", "O Hierofante": "🗝",
            "Os Enamorados": "♡", "O Carro": "⚑", "A Justiça": "⚖",
            "O Eremita": "🏮", "A Roda da Fortuna": "☸", "A Força": "🦁",
            "O Enforcado": "⟡", "A Morte": "☠", "A Temperança": "⚗",
            "O Diabo": "♆", "A Torre": "ϟ", "A Estrela": "✧",
            "A Lua": "☽", "O Sol": "☼", "O Julgamento": "♧", "O Mundo": "◎",
        }
        if nome in arcanos:
            return arcanos[nome]
        if nome.endswith(" de Paus"):
            return "♣"
        if nome.endswith(" de Copas"):
            return "♡"
        if nome.endswith(" de Espadas"):
            return "⚔"
        if nome.endswith(" de Ouros"):
            return "✥"
        return "✦"
    lenormand = [
        ("Cavaleiro", "🐎"), ("Trevo", "☘"), ("Navio", "⚓"),
        ("Casa", "⌂"), ("Árvore", "♧"), ("Nuvens", "☁"),
        ("Cobra", "〰"), ("Caixão", "▣"), ("Buquê", "❀"),
        ("Foice", "⚒"), ("Chicote", "≋"), ("Pássaros", "♧"),
        ("Criança", "✿"), ("Raposa", "🦊"), ("Urso", "🐻"),
        ("Estrelas", "✧"), ("Cegonha", "🕊"), ("Cão", "🐕"),
        ("Torre", "♜"), ("Jardim", "❦"), ("Montanha", "▲"),
        ("Caminhos", "⑂"), ("Ratos", "⌁"), ("Coração", "♡"),
        ("Anel", "◉"), ("Livro", "▤"), ("Carta", "✉"),
        ("Homem", "♙"), ("Mulher", "♙"), ("Lírios", "⚜"),
        ("Sol", "☼"), ("Lua", "☾"), ("Chave", "⚿"),
        ("Peixes", "♓"), ("Âncora", "⚓"), ("Cruz", "✝"),
    ]
    for trecho, simbolo in lenormand:
        if trecho.lower() in nome.lower():
            return simbolo
    return "✧"


if "historico" not in st.session_state:
    st.session_state.historico = []
if "tiragem_atual" not in st.session_state:
    st.session_state.tiragem_atual = None

st.markdown("""
<div class="hero">
  <div class="eyebrow">✦ espaço de reflexão ✦</div>
  <h1>Oráculo</h1>
  <p>Tarot & Baralho Cigano — configure sua tiragem, revele as cartas e explore os significados e as relações entre elas.</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## ✦ Configurar tiragem")
    baralho_escolhido = st.radio(
        "Baralho", ["Tarot", "Baralho Cigano", "Ambos"], index=2,
        help="A quantidade selecionada será aplicada separadamente a cada baralho escolhido."
    )
    assunto = st.selectbox("✧ Assunto", ["Amor", "Família", "Trabalho", "Estudos", "Geral"])
    pergunta = st.text_area("☾ Pergunta ou intenção (opcional)", placeholder="Escreva sua pergunta...", height=100)
    quantidade = st.slider("✦ Cartas por baralho", min_value=1, max_value=15, value=3)
    inversoes = st.checkbox("Permitir cartas invertidas no Tarot", value=True, disabled=(baralho_escolhido == "Baralho Cigano"))
    st.caption("O assunto e a pergunta orientam a interpretação, mas não influenciam quais cartas são sorteadas.")
    sortear = st.button("✦ Revelar cartas", use_container_width=True)

if sortear:
    tiragens = {}
    if baralho_escolhido in ("Tarot", "Ambos"):
        tiragens["Tarot"] = sortear_cartas(TAROT, quantidade, inversoes)
    if baralho_escolhido in ("Baralho Cigano", "Ambos"):
        tiragens["Baralho Cigano"] = sortear_cartas(CIGANO, quantidade, False)
    registro = {
        "assunto": assunto, "pergunta": pergunta.strip(),
        "baralho": baralho_escolhido, "tiragens": tiragens,
    }
    st.session_state.tiragem_atual = registro
    st.session_state.historico.insert(0, registro)

atual = st.session_state.tiragem_atual
if atual is None:
    st.markdown("### Antes de começar")
    st.write("Escolha o baralho, o assunto e a quantidade na barra lateral.")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="card"><div class="symbol">☾</div><div class="name">Tarot</div><div class="orientation">78 cartas</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="card"><div class="symbol">✧</div><div class="name">Baralho Cigano</div><div class="orientation">36 cartas</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="card"><div class="symbol">✦</div><div class="name">Leitura combinada</div><div class="orientation">Dois sistemas</div></div>', unsafe_allow_html=True)
else:
    st.markdown(f"### Sua tiragem · {atual['assunto']}")
    if atual["pergunta"]:
        st.info(f"**Pergunta:** {atual['pergunta']}")
    todas = []
    for nome_baralho, cartas in atual["tiragens"].items():
        st.markdown(f"#### ✧ {nome_baralho}")
        cols = st.columns(min(5, len(cartas)))
        for i, carta in enumerate(cartas):
            todas.append(carta)
            with cols[i % len(cols)]:
                st.markdown(
                    f'<div class="card"><div class="symbol">✦</div><div class="name">{carta["nome"]}</div><div class="orientation">{carta["orientacao"]}</div></div>',
                    unsafe_allow_html=True
                )
        st.markdown("##### Interpretação individual")
        for i, carta in enumerate(cartas, start=1):
            leitura = interpretar(carta, atual["assunto"], posicao=f"carta {i}")
            with st.expander(f"{i}. {leitura['titulo']}", expanded=False):
                st.markdown(f"**Significado simbólico:** {leitura['significado'].capitalize()}.")
                st.markdown(f"**No tema {atual['assunto'].lower()}:** {leitura['contexto']}")
                st.markdown(f"**Pergunta para reflexão:** {leitura['reflexao']}")
                st.markdown(f"**Possível ação prática:** {leitura['acao']}")
    st.markdown("### Leitura do conjunto")
    st.caption("A síntese considera a sequência de cartas, padrões simbólicos, orientações e o tema selecionado. É uma leitura interpretativa, não uma previsão garantida.")
    st.markdown(sintetizar(todas, atual["assunto"], atual["pergunta"]))

st.divider()
st.markdown("### Histórico desta sessão")
if not st.session_state.historico:
    st.caption("As tiragens realizadas nesta sessão aparecerão aqui.")
else:
    for idx, registro in enumerate(st.session_state.historico):
        total = sum(len(v) for v in registro["tiragens"].values())
        nomes = [c["nome"] for cartas in registro["tiragens"].values() for c in cartas]
        with st.expander(f"{idx + 1}. {registro['assunto']} · {registro['baralho']} · {total} cartas"):
            if registro["pergunta"]:
                st.write(f"**Pergunta:** {registro['pergunta']}")
            st.write(" · ".join(nomes))
    if st.button("Limpar histórico da sessão"):
        st.session_state.historico = []
        st.session_state.tiragem_atual = None
        st.rerun()

st.caption("Uso reflexivo e simbólico. As cartas não comprovam sentimentos de terceiros nem garantem acontecimentos.")
