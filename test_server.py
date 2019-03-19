import pytest

from flask import Flask

from server import app, HELLO_MESSAGE


@pytest.fixture
def client():

    return app.test_client()


def test_request(client):

    resp = client.get("/")
    assert resp.status_code == 201
    assert resp.data.rfind(bytes(HELLO_MESSAGE.encode("utf-8"))) >= 0
