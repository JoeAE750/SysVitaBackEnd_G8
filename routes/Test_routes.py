from flask import Blueprint, jsonify,request

from utils.extensions import db
from models.Test import Test

Test_routes = Blueprint("Test_routes", __name__)

@Test_routes.route("/tests", methods=["GET"])
def get_tests():
    tests = Test.query.all()
    return jsonify([test.to_dict() for test in tests]), 200   