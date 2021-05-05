import os
import json

from unittest import mock
import pytest

from webcron import app


def test_lambda_handler(mocker):
    os.environ["webcron_url"] = "http://test"
    res = mock.MagicMock()
    res.ok = True
    res.json = mock.MagicMock()
    res.json.return_value = {"status": "success"}
    mocker.patch("requests.get", return_value=res)
    ret = app.lambda_handler(None, None)
    assert ret.get("status") == "success"


def test_lambda_handler_no_url(mocker):
    os.environ["webcron_url"] = ""
    ret = app.lambda_handler(None, None)
    assert ret == None


def test_lambda_handler_http_error(mocker):
    os.environ["webcron_url"] = "http://test"
    res = mock.MagicMock()
    res.ok = False
    res.status_code = 404
    res.reason = "Not found"
    res.json = mock.MagicMock()
    res.json.return_value = {"status": "error", "data": {"message": "error message"}}
    mocker.patch("requests.get", return_value=res)
    exception = None
    try:
        app.lambda_handler(None, None)
    except Exception as e:
        exception = e
    assert exception.args[0] == "404 Not found"


def test_lambda_handler_webcron_disabled(mocker):
    os.environ["webcron_url"] = "http://test"
    res = mock.MagicMock()
    res.ok = True
    res.status_code = 200
    res.json = mock.MagicMock()
    res.json.return_value = {
        "data": {
            "message": "Backgroundjobs are using system cron!"
        },
        "status": "error"
    }
    mocker.patch("requests.get", return_value=res)
    exception = None
    try:
        ret = app.lambda_handler(None, None)
    except Exception as e:
        exception = e
    err = json.loads(exception.args[0])
    assert err["status"] == "error"
    assert err["data"]["message"] == "Backgroundjobs are using system cron!"
