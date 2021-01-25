

from flask import Blueprint
ageing = Blueprint("ageing", __name__, url_prefix="/ageing")
from ..ageing_api import routes
