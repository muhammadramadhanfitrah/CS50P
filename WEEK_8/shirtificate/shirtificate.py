from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 48)
        self.cell(0, 30, "CS50 Shirtificate", ln=True, align="C")
        self.ln(10)

    def add_shirt(self, name):
        self.image("./shirtificate.png", x=(210 - 190) / 2, y=70, w=190)
        self.set_font("helvetica", "B", 24)
        self.set_text_color(255, 255, 255)
        self.set_y(140)
        self.cell(0, 10, f"{name} took CS50", align="C")


def main():
    name = input("Name: ")
    create_shirtificate(name)


def create_shirtificate(name):
    pdf = PDF(orientation="portrait", format="A4")
    pdf.add_page()
    pdf.add_shirt(name)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
