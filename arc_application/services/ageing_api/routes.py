from flask import jsonify, current_app, request, send_file
from ..ageing_api import ageing
from .helpers import *


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
        date (str): date until which data is required
    """
    result = get_total_out_standing(seller_id, date)
    return result


@ageing.route('/ageingSummary/<int:seller_id>/<string:date>')
def ageing_summary_report_route(seller_id, date):
    """return all the data fields for a seller

    Args:
        seller_id (int): 
        date (str): date until which data is required
    """
    res = ageing_summary_report(seller_id, date)
    return res


@ageing.route('/ageingDetails/<int:seller_id>/<string:date>')
def ageing_details_report_route(seller_id, date):
    """return all the data fields for a seller

    Args:
        seller_id (int): 
        date (str): date until which data is required
    """
    res = ageing_details_report(seller_id, date)
    return res


@ageing.route('/downloadAgeingSummary', methods=["POST"])
def download_ageing_summary_report():
    """return all the data fields for a seller

    Args:
        seller_id (int): 
        date (str): date until which data is required
    """
    data = request.json
    seller_id = data.get("seller_id")
    date = data.get("date")
    if seller_id and date:
        if isinstance(seller_id, int) and isinstance(date, str):
            res = download_ageing_summry(seller_id, date)
            return res
        else:
            return jsonify({
                "error": "invalid datatype",
                "description": "please the the datatypes of values"
            })

    else:
        return jsonify({
            "error": "missing key",
            "description": "either key is missing or it is spelled wrong"
        })


@ageing.route('/downloadAgeingDetails', methods=["POST"])
def download_ageing_details_report():
    """return all the data fields for a seller

    Args:
        seller_id (int): 
        date (str): date until which data is required
    """
    data = request.json
    seller_id = data.get("seller_id")
    date = data.get("date")
    if seller_id and date:
        if isinstance(seller_id, int) and isinstance(date, str):
            res = download_ageing_details(seller_id, date)
            return res
        else:
            return jsonify({
                "error": "invalid datatype",
                "description": "please the the datatypes of values"
            })

    else:
        return jsonify({
            "error": "missing key",
            "description": "either key is missing or it is spelled wrong"
        })
