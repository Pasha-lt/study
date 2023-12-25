import pytest
import requests

class TestClass:

    @classmethod
    def setup_class(cls):
        cls.response = requests.request("GET", "https://api.chucknorris.io/jokes/random")
        print(1)

    @classmethod
    def teardown_class(cls):
        print("\nвсе")

    def test_key_categories(self):
        assert self.response.json()["categories"] == []


    @pytest.mark.parametrize("key", ['created_at', 'icon_url', 'id', 'updated_at', 'url', 'value'])
    def test_keys(self, key):
        assert self.response.json()[key]