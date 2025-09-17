from flask import Flask, request, jsonify
from translation import translate_text

app = Flask(__name__)

@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response

@app.route("/translate", methods=["GET"])
def translate():
    text = request.args.get("text", "Welcome")
    lang = request.args.get("lang", "en")

    if not text:
        return jsonify({"error": "Text to translate is required."}), 400

    translated_text = translate_text(text, lang)

    return jsonify({"translated_text": translated_text})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
