import os
from api_tools.api_request_tools import build_path_var_url, get_api
from wikimedia_service.transformer import adapt_resource


_URL_TEMPLATE = "https://en.wikipedia.org/api/rest_v1/feed/onthisday/births"
_API_USER_AGENT = os.environ.get('API_USER_AGENT') or "bradleywboggs@gmail.com"


def _pluck_required_params(params):
    mm = params.get('filter').get('month')
    dd = params.get('filter').get('day')

    page = params.get('page') or {'offset': 1, 'limit': 30}
    page_offset = page.get('offset') or 1
    page_limit = page.get('limit') or 30

    return mm, dd, page_offset, page_limit

# TODO: Break this apart.


def get_births(params: dict):
    (mm, dd, page_offset, page_limit) = _pluck_required_params(params)
    url = build_path_var_url(_URL_TEMPLATE, mm, dd)
    headers = {'Api-User-Agent': _API_USER_AGENT}
    response = get_api(url, {}, headers)

    resource = [adapt_resource(r, mm, dd) for r in response.get('births')]

    first_record = (page_offset - 1) * page_limit
    last_record = first_record + page_limit
    total_pages = (len(resource) // page_limit + 1)

    return {
        'data': resource[first_record:last_record],
        'links': {
           'current_page': page_offset,
           'records_per_page': page_limit,
           'total_records': len(resource),
           'total_pages': total_pages,
        }
    }

