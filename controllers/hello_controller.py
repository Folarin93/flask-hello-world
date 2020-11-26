from flask import Blueprint

hello = Blueprint("hello", __name__, url_prefix="/hello")


@hello.route("/", methods=["GET"])
def hello_world():
    return "hello world"
