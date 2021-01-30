from flask import jsonify, current_app, request
from ..ageing_api import ageing
from .helpers import get_card_data, get_total_out_standing, get_due_age_by_summary


@ageing.route('/status')
def status_function():
    return jsonify(
        {
            "api_service": "ageing dashboards & reports",
            "version": current_app.config["VERSION"],
            "copyright": "Bot it services private ltd.",
            "description": "this api collection contains all ageing dashboards and reports related api's",
            "environment": current_app.config["ENVIRONMENT"]
        }
    ), 200


@ageing.route('/cards/<int:seller_id>/<string:date>')
def get_dashboard(seller_id, date):
    """ this function returns the dashboard for particular seller

    Args:
        seller_id (int): seller id_in iteger
        date (str):yyyy-mm-dd
    """
    result = get_card_data(seller_id, date)
    return result


@ageing.route('/dueBySummary/<int:seller_id>/<string:date>')
def due_age_by_summary_chart(seller_id, date):
    """this function returns due by summary for a seller

    Args:
        seller_id (int): seller id
    """
    result = get_due_age_by_summary(seller_id, date)

    return result


@ageing.route('/totalOutstanding/<int:seller_id>/<string:date>')
def total_out_standing_chart(seller_id, date):
    """returns total outstanding amount of top 5 customers

    Args:
        seller_id (int): seller id
    """
    result = get_total_out_standing(seller_id, date)
    return result
