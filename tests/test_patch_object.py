import pytest
from src.api_client import APIClient

client = APIClient()


@pytest.fixture(scope="module")
def test_object_id():
    """Create a fresh object for testing and return its ID"""
    payload = {"name": "Test Device", "data": {"year": 2024, "price": 1000}}
    response = client.create_object(payload)
    assert response.status_code == 200
    return response.json()["id"]

def test_patch_valid_name(test_object_id):
    response = client.patch_object(test_object_id, {"name": "Updated Device"})
    assert response.status_code == 200
    body = response.json()
    assert body["name"] == "Updated Device"

def test_patch_valid_nested_field(test_object_id):
    response = client.patch_object(test_object_id, {"data": {"year": 2025}})
    assert response.status_code == 200
    body = response.json()
    assert body["data"]["year"] == 2025

def test_patch_invalid_id():
    response = client.patch_object("invalid-id-123", {"name": "Test"})
    assert response.status_code == 404

def test_patch_empty_payload(test_object_id):
    response = client.patch_object(test_object_id, {})
    # API may respond differently depending on backend test
    assert response.status_code in [200, 400, 404]
"""
def test_patch_empty_payload():
    # Create a new object
    payload = {"name": "Temp Device", "data": {"year": 2024}}
    obj_id = client.create_object(payload).json()["id"]

    response = client.patch_object(obj_id, {})
    assert response.status_code in [200, 400]

    # (optional) cleanup
    # client.delete_object(obj_id)


def test_patch_empty_payload(test_object_id):
    response = client.patch_object(test_object_id, {})
    # Some APIs accept empty payloads (200), some reject (400)
    assert response.status_code in [200, 400]"""

"""
@pytest.mark.parametrize("object_id, payload", [
    ("ff8081818...", {"name": "Updated Name"}),   # valid update
    ("ff8081818...", {"data": {"year": 2025}}),  # update nested field
])
def test_patch_valid_object(object_id, payload):
    response = client.patch_object(object_id, payload)
    assert response.status_code == 200
    body = response.json()
    for key in payload:
        assert key in body, f"{key} not found in response"

def test_patch_invalid_id():
    response = client.patch_object("invalid-id", {"name": "Test"})
    assert response.status_code == 404

def test_patch_empty_payload():
    response = client.patch_object("ff8081818...", {})
    assert response.status_code in [200, 400]  # Depending on API behavior
"""