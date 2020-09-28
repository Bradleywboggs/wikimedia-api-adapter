from fastapi import HTTPException


def validate(parameters):
    _validate_filter(parameters.get('filter'))
    _validate_page(parameters.get('page'))


# TODO
def _validate_filter(filters: dict):
    pass
    # month = filters.get('month')
    # day = filters.get('day')
    #
    # if not type(month) == int and not month > 0 and not month < 13:
    #     raise HTTPException(400, "'filter[month]' must be an integer between 1 and 12')")
    # if not type(day) == int and not day > 0 and not day < 32:
    #     raise HTTPException(400, "'filter[day]' must be an integer between 1 and 31')")
    #


# TODO
def _validate_page(page):
    pass
