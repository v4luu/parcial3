from lambda1.parcial import lambda_handler
from unittest.mock import Mock
import pytest
import datetime

def test_lambda_handler(mocker):
    # Mock del resultado de requests.get
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = "contenido html de prueba"
    mocker.patch('requests.get', return_value=mock_response)

    # Mock del cliente de boto3
    mock_s3_client = mocker.patch('boto3.client')

    # Mock de datetime
    mock_datetime = mocker.patch('lambda1.parcial.datetime')  # Asegúrate de parchar el módulo donde se usa
    mock_datetime.now.return_value.strftime.return_value = "2025-06-03"

    # Ejecutar función con mocks de event y context
    event = {}
    context = {}
    lambda_handler(event, context)

def test_lambda_handler_http_error(mocker):
    # Simula un error HTTP 404
    mock_response = Mock()
    mock_response.status_code = 404
    mocker.patch('requests.get', return_value=mock_response)
    mock_s3_client = mocker.patch('boto3.client')

    event = {}
    context = {}
    lambda_handler(event, context)
