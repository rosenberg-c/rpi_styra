from flask import Flask, jsonify, request

from requests.energenie.on_off.contol import energenie_control
from requests.support import ENERGENIE_ENDPOINT


def endpoint_energenie_on(app: Flask):
    @app.route(ENERGENIE_ENDPOINT + "/on/<data>", methods=["POST"])
    def request_energenie_on(data):
        if request.method == "POST":
            if data == "data":
                energenie_control(request.get_json()["sleep"], "on", request.get_json()["socket"])
                return jsonify(True)

        return jsonify(None)
