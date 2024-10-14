from unittest.mock import patch


@patch("src.external_api.requests.request")
def test_get_sum(mock_get):
    mock_get.return_value.json.return_value = {
        "date": "2018-02-22",
        "historical": "",
        "info": {"rate": 148.972231, "timestamp": 1519328414},
        "query": {"amount": 20, "from": "USD", "to": "RUB"},
        "result": 3724.305775,
        "success": True,
    }
