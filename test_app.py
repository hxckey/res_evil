import json

class TestAPICase():
    def test_welcome(self, api):
        res = api.get('/')
        assert res.status == '200 OK'
        assert res.json['message'] == 'Welcome to Raccoon City, home of the Umbrella Corporation'

    def test_get_chars(self, api):
        res = api.get('/chars')
        assert res.status == '200 OK'
        assert len(res.json) == 2

    def test_get_char(self, api):
        res = api.get('/chars/1')
        assert res.status == '200 OK'
        assert res.json["name"] == 'HULK'