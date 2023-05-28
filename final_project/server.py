import machinetranslation
from machinetranslation.translator import eng_to_fr, fr_to_eng
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def eng_to_fr():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    result = machinetranslation.translator.eng_to_fr(textToTranslate)
    return result

@app.route("/frenchToEnglish")
def fr_to_eng():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    result = machinetranslation.translator.fr_to_eng(textToTranslate)
    return result

@app.route("/")
def renderIndexPage():
    # Write the code to render templatedd
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
