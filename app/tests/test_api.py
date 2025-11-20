import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_question():
    response = client.post("/questions/", json={"text": "Тестовый вопрос?"})
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == "Тестовый вопрос?"
    assert "id" in data

def test_get_questions():
    response = client.get("/questions/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_question_by_id():
    q = client.post("/questions/", json={"text": "Ещё один вопрос"}).json()
    response = client.get(f"/questions/{q['id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == q["id"]

def test_delete_question():
    q = client.post("/questions/", json={"text": "Вопрос для удаления"}).json()
    response = client.delete(f"/questions/{q['id']}")
    assert response.status_code == 200
    response = client.get(f"/questions/{q['id']}")
    assert response.status_code == 404


def test_create_answer():
    q = client.post("/questions/", json={"text": "Вопрос для ответа"}).json()
    response = client.post(f"/answers/questions/{q['id']}/", json={
        "text": "Мой ответ",
        "user_id": "user-1"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == "Мой ответ"
    assert data["question_id"] == q["id"]

def test_get_answer():
    q = client.post("/questions/", json={"text": "Вопрос для проверки ответа"}).json()
    a = client.post(f"/answers/questions/{q['id']}/", json={
        "text": "Ответ для проверки",
        "user_id": "user-2"
    }).json()
    response = client.get(f"/answers/{a['id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == a["id"]

def test_delete_answer():
    q = client.post("/questions/", json={"text": "Вопрос для удаления ответа"}).json()
    a = client.post(f"/answers/questions/{q['id']}/", json={
        "text": "Ответ для удаления",
        "user_id": "user-3"
    }).json()
    response = client.delete(f"/answers/{a['id']}")
    assert response.status_code == 200
    response = client.get(f"/answers/{a['id']}")
    assert response.status_code == 404
