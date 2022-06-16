from datetime import date
import json
from src.app import app

def test_flask_app_response():
    today = date.today().strftime("%d/%m/%Y")
    with app.test_client() as test_client:
        response = test_client.get("/")
        json_data = json.loads(response.data)
        assert response.status_code == 200
        assert json_data == {"message": 'flask_app ready!', 'datetime': today}