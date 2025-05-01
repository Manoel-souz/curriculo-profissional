from fpdf import FPDF
from fpdf.enums import XPos, YPos
import textwrap

class PDF(FPDF):
    """
    Classe personalizada para geração de currículo em PDF.
    Herda da classe FPDF e implementa formatação específica para currículo.
    """
    def __init__(self):
        super().__init__(orientation='P', unit='mm', format='A4')
        self.add_page()
        self.set_margins(10, 10, 10)  # Ajustando as margens
        self.set_auto_page_break(auto=True, margin=10)

    def header(self):
        """
        Define o cabeçalho do currículo com nome, título e informações de contato.
        Inclui links clicáveis para LinkedIn e GitHub.
        """
        verde = (0, 100, 0)
        azul_link = (0, 0, 255)  # Cor azul para links
        
        # Nome e Título mais compactos
        self.set_font('Helvetica', 'B', 20)
        self.set_text_color(*verde)
        self.cell(0, 8, "MANOEL SOUZA", align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        
        self.set_font('Helvetica', 'B', 16)
        self.cell(0, 6, "Desenvolvedor Backend (em transição de carreira)", align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        
        # Contato em duas linhas
        self.set_font('Helvetica', '', 11)
        self.set_text_color(0, 0, 0)
        self.cell(0, 4, "11 95911-4346 | manu0019@hotmail.com | Itapecerica da Serra, São Paulo", align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        
        # Links clicáveis
        self.set_text_color(*azul_link)
        self.set_font('Helvetica', '', 11)
        
        # Calculando posições para centralizar os links
        linkedin_text = "LinkedIn: linkedin.com/in/manoel-sz"
        github_text = "GitHub: github.com/Manoel-souz"
        espacamento = " | "
        
        texto_total = linkedin_text + espacamento + github_text
        largura_total = self.get_string_width(texto_total)
        posicao_x = (210 - largura_total) / 2  # 210 é a largura da página A4 em mm
        
        # LinkedIn
        self.set_x(posicao_x)
        self.cell(self.get_string_width(linkedin_text), 4, linkedin_text, 
                 link="https://linkedin.com/in/manoel-sz")
        
        # Separador
        self.cell(self.get_string_width(espacamento), 4, espacamento)
        
        # GitHub
        self.cell(self.get_string_width(github_text), 4, github_text, 
                 link="https://github.com/Manoel-souz", 
                 new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        
        # Resetando a cor do texto
        self.set_text_color(0, 0, 0)
        
        # Linha decorativa
        self.set_draw_color(*verde)
        self.line(10, self.get_y() + 2, 200, self.get_y() + 2)
        self.ln(6)  # Aumentado o espaçamento após a linha

    def section_title(self, title):
        """
        Formata o título de uma seção do currículo.
        
        Args:
            title (str): Título da seção
        """
        self.ln(3)  # Aumentado o espaçamento após o título
        self.set_font('Helvetica', 'B', 14)
        self.set_text_color(0, 100, 0)
        self.cell(0, 5, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_text_color(0, 0, 0)
        self.ln(3)  # Aumentado o espaçamento após o título

    def section_body(self, text):
        """
        Formata o corpo de texto de uma seção.
        
        Args:
            text (str): Texto a ser formatado
        """
        self.set_font('Helvetica', '', 11)
        lines = textwrap.wrap(text, width=100)
        for line in lines:
            self.cell(0, 4, line, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(4)  # Aumentado o espaçamento após o corpo do texto

    def add_list_section(self, title, items):
        """
        Adiciona uma seção com lista de itens.
        
        Args:
            title (str): Título da seção
            items (list): Lista de itens a serem adicionados
        """
        self.section_title(title)
        self.set_font('Helvetica', '', 11)
        for item in items:
            self.cell(5)
            lines = textwrap.wrap(f"{item}", width=90)
            for i, line in enumerate(lines):
                if i > 0:
                    self.cell(5)
                self.cell(0, 4, line, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(4)  # Aumentado o espaçamento após a lista

    def add_experience(self, experiencias):
        """
        Adiciona a seção de experiência profissional.
        
        Args:
            experiencias (list): Lista de dicionários contendo as experiências profissionais
        """
        self.section_title("Experiência Profissional")
        for exp in experiencias:
            self.set_font('Helvetica', 'B', 12)
            self.cell(0, 4, exp["titulo"], new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            
            self.set_font('Helvetica', 'I', 11)
            self.cell(0, 4, exp["periodo"], new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            
            self.set_font('Helvetica', '', 11)
            for d in exp["descricao"]:
                self.cell(5)
                lines = textwrap.wrap(f"- {d}", width=90)
                for i, line in enumerate(lines):
                    if i > 0:
                        self.cell(5)
                    self.cell(0, 4, line, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            self.ln(4)  # Aumentado o espaçamento entre experiências

# Dados do currículo
resumo = (
    "Profissional com experiência em Marketing Digital e gestão de projetos, em transição para Desenvolvimento Backend. "
    "Conhecimento prático em desenvolvimento de sistemas e APIs através da Options Tech. "
    "Familiaridade com Node.js, JavaScript/TypeScript, PostgreSQL e Git."
)

experiencias = [
    {
        "titulo": "Fundador & Desenvolvedor | Options Tech",
        "periodo": "2020 - Atualmente",
        "descricao": [
            "Eu e minha equipe desenvolvemos sistemas personalizados, soluções de automação e aplicativos para diversos clientes.",
            "Desenvolvi e mantive APIs RESTful utilizando Node.js e TypeScript.",
            "Trabalhei com bancos de dados relacionais (PostgreSQL) e Git para controle de versão."
        ]
    },
    {
        "titulo": "Assistente de Marketing | Grupo Raotes - Embu das Artes, São Paulo",
        "periodo": "2022 - 2025",
        "descricao": [
            "Criação de sites, gerenciamento de redes sociais, campanhas, endomarketing e análise de KPIs."
        ]
    }
]

formacao = (
    "Marketing Digital | Estácio (2021 - 2023)\n"
    "Base em análise de mercado, comportamento do consumidor e estratégias de comunicação."
)

habilidades = [
    "Linguagens e Frameworks: Node.js (Básico), TypeScript (Básico), JavaScript (Básico), Python (Básico), NestJS (Básico)",
    "Bancos de Dados: PostgreSQL (Noções)",
    "Controle de Versão: Git (Intermediário)",
    "Desenvolvimento Web: APIs RESTful, Desenvolvimento de Sites",
    "Outras: Clean Code, Testes Automatizados, Análise de KPIs, Pacote Office, Photoshop"
]

idiomas = "Inglês: Intermediário"

sobre = (
    "Apaixonado por tecnologia e aprendizado contínuo. Experiência em marketing e desenvolvimento na Options Tech "
    "proporciona visão única para criar soluções eficientes. Me comunico bem, sou colaborativo e possuo grande vontade de aprender."
)

# Criando o PDF
pdf = PDF()

# Adicionando conteúdo
pdf.section_title("Resumo Profissional")
pdf.section_body(resumo)

pdf.add_experience(experiencias)

pdf.section_title("Formação Acadêmica")
pdf.section_body(formacao)

pdf.add_list_section("Habilidades Técnicas", habilidades)

pdf.section_title("Idiomas")
pdf.section_body(idiomas)

pdf.section_title("Sobre Mim")
pdf.section_body(sobre)

# Salvando o arquivo
output_path = "Curriculo_Manoel_Souza.pdf"
pdf.output(output_path)

print(f"Currículo gerado com sucesso! Arquivo salvo como: {output_path}")
