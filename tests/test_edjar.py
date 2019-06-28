import os
import pytest

from edjar import edjar

@pytest.fixture
def client():
    resta.app.config['TESTING'] = True
    client = resta.app.test_client()
    yield client

def test_endpoints(client):
    routes = {'/': b"All courses", '/courses':  b"All courses", 
              '/course/new': b"Create new course",
              '/course/1/edit': b"Edit course 1",
              '/course/1/delete': b"Delete course 1",
              '/course/1': b"Show course 1 syllabus",
              '/course/1/syllabus': b"Show course 1 syllabus",
              '/course/1/syllabus/new': b"Create new syllabus item in course 1",
              '/course/1/syllabus/2/edit/': b"Edit existing syllabus item 2 in course 1",
              '/course/1/syllabus/2/delete/': b"Delete syllabus item 2 from course 1",
}
    for r in routes:
        rv = client.get(r)
        assert routes[r] in rv.data
