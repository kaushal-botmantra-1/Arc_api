from arc_application import db
from flask import jsonify
from decimal import Decimal


def get_card_data(seller_id, date):
    """
    this function retrieves card data for dashboard
    # ARGS
        seller_id (int) - id of seller
        date (string) yyyy-mm-dd
    """
    try:
        query = f"""
        SELECT
        seller_name,
        SUM(amount_out_standing) AS total_receivables,
        SUM(amount_not_yet_due) AS not_yet_due

        FROM arc_aging_summary
        WHERE
        seller_code ={seller_id}
        AND
        as_on_date <= '{date}'

        group by seller_name
        """

        result = [dict(item) for item in db.engine.execute(query)]
        if len(result) > 0:
            name = result[0].get("seller_name")
            total_receivables = float(result[0].get("total_receivables"))
            not_yet_due = float(result[0].get("not_yet_due"))

            invoice_due_query = """
            SELECT  COUNT(DISTINCT invoice_number)
            from arc_aging_details
            WHERE days_past_due_date>0
            """

            invoice_due = [item for item in db.engine.execute(
                invoice_due_query)][0][0]

            payload = {
                "seller_id": seller_id,
                "seller_name": name,
                "cards_data": {
                    "total_receivables": total_receivables,
                    "not_yet_due": not_yet_due,
                    "total_overdue": total_receivables - not_yet_due,
                    "overdue_percent": f"{round(((total_receivables - not_yet_due)/total_receivables)*100,2)}%",
                    "invoice_due": invoice_due
                }
            }

            return jsonify(payload), 200

        return jsonify({
            "error": "data not found",
            "description": "No data exists for this particular query"
        }), 404

    except Exception as e:
        return jsonify({
            "error": "Unknown",
            "description": str(e)
        }), 500


def get_total_out_standing(seller_id, date, limit=5):
    """
    this function retrieves total outstanding for top 5 customers
    # ARGS
        seller_id (int) - id of seller
        date (string) yyyy-mm-dd
    """

    try:
        query = f"""
            SELECT
            amount_out_standing,
            seller_customer_name,
            seller_name,
            seller_customer_code

            FROM arc_aging_summary

            WHERE
            seller_code ={seller_id}
            AND
            as_on_date <= '{date}'
            ORDER BY amount_out_standing DESC limit {limit}
            """

        result = [dict(item) for item in db.engine.execute(query)]
        if len(result) > 0:
            seller_name = result[0].get("seller_name")
            customer_data = list()
            for customer in result:
                customer_data.append(
                    {
                        "name": customer.get("seller_customer_name"),
                        "customer_code": customer.get("seller_customer_code"),
                        "y": float(customer.get("amount_out_standing"))
                    }
                )
            payload = {
                "seller_id": seller_id,
                "seller_name": seller_name,
                "data": customer_data
            }

            return jsonify(payload), 200

        return jsonify({
            "error": "data not found",
            "description": "No data exists for this particular query"
        }), 404

    except Exception as e:
        return jsonify({
            "error": "Unknown",
            "description": str(e)
        }), 500


def get_due_age_by_summary(seller_id, date):
    """
    this function retrieves total outstanding for all customers
    # ARGS
        seller_id (int) - id of seller
        date (string) yyyy-mm-dd
    """

    try:
        query = f"""
        SELECT
        SUM(amount_aging_0_30) AS days_0_30,
        SUM(amount_aging_31_60) AS days_31_60,
        SUM(amount_aging_61_90) AS days_61_90,
        SUM(amount_aging_91_120) AS days_91_120,
        SUM(amount_aging_121_180) AS days_121_180,
        SUM(amount_aging_181_270) AS days_181_270,
        SUM(amount_aging_271_360) AS days_271_360,
        SUM(amount_aging_361plus) AS days_361_plus

        FROM
        arc_aging_summary

        WHERE
            seller_code ={seller_id}
            AND
            as_on_date <= '{date}'
        """
        result = [dict(item) for item in db.engine.execute(query)]
        if len(result) > 0:
            all_ageing_amount = list()
            # as there will always be one result
            result = result[0]
            for key, value in result.items():
                all_ageing_amount.append(
                    {
                        "name": key,
                        "y": float(value) if value else 0.0
                    }
                )

            payload = {
                "seller_id": seller_id,
                "data": all_ageing_amount
            }

            return jsonify(payload), 200
        return jsonify(
            {
                "error": "data not found",
                "description": "No data exists for this particular query"
            }
        ), 404

    except Exception as e:
        return jsonify({
            "error": "Unknown",
            "description": str(e)
        }), 500


def ageing_summary_report(seller_id, date):
    """this function retrieves all data points for a paricular seller till date

    Args:
        seller_id (int): seller identity number
        date (str): yyyy-mm-dd
    """
    try:

        query = f"""
        SELECT *
        FROM
            arc_aging_summary

            WHERE
                seller_code ={seller_id}
                AND
                as_on_date <= '{date}'
        """
        result = [dict(item) for item in db.engine.execute(query)]
        if len(result) > 0:
            for data in result:
                for key, values in data.items():
                    if isinstance(values, Decimal):
                        data[key] = float(values)

            payload = {
                "seller_id": seller_id,
                "data": result
            }
            return jsonify(payload)

        return jsonify(
            {
                "error": "data not found",
                "description": "No data exists for this particular query"
            }
        ), 404
    except Exception as e:
        print(e)
        return jsonify({
            "error": "Unknown",
            "description": str(e)
        }), 500


def ageing_details_report(seller_id, date):
    """this function retrieves all datapoints of ageing details for a prticular seller


        Args:
        seller_id (int): seller identity number
        date (str): yyyy-mm-dd
    """
    try:

        query = f"""
        SELECT *
        FROM
            arc_aging_details

            WHERE
                seller_code ={seller_id}
                AND
                as_on_date <= '{date}'
        """
        result = [dict(item) for item in db.engine.execute(query)]
        if len(result) > 0:
            for data in result:
                for key, values in data.items():
                    if isinstance(values, Decimal):
                        data[key] = float(values)

            payload = {
                "seller_id": seller_id,
                "data": result
            }
            return jsonify(payload)

        return jsonify(
            {
                "error": "data not found",
                "description": "No data exists for this particular query"
            }
        ), 404
    except Exception as e:
        print(e)
        return jsonify({
            "error": "Unknown",
            "description": str(e)
        }), 500
