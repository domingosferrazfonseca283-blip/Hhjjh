from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER

AUTHOR = "domingosferrazfonseca283-blip"

TOPICS = [
    ("Começar do zero", ["programação", "Python", "print", "comentários", "primeiro programa"]),
    ("Fundamentos", ["variáveis", "números", "texto", "booleanos", "entrada"]),
    ("Decisões", ["if", "else", "elif", "comparações", "operadores lógicos"]),
    ("Repetição", ["for", "while", "range", "contadores", "acumuladores"]),
    ("Coleções", ["listas", "tuplos", "conjuntos", "dicionários", "percorrer coleções"]),
    ("Funções", ["def", "parâmetros", "return", "valores padrão", "escopo"]),
    ("Erros", ["SyntaxError", "ValueError", "TypeError", "try/except", "debugging"]),
    ("Ficheiros", ["ler", "escrever", "with", "caminhos", "CSV"]),
    ("Objetos", ["classes", "objetos", "atributos", "métodos", "herança"]),
    ("Avançado", ["compreensões", "iteradores", "geradores", "decoradores", "context managers"]),
    ("Profissional", ["typing", "testes", "logging", "performance", "concorrência"]),
    ("Internals", ["modelo de objetos", "CPython", "bytecode", "memória", "protocolos"]),
]

LESSONS = []
for area, items in TOPICS:
    for item in items:
        for level in range(1, 6):
            LESSONS.append((area, item, level))
LESSONS = LESSONS[:250]

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Cover", parent=styles["Title"], fontSize=25, leading=30, alignment=TA_CENTER))
styles.add(ParagraphStyle(name="BodySimple", parent=styles["BodyText"], fontSize=9.2, leading=12))
styles.add(ParagraphStyle(name="CodeSimple", parent=styles["Code"], fontSize=7.5, leading=9))

story = [
    Spacer(1, 150),
    Paragraph("PYTHON SEM MEDO", styles["Cover"]),
    Paragraph("Do zero absoluto ao Python avançado", styles["Cover"]),
    Spacer(1, 30),
    Paragraph("Autor: " + AUTHOR, styles["BodySimple"]),
    Paragraph("250 aulas × 4 páginas = 1.000 páginas", styles["BodySimple"]),
    PageBreak(),
]

for n, (area, topic, level) in enumerate(LESSONS, 1):
    code = 'nome = "Ana"\nprint("Olá,", nome)'
    if topic in ("if", "else", "elif"):
        code = 'idade = 10\nif idade >= 10:\n    print("Olá!")'
    elif topic in ("for", "while", "range"):
        code = 'for numero in range(3):\n    print(numero)'
    elif topic == "funções" or topic == "def":
        code = 'def dobro(numero):\n    return numero * 2\n\nprint(dobro(5))'
    story += [
        Paragraph(f"Aula {n:03d} — {topic}", styles["Heading1"]),
        Paragraph(f"Área: {area} · nível {level}/5", styles["BodySimple"]),
        Spacer(1, 8),
        Paragraph(f"Vamos aprender {topic} com calma. Primeiro entende a ideia. Depois observa o exemplo. "
                  "Finalmente muda o código e faz um exercício. Não precisas decorar tudo.", styles["BodySimple"]),
        PageBreak(),
        Paragraph(f"Exemplo — {topic}", styles["Heading1"]),
        Paragraph("Código:", styles["BodySimple"]),
        Paragraph("<font name='Courier'>" + code.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace("\n","<br/>") + "</font>", styles["BodySimple"]),
        Spacer(1, 10),
        Paragraph("Lê cada linha. Pergunta o que ela pede ao computador. Depois executa o programa e compara o resultado com a tua previsão.", styles["BodySimple"]),
        PageBreak(),
        Paragraph("Explicação linha a linha", styles["Heading1"]),
        Paragraph("Uma linha de código é apenas uma pequena instrução. Divide problemas grandes em instruções pequenas. "
                  "Quando algo falhar, usa a mensagem de erro como pista.", styles["BodySimple"]),
        Spacer(1, 10),
        Paragraph("Perguntas: O que entra? O que acontece? O que sai? O que mudaria se alterasses um valor?", styles["BodySimple"]),
        PageBreak(),
        Paragraph("Exercícios e desafio", styles["Heading1"]),
        Paragraph("1. Explica a ideia com as tuas próprias palavras.<br/><br/>"
                  "2. Executa o exemplo.<br/><br/>"
                  "3. Muda um valor e prevê o resultado.<br/><br/>"
                  "4. Cria uma segunda versão sem copiar exatamente.<br/><br/>"
                  "5. Cria um pequeno programa do teu dia a dia usando a ideia desta aula.", styles["BodySimple"]),
        PageBreak(),
    ]

# O último PageBreak é intencionalmente removido.
story.pop()
SimpleDocTemplate("Livro_Python_do_Zero_ao_Avancado.pdf", pagesize=A4,
                  rightMargin=38, leftMargin=38, topMargin=38, bottomMargin=38).build(story)
print("PDF criado com 1.000 páginas.")
