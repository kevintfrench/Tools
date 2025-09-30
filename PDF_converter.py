
pip install pdf2image pytesseract fpdf

from pdf2image import convert_from_path
import pytesseract
from fpdf import FPDF

# Convert PDF to images
images = convert_from_path("2025-07-12_06-50-18.pdf", dpi=300)

# Extract text
lines = []
for img in images:
    text = pytesseract.image_to_string(img)
    lines.extend([line.strip() for line in text.split("\n") if line.strip()])

# Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
for line in lines:
    pdf.multi_cell(0, 10, line)

pdf.output("quizlet_flashcards.pdf")