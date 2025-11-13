import pandas as pd

# ================================
#   1. DATOS DEL CUADRO
# ================================

rows = [
    # Rol del Estado / Economía
    ("Rol del Estado / Economía", "Jeannette Jara",
     "Estado regulador, articulador e inversionista en algunos sectores; eje en «Un Estado que le cumple a las personas»."),
    ("Rol del Estado / Economía", "José Antonio Kast",
     "Énfasis en libre mercado, orden y estabilidad económica, con menor intervención estatal."),
    ("Rol del Estado / Economía", "Johannes Kaiser",
     "Estado austero, transparente y facilitador; impuestos bajos y mínima burocracia."),
    ("Rol del Estado / Economía", "Evelyn Matthei",
     "Estado que acompaña y regula; reducción de ministerios y eficiencia del gasto público."),

    # Seguridad / Orden Público
    ("Seguridad / Orden Público", "Jeannette Jara",
     "Seguridad, justicia y defensa como eje central."),
    ("Seguridad / Orden Público", "José Antonio Kast",
     "«Plan Implacable» contra crimen organizado; énfasis en orden."),
    ("Seguridad / Orden Público", "Johannes Kaiser",
     "Enfoque institucional liberal; cumplimiento estricto de la ley."),
    ("Seguridad / Orden Público", "Evelyn Matthei",
     "«Toda la fuerza del Estado al resguardo de la seguridad»."),

    # Trabajo / Empleo / Protección Social
    ("Trabajo / Empleo / Protección Social", "Jeannette Jara",
     "Crecimiento inclusivo, empleo de calidad y fortalecimiento de protección social."),
    ("Trabajo / Empleo / Protección Social", "José Antonio Kast",
     "Crecimiento económico como base para creación de empleo."),
    ("Trabajo / Empleo / Protección Social", "Johannes Kaiser",
     "Flexibilización del mercado laboral y uso de vouchers."),
    ("Trabajo / Empleo / Protección Social", "Evelyn Matthei",
     "Corresponsabilidad Estado–privados; eficiencia del gasto social."),

    # Educación / Salud / Bienestar
    ("Educación / Salud / Bienestar", "Jeannette Jara",
     "Fortalecimiento de educación y salud públicas."),
    ("Educación / Salud / Bienestar", "José Antonio Kast",
     "Menor desarrollo programático público en este eje."),
    ("Educación / Salud / Bienestar", "Johannes Kaiser",
     "Modelo liberal con vouchers y énfasis privado."),
    ("Educación / Salud / Bienestar", "Evelyn Matthei",
     "Estado articulador, innovación público–privada."),

    # Minería / Energía
    ("Minería / Energía", "Jeannette Jara",
     "Colaboración estatal–privada en litio y minería."),
    ("Minería / Energía", "José Antonio Kast",
     "Impulso a inversión en recursos naturales."),
    ("Minería / Energía", "Johannes Kaiser",
     "Privatización parcial/total de CODELCO; Fondo Soberano Minero."),
    ("Minería / Energía", "Evelyn Matthei",
     "Estrategia Nacional de Minerales Críticos con inversión privada."),
]

df = pd.DataFrame(rows, columns=["Temática", "Candidato", "Propuesta"])


# ================================
#   2. EXPORTACIONES
# ================================

# CSV
df.to_csv("cuadro_comparativo.csv", index=False)

# Excel
df.to_excel("cuadro_comparativo.xlsx", index=False)

# PDF (simple)
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()
doc = SimpleDocTemplate("cuadro_comparativo.pdf", pagesize=letter)
elements = []

elements.append(Paragraph("<b>Cuadro comparativo de propuestas</b>", styles["Title"]))

table_data = [["Temática", "Candidato", "Propuesta"]]
table_data += rows

t = Table(table_data, colWidths=[120, 100, 300])
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
    ("GRID", (0,0), (-1,-1), 0.4, colors.black),
    ("VALIGN", (0,0), (-1,-1), "TOP")
]))

elements.append(t)
doc.build(elements)


# ================================
#   3. VISUALIZACIÓN LOCAL
# ================================
print(df)
