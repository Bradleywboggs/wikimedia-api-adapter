from typing import List, Dict
from fastapi import FastAPI, Request, Query
import json
from wikimedia import get_wikimedia

app = FastAPI()


@app.get('/')
async def root():
    return {"api": "wikimedia-adapter", "version": "0.1.1"}


@app.get('/births')
async def get_births(
        request: Request,
        filter: str = Query(..., title="json string of filters", ),
        page: str = Query(..., title="json string of page parameters"),
):
    # TODO: Minimize the lines in the routes functions:
    #  1. pass the stuff to a controller
    #  2.  which will call a service which fetches data
    #  3.  which will be passed to a generic response builder to generate pagination, and the all json-api thingies
    #  4   which will finally return our JSON resource

    fs = json.loads(filter)
    month = fs.get('month')
    day = fs.get('day')

    response = get_wikimedia(month, day,  request, page=json.loads(page),)

    return response

