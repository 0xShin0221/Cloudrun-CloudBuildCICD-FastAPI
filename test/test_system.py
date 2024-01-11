import os
import requests

# def test_system():
#     base_url = os.environ.get("BASE_URL")
#     assert base_url, "Cloud Run service URL not found"

#     id_token = os.environ.get("ID_TOKEN")
#     assert id_token, "Unable to acquire an ID token"

#     response = requests.get(base_url, headers={"Authorization": f"Bearer {id_token}"})
#     assert response.status_code == 200
#     assert response.text == "Hello, World!"