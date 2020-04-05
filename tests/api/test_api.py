import pytest
import requests
from pytest import mark
from pageobjects.api_base import ApiBase

@mark.api
class TestApi:

    URL = 'http://api.zippopotam.us/us/90210'

    def test_get_locations_for_us_90210_check_status_code_equals_200(self):
        self.response = requests.get(self.URL)
        assert self.response.status_code == 200

    def test_api(self):

        assert ApiBase.call_endpoint(self.URL).status_code == 200


    def test_get_locations_for_us_90210_check_content_type_equals_json(self):
        self.response = requests.get(self.URL)
        assert self.response.headers['Content-Type'] == "application/json"


    def test_get_locations_for_us_90210_check_country_equals_united_states(self):
        self.response = requests.get(self.URL)
        self.response_body = self.response.json()
        assert self.response_body["country"] == "United States"


    def test_get_locations_for_us_90210_check_city_equals_beverly_hills(self):
        self.response = requests.get(self.URL)
        self.response_body = self.response.json()
        assert self.response_body["places"][0]["place name"] == "Beverly Hills"


    def test_get_locations_for_us_90210_check_one_place_is_returned(self):
        self.response = requests.get(self.URL)
        self.response_body = self.response.json()
        assert len(self.response_body["places"]) == 1