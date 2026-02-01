from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import csv


csv_file = "sample_data.csv"

names = []
scores = []

with open(csv_file, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        names.append(row["Name"])
        scores.append(int(row["Score"]))


avg_score = sum(scores) / len(scores)
max_score = max(scores)
min_score = min(scores)


pdf_file = "automated_report.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=A4)
styles = getSampleStyleSheet()

elements = []
elements.append(Paragraph("Automated Report Generation", styles["Title"]))
elements.append(Spacer(1, 12))

elements.append(Paragraph(f"Average Score: {avg_score}", styles["Normal"]))
elements.append(Paragraph(f"Highest Score: {max_score}", styles["Normal"]))
elements.append(Paragraph(f"Lowest Score: {min_score}", styles["Normal"]))
elements.append(Spacer(1, 12))


table_data = [["Name", "Score"]]
for n, s in zip(names, scores):
    table_data.append([n, s])

table = Table(table_data)
table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
    ("GRID", (0,0), (-1,-1), 1, colors.black)
]))

elements.append(table)
doc.build(elements)

print("PDF Report Generated Successfully!")
