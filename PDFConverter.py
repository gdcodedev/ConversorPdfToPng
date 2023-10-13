

import fitz
import os

def convert_pdf_to_png(pdf_path, output_dir):

    pdf_filename = os.path.splitext(os.path.basename(pdf_path))[0]


    pdf_document = fitz.open(pdf_path)


    for page_number in range(pdf_document.page_count):

        page = pdf_document.load_page(page_number)


        image = page.get_pixmap()


        image_filename = f'{pdf_filename}{page_number + 1}.png'
        image_path = os.path.join(output_dir, image_filename)


        image.save(image_path)


    pdf_document.close()

def main():
    input_pdf_directory = 'C:/Users/guilh/OneDrive/Área de Trabalho/Treinamento Valide/Holerite'
    output_png_directory = 'C:/Users/guilh/OneDrive/Área de Trabalho/Treinamento Valide/Holerite'


    if not os.path.exists(output_png_directory):
        os.makedirs(output_png_directory)


    for filename in os.listdir(input_pdf_directory):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(input_pdf_directory, filename)
            convert_pdf_to_png(pdf_path, output_png_directory)

if __name__ == "__main__":
    main()
