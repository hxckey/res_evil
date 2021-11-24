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

    def test_get_char_error(self, api):
        res = api.get('/chars/100')
        assert res.status == '200 OK'
        assert 'No agent' in res.json

    def test_post_char(self, api):
        mock_data = json.dumps({"name": "Chief Irons"})
        mock_headers = {"Content-Type": "application/json"}
        res = api.post('/chars', data=mock_data, headers=mock_headers)
        assert res.json['id'] == 3

    def test_patch_char(self, api):
        mock_data = json.dumps({"name": "Licker"})
        mock_headers = {"Content-Type": "application/json"}
        res = api.put('/chars/1', data=mock_data, headers=mock_headers)
        assert res.json['name'] == 'Licker'
        assert res.json['id'] == 1

    def test_delete_char(self, api):
        res = api.delete('/chars/1')
        assert res.status == '204 NO CONTENT'

    def test_not_found(self, api):
        res = api.get('/dinocrisis')
        assert res.status == '404 NOT FOUND'
        assert 'WARNING' in res.json['message']