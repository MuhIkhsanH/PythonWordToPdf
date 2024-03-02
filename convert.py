from docx2pdf import convert

input_docx = "input.docx"  # Ganti nama dokumen Word
output_pdf = "output.pdf"  # Ganti nama output PDF

try:
    convert(input_docx, output_pdf)
    print("Konversi berhasil!")
except Exception as e:
    print(f"Terjadi kesalahan saat melakukan konversi: {str(e)}")
