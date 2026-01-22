from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Input and output files
input_file = "data.txt"
output_pdf = "report.pdf"

names = []
marks = []

# ===== Read data from file =====
with open(input_file, "r") as file:
    lines = file.readlines()

for line in lines[1:]:  # skip header
    name, mark = line.strip().split(",")
    names.append(name)
    marks.append(int(mark))

# ===== Analyze data =====
total_students = len(marks)
average_marks = sum(marks) / total_students
highest_marks = max(marks)
lowest_marks = min(marks)

# ===== Create PDF =====
c = canvas.Canvas(output_pdf, pagesize=A4)
width, height = A4

y = height - 50

c.setFont("Helvetica-Bold", 16)
c.drawString(50, y, "Student Marks Report")
y -= 40

c.setFont("Helvetica", 12)
c.drawString(50, y, f"Total Students: {total_students}")
y -= 25

c.drawString(50, y, f"Average Marks: {average_marks:.2f}")
y -= 25

c.drawString(50, y, f"Highest Marks: {highest_marks}")
y -= 25

c.drawString(50, y, f"Lowest Marks: {lowest_marks}")
y -= 40

c.setFont("Helvetica-Bold", 12)
c.drawString(50, y, "Student Details:")
y -= 25

c.setFont("Helvetica", 11)

for i in range(total_students):
    c.drawString(60, y, f"{names[i]}  -  {marks[i]}")
    y -= 20

    if y < 50:
        c.showPage()
        y = height - 50

c.save()

print("PDF report generated successfully:", output_pdf)
