import os

import requests

MONGODB_DATA_API_BASE_URL = os.getenv(
    "MONGODB_DATA_API_BASE_URL",
    "https://eu-central-1.aws.data.mongodb-api.com/app/data-qjiey/endpoint/data/v1/action",
)
MONGODB_COLLECTION = os.getenv("MONGODB_COLLECTION", "Timesheet")
MONGODB_DATABASE = os.getenv("MONGODB_DATABASE", "Timesheet_1")
MONGODB_DATA_SOURCE = os.getenv("MONGODB_DATA_SOURCE", "Cluster0")


def _get_headers():
    api_key = os.getenv("MONGODB_DATA_API_KEY", "").strip()
    if not api_key:
        raise ValueError("MONGODB_DATA_API_KEY environment variable is not set.")
    return {
        "Content-Type": "application/json",
        "Access-Control-Request-Headers": "*",
        "api-key": api_key,
    }


def _perform_action(action, payload):
    request_payload = {
        "collection": MONGODB_COLLECTION,
        "database": MONGODB_DATABASE,
        "dataSource": MONGODB_DATA_SOURCE,
    }
    request_payload.update(payload)

    try:
        response = requests.post(
            f"{MONGODB_DATA_API_BASE_URL}/{action}",
            headers=_get_headers(),
            json=request_payload,
            timeout=15,
        )
        response.raise_for_status()
        response_data = response.json()
        response_data["ok"] = True
        return response_data
    except (requests.RequestException, ValueError) as exc:
        return {"ok": False, "error": str(exc)}


def insert_row(create_row):
    return _perform_action("insertOne", {"document": create_row})


def find_data(user_name, date):
    return _perform_action("findOne", {"filter": {"User": user_name, "Date": date}})


def delete_data(user_name, date):
    return _perform_action("deleteOne", {"filter": {"User": user_name, "Date": date}})
