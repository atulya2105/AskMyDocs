from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", size=12)

text = """
Artificial Intelligence (AI)

Artificial Intelligence is a branch of computer science that focuses on
creating machines capable of performing tasks that require human intelligence.

Examples include:
- Self driving cars
- Virtual assistants
- Recommendation systems

Machine learning is a subset of AI.
"""

for line in text.split("\n"):
    pdf.cell(200, 10, txt=line, ln=True)

pdf.output("New.pdf")

print("PDF created successfully!")