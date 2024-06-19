from flask import jsonify

from main import app
from main.utils.log import LoggerService

logger = LoggerService(name="probe")


@app.get("/ping")
def ping():
    logger.info(message='testing logger', data={'is_good?': 'yes'})
    return jsonify({"message": "pong"})
