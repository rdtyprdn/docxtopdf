from docx2pdf import convert
import os

def word_to_pdf(input_path, output_path=None):
    if not os.path.exists(input_path):
        print("The file does not exist.")
        return

    try:
        convert(input_path, output_path)
        print(f"Successfully converted '{input_path}' to PDF.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
   word_file = r"contoh.docx" #aint gonna tell you my file
   output_dir = r"your directory" #aint gonna tell you my file directory 
   word_to_pdf(word_file, output_dir)
