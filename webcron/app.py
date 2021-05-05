# app.py
import json
import logging
import os

import requests


logger = logging.getLogger()
logger.setLevel(logging.getLevelName(os.environ.get("loglevel", "INFO")))


def lambda_handler(event, context):
    webcron_url = os.environ.get("webcron_url")
    logger.info(f"webcron_url: {webcron_url}")
    if not webcron_url:
        logger.warning(f"webcron_url is not set")
        return None
    res = requests.get(webcron_url)
    if res.ok:
        res_json = res.json()
        logger.info(f"{res_json}")
    else:
        logger.error(f"{res.status_code} {res.reason}")
        raise Exception(f"{res.status_code} {res.reason}")
    if res_json["status"] == "error":
        raise Exception(json.dumps(res_json))
    return res_json
