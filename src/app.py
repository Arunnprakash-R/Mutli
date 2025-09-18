from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from translation import translate_text
import os
import fitz  # PyMuPDF
import docx
from fpdf import FPDF

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/upload", methods=["POST"])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file:
        filename = file.filename
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
        return jsonify({"message": "File uploaded successfully", "filepath": filepath}), 200

@app.route("/translate-file", methods=["POST"])
def translate_file():
    data = request.get_json()
    filepath = data.get('filepath')
    lang = data.get('lang', 'en')

    if not filepath or not os.path.exists(filepath):
        return jsonify({"error": "File not found"}), 400

    text = ""
    if filepath.endswith('.pdf'):
        with fitz.open(filepath) as doc:
            for page in doc:
                text += page.get_text()
    elif filepath.endswith('.docx'):
        doc = docx.Document(filepath)
        for para in doc.paragraphs:
            text += para.text + '\n'
    elif filepath.endswith('.txt'):
        with open(filepath, 'r') as f:
            text = f.read()
    else:
        return jsonify({"error": "Unsupported file type"}), 400

    if not text.strip():
        return jsonify({"error": "Could not extract text from file"}), 400

    translated_text = translate_text(text, lang)

    # For simplicity, let's save the translated text to a file and make it downloadable.
    # A more robust solution would handle this differently.
    translated_filename = f"translated_{os.path.basename(filepath)}.pdf"
    translated_filepath = os.path.join(UPLOAD_FOLDER, translated_filename)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, translated_text.encode('latin-1', 'replace').decode('latin-1'))
    pdf.output(translated_filepath)

    return jsonify({"translated_text": translated_text, "download_path": translated_filepath})

@app.route("/download/<filename>")
def download_file(filename):
    path = os.path.join(UPLOAD_FOLDER, filename)
    return send_file(path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
