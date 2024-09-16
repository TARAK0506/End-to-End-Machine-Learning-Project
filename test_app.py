from app import app

def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

def test_predict_api(client):
    response = client.post('/predict_api', json={"data": [0.00632, 18.0, 2.31, 0.0, 0.538, 6.575, 65.2, 4.0900, 1.0, 296.0, 15.3, 396.90, 4.98]})
    assert response.status_code == 200
    assert response.json is not None
