from flask import Flask, jsonify
from flask_cors import CORS  
import random

app = Flask(__name__)
CORS(app)  


motivational_quotes = [
    "El éxito es la suma de pequeños esfuerzos repetidos día tras día.",
    "No importa lo lento que vayas, siempre y cuando no te detengas.",
    "El único límite para nuestra realización de mañana será nuestras dudas de hoy.",
    "La mejor manera de predecir el futuro es crearlo.",
    "No te rindas, comienza ahora mismo, el futuro es prometedor.",
    "El esfuerzo constante es la clave para desbloquear nuestro potencial.",
    "Cada día es una nueva oportunidad para cambiar tu vida.",
    "La persistencia es el camino al éxito.",
    "Cree que puedes y ya estarás a medio camino.",
    "El único modo de hacer un gran trabajo es amar lo que haces."
]

@app.route('/get-quote', methods=['GET'])
def get_quote():
    quote = random.choice(motivational_quotes)
    return jsonify({"quote": quote})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)