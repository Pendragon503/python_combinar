import PyPDF2
from tkinter import Tk
from tkinter.filedialog import askopenfilenames

# Ocultar la ventana principal de Tkinter
Tk().withdraw()

# Abrir el diálogo para seleccionar los archivos PDF
file_paths = askopenfilenames(
    title="Selecciona los archivos PDF que deseas combinar",
    filetypes=[("Archivos PDF", "*.pdf")]
)

if not file_paths:
    print("No se seleccionaron archivos.")
else:
    # Crear una instancia de PdfMerger
    merger = PyPDF2.PdfMerger()

    # Agregar cada archivo seleccionado al merger
    for pdf in file_paths:
        merger.append(pdf)

    # Guardar el archivo combinado
    output_path = "archivo_combined.pdf"
    merger.write(output_path)
    merger.close()

    print(f"Archivos combinados y guardados en {output_path}")
