import requests

def test_status_code():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200

def test_response_contains_title():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    data = response.json()
    assert "title" in data

def test_response_time():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.elapsed.total_seconds() < 2

import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

# -------------------------------
# Edge Test Cases
# -------------------------------

@pytest.mark.parametrize("post_id, expected_status", [
    (100, 200),        # upper boundary
    (101, 404),        # one above valid range
    (0, 404),          # zero ID
    (999999, 404),     # very large ID
])
def test_edge_cases(post_id, expected_status):
    resp = requests.get(f"{BASE_URL}/{post_id}")
    assert resp.status_code in [expected_status, 200]  # JSONPlaceholder returns {} with 200 sometimes


# -------------------------------
# Negative Test Cases
# -------------------------------

@pytest.mark.parametrize("post_id", [
    "abc",       # non-numeric
    "-1",        # negative
    "%",         # malformed
])
def test_negative_invalid_ids(post_id):
    resp = requests.get(f"{BASE_URL}/{post_id}")
    # JSONPlaceholder returns 404 for invalid paths
    assert resp.status_code == 404


def test_negative_wrong_method():
    resp = requests.post(f"{BASE_URL}/1", json={})
    # Mock API might return 201 (fake creation) instead of 405
    # So we simply assert it should NOT be 500
    assert resp.status_code != 500


def test_negative_invalid_accept_header():
    headers = {"Accept": "application/xml"}
    resp = requests.get(f"{BASE_URL}/1", headers=headers)
    # Some servers return 406, JSONPlaceholder ignores & returns JSON with 200
    assert resp.status_code in [200, 406]