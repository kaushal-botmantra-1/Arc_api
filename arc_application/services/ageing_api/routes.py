from flask import jsonify, current_app, request
from ..ageing_api import ageing
from .dummy_data import due_age_by_summary, card_data, total_out_standing


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


@ageing.route('/cards/<int:seller_id>')
def get_dashboard(seller_id):
    """ this function returns the dashboard for particular seller

    Args:
        seller_id (int): seller id_in iteger
    """
    if card_data.get("seller_id") == seller_id:
        return jsonify(card_data), 200

    return jsonify(
        {
            "error": "data not found",
            "description": "seller does not exists"
        }
    ), 404


@ageing.route('/dueBySummary/<int:seller_id>')
def due_age_by_summary_chart(seller_id):
    """this function returns due by summary for a seller

    Args:
        seller_id (int): seller id
    """
    if due_age_by_summary.get("seller_id") == seller_id:
        return jsonify(due_age_by_summary), 200

    return jsonify(
        {
            "error": "data not found",
            "description": "seller does not exists"
        }
    ), 404


@ageing.route('/totalOutstanding/<int:seller_id>')
def total_out_standing_chart(seller_id):
    """returns total outstanding amount of top 5 customers

    Args:
        seller_id (int): seller id
    """
    if total_out_standing.get("seller_id") == seller_id:
        return jsonify(total_out_standing), 200

    return jsonify(
        {
            "error": "data not found",
            "description": "seller does not exists"
        }
    ), 404
