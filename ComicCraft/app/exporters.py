from fpdf import FPDF
import os
from datetime import datetime


def save_pdf(layout):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    export_folder = "static/exports"
    os.makedirs(export_folder, exist_ok=True)

    for panel in layout:
        pdf.add_page()

        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, f"Panel {panel['panel']}", ln=True)

        if panel.get("image"):
            pdf.image(panel["image"], x=10, y=30, w=180)

        pdf.set_y(140)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 8, panel.get("text", ""))

    filename = f"comic_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    filepath = os.path.join(export_folder, filename)

    pdf.output(filepath)

    return filepath