import argparse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


def generate_resume(output_file, font_size, font_color, background_color):
    # Set up the document
    doc = SimpleDocTemplate(output_file, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # Customize font size and color
    styles["Normal"].fontSize = font_size
    styles["Normal"].textColor = colors.HexColor(font_color)
    styles["Heading2"].fontSize = font_size + 2
    styles["Heading2"].textColor = colors.HexColor(font_color)
    styles["Title"].fontSize = font_size + 4
    styles["Title"].textColor = colors.HexColor(font_color)

    # Background color setup
    def add_background(canvas, doc):
        canvas.saveState()
        canvas.setFillColor(colors.HexColor(background_color))
        canvas.rect(0, 0, letter[0], letter[1], fill=True, stroke=False)
        canvas.restoreState()

    # Name and Contact Information
    name = Paragraph("KANDARP JANI", styles["Title"])
    elements.append(name)

    contact_info = Paragraph(
        "Parsa, Siddharth Nagar • XXXXXXXXXX • XXXXXXXXX@iitgn.ac.in",
        styles["Normal"],
    )
    elements.append(contact_info)
    elements.append(Spacer(1, 20))

    # Skills
    elements.append(Paragraph("Skills", styles["Heading2"]))
    skills = Paragraph(
        "- Software Development<br/>"
        "- Project Management<br/>"
        "- Machine Learning<br/>"
        "- Robotics and Automation<br/>"
        "- CAD",
        styles["Normal"],
    )
    elements.append(skills)
    elements.append(Spacer(1, 20))

    # Education
    elements.append(Paragraph("Education", styles["Heading2"]))
    education = Paragraph(
        "Master of Engineering in Computer Science and Engineering, Oct 2022 - Present<br/>"
        "Bachelor of Science in Civil Engineering, Aug 2018 - Apr 2022<br/>"
        "Siddharth Public School, <br/><br/>",
        styles["Normal"],
    )
    elements.append(education)
    elements.append(Spacer(1, 20))

    # Experience
    elements.append(Paragraph("Experience", styles["Heading2"]))
    experience = Paragraph(
        "<b>Engineering Executive</b>, Borelle Technologies, Jan 2023 - Present<br/>"
        "- Implemented cost-effective solutions, reducing project expenses by 20%.<br/>"
        "- Streamlined project workflows, improving overall efficiency by 25%.<br/>"
        "- Delivered complex projects on time and within budget.<br/><br/>"
        "<b>Project Engineer</b>, Salford & Co, Mar 2021 - Dec 2022<br/>"
        "- Reduced delivery timelines by 30%.<br/>"
        "- Improved project accuracy by 15% using new tools.<br/>"
        "- Enhanced project success rates by 10% through team collaboration.",
        styles["Normal"],
    )
    elements.append(experience)
    elements.append(Spacer(1, 20))

    # Build the PDF with the background color
    doc.build(elements, onFirstPage=add_background, onLaterPages=add_background)
    print(f"Resume saved as {output_file}")


if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Generate a customizable resume.")
    parser.add_argument("--output", type=str, default="customized_resume.pdf", help="Output file name (default: customized_resume.pdf)")
    parser.add_argument("--font-size", type=int, default=12, help="Font size (default: 12)")
    parser.add_argument("--font-color", type=str, default="#000000", help="Font color in hex code (default: #000000)")
    parser.add_argument("--background-color", type=str, default="#FFFFFF", help="Background color in hex code (default: #FFFFFF)")

    # Parse arguments
    args = parser.parse_args()

    # Generate the resume with provided customization options
    generate_resume(args.output, args.font_size, args.font_color, args.background_color)
