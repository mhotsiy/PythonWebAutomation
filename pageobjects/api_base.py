import requests


class ApiBase:

    @staticmethod
    def call_endpoint(url):
        response = requests.get(url)
        return response


if __name__ == "__main__":
    ApiBase.call_endpoint()
