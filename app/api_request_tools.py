import requests
from functools import reduce


def build_path_var_url(url_template, *path_vars):
    return reduce(lambda url, var: f'{url}/{var}', path_vars,  url_template)


def get_api(url, params=None, headers=None):
    if headers is None:
        headers = {}
    if params is None:
        params = {}

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()
    except:
        # TODO: Add error handling for non-200 responses
        pass



