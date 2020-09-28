from fastapi import FastAPI, Request, Depends
from request_manager.handler import QueryParser
from request_manager.validator import validate
from wikimedia_service import wikimedia

app = FastAPI()


@app.get('/')
async def root():
    return {"api": "wikimedia-adapter", "version": "0.1.1"}

# TODO: Add auth middleware


@app.get('/births')
async def get_births(
        request: Request,
        query_parser=Depends(QueryParser)
):
    # # TODO: Minimize the lines in the routes functions:
    # #  1. pass the stuff to a controller
    # #  2.  which will call a service which fetches data
    # #  3.  which will be passed to a generic response builder to generate pagination, and the all json-api thingies
    # #  4   which will finally return our JSON resource

    params = query_parser(request.query_params)
    validate(params)

    return wikimedia.get_births(params)

