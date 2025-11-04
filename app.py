import flask
import random
import time
import logging

app = flask.Flask(__name__)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def simular_latencia():
    time.sleep(random.uniform(0.1, 0.4))

@app.route('/api/pagos/transaccion', methods=['POST'])
def pago_transaccion():

    logging.info("Recibida solicitud de TRANSACCIÓN de pago")
    simular_latencia()
    
    if random.choice([True, False]):
        #Funciono
        logging.info("Pago APROBADO (Status 200)")
        return flask.jsonify({"mensaje": "Pago procesado exitosamente"}), 200
    else:
        #Fallo
        logging.warning("Pago RECHAZADO (Status 409)")
        return flask.jsonify({"mensaje": "Pago fallido o rechazado"}), 409

