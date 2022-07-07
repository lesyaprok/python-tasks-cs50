from fpdf import FPDF

def main():
    user_name = input("Name: ")
    shirtificate = Shirtificate(user_name)
    shirtificate.create_pdf()

class Shirtificate:
    def __init__(self, name):
        self.name = name
    def create_pdf(self):
        pdf = FPDF(orientation='portrait', unit='mm', format=(210, 297))
        pdf.add_page()
        pdf.set_font("helvetica", "B", 38)
        pdf.cell(0, 30, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")
        pdf.image("./shirtificate.png", 0, int(297/5), 210)
        pdf.set_font("helvetica", "B", 24)
        pdf.set_text_color(255)
        pdf.cell(0, 200, f"{self.name} took CS50", new_x="LMARGIN", new_y="NEXT", align="C")
        pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
