import os
import pytest
import requests

from dotenv import load_dotenv, find_dotenv
from todo_app import app

@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    test_app = app.create_app()

    with test_app.test_client() as client:
        yield client

def test_index_page(monkeypatch, client):
    monkeypatch.setattr(requests, 'get', stub)

    response = client.get('/')

    assert response.status_code == 200
    assert "Test card" in response.data.decode()

def stub(url, params={}):
    test_board_id = os.environ.get('TRELLO_BOARD_ID')
    test_api_key = os.environ.get('TRELLO_API_KEY')
    test_api_token = os.environ.get('TRELLO_API_TOKEN')

    if url == f'https://api.trello.com/1/boards/{test_board_id}/lists?key={test_api_key}&token={test_api_token}&cards=open&card_fields=id,name':
        fake_response_data = """[{
            "id": "123abc",
            "name": "To Do",
            "cards": [{"id": "456", "name": "Test card"}]
        }]"""
        return get_succesful_response(fake_response_data)

    raise Exception(f'Integration test did not expect URL "{url}"')

def get_succesful_response(fake_response_data):
    response = requests.models.Response()
    response.status_code = 200
    response._content = fake_response_data.encode("utf-8")
    response.encoding = "utf-8"
    return response

