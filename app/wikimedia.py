import os
import urllib.parse as urltools
import json
from fastapi import Request
from api_request_tools import build_path_var_url
_URL_TEMPLATE = "https://en.wikipedia.org/api/rest_v1/feed/onthisday/births"
_API_USER_AGENT = os.environ.get('API_USER_AGENT') or "bradleywboggs@gmail.com"

def get_births(
        mm: int,
        dd: int,
        request: Request,
        page: dict = {},
        filters: dict = {},
        fields: dict = {},
):

    url = build_path_var_url(_URL_TEMPLATE, str(mm), str(dd))
    headers = {'Api-User-Agent': _API_USER_AGENT}
    response = get_api(url, {}, headers)

    resource = [adapt_resource(r, mm, dd) for r in response.get('births')]

    first_record = (page.get('offset') - 1) * page.get('limit')
    last_record = first_record + page.get('limit')
    total_pages = (len(resource) // page.get('limit')) + 1
    self_link = request.url

    return {
        'data': resource[first_record:last_record],
        'links': {
           'current_page': self_link,
           'records_per_page': page.get('limit'),
           'total_records': len(resource),
           'total_pages': total_pages,
        }
    }
    # data = \
    #     WikiMediaTransformer(response, filters, filters).filter().map()


    # transformer.filter().map()
    # filtered = _filter_response(response, filters)
    # return _map_response(filtered, fields)


def _filter_response(response, filters):
    return []


def _map_response(response, fields):
    return []

