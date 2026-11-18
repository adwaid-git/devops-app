from app import app

def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b"Welcome to the Production app!" in response.data

def test_health():
    response = app.test_client().get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "UP"}

def test_about():
    response = app.test_client().get('/about')
    assert response.status_code == 200
    assert b"DevOps practice application" in response.data

def test_version():
    response = app.test_client().get('/version')
    assert response.status_code == 200
    assert response.json == {"version": "1.0.0"}
