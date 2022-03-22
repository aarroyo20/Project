"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<li class="nav-item"><a class="nav-link" href="/page1">Git and Github</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/page2">Docker</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/page3">Python and Flask</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/page4">CICD</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/article1">Python and others</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/article2">AAA Testing</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/article3">OOPs</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/article4">SOLID</a></li>' in response.data

def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome" in response.data

def test_request_about(client):
    """This makes the index page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"About" in response.data

def test_request_page1(client):
    """This makes the index page"""
    response = client.get("/page1")
    assert response.status_code == 200
    assert b"Git and Github" in response.data

def test_request_page2(client):
    """This makes the index page"""
    response = client.get("/page2")
    assert response.status_code == 200
    assert b"Docker" in response.data

def test_request_page3(client):
    """This makes the index page"""
    response = client.get("/page3")
    assert response.status_code == 200
    assert b"Python and Flask" in response.data

def test_request_page4(client):
    """This makes the index page"""
    response = client.get("/page4")
    assert response.status_code == 200
    assert b"CICD" in response.data

def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404
