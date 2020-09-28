# WikiMedia API Adapter
A REST API Middlelayer which translates Wikimedia API responses to [JSON:API](https://jsonapi.org/) specced loveliness.

This is still **quite** a work in progress.
What you get right now:
* JSON:API specified resource with pagination by default (links are still needing some work) 
    - example call: `{baseUrl}/v0/births?filter[month]=12&filter[day]=25&page[limit]=30&page[offset]=3`
    - note that due to the nature of the resource the filters are required
    - At this point, only the happy path is functioning, and there's just one endpoint "births".
      use case: "Born on this day"

Future plans:
    - optimize by adding caching layer with MongoDB, to enable lighting fast queries when requesting additional pages 
    - add error handling
    - add additional filters and sorting


Without the adapter, an example "birth" record from the wikimedia api:  
```{
    "births": [
        {
            "text": "Sam McQueen, English footballer",
            "pages": [
                {
                    "type": "standard",
                    "title": "Sam_McQueen",
                    "displaytitle": "Sam McQueen",
                    "namespace": {
                        "id": 0,
                        "text": ""
                    },
                    "wikibase_item": "Q16236902",
                    "titles": {
                        "canonical": "Sam_McQueen",
                        "normalized": "Sam McQueen",
                        "display": "Sam McQueen"
                    },
                    "pageid": 41950830,
                    "thumbnail": {
                        "source": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Sam_McQueen_v_Augsburg_2017.jpg/218px-Sam_McQueen_v_Augsburg_2017.jpg",
                        "width": 218,
                        "height": 320
                    },
                    "originalimage": {
                        "source": "https://upload.wikimedia.org/wikipedia/commons/d/d9/Sam_McQueen_v_Augsburg_2017.jpg",
                        "width": 735,
                        "height": 1077
                    },
                    "lang": "en",
                    "dir": "ltr",
                    "revision": "974887655",
                    "tid": "ba5ec9b0-fcf6-11ea-ac56-c790b9216e89",
                    "timestamp": "2020-08-25T16:17:32Z",
                    "description": "English association football player (born 1995)",
                    "description_source": "central",
                    "content_urls": {
                        "desktop": {
                            "page": "https://en.wikipedia.org/wiki/Sam_McQueen",
                            "revisions": "https://en.wikipedia.org/wiki/Sam_McQueen?action=history",
                            "edit": "https://en.wikipedia.org/wiki/Sam_McQueen?action=edit",
                            "talk": "https://en.wikipedia.org/wiki/Talk:Sam_McQueen"
                        },
                        "mobile": {
                            "page": "https://en.m.wikipedia.org/wiki/Sam_McQueen",
                            "revisions": "https://en.m.wikipedia.org/wiki/Special:History/Sam_McQueen",
                            "edit": "https://en.m.wikipedia.org/wiki/Sam_McQueen?action=edit",
                            "talk": "https://en.m.wikipedia.org/wiki/Talk:Sam_McQueen"
                        }
                    },
                    "extract": "Samuel James McQueen is an English professional footballer who plays for Southampton. A native of the city of Southampton, McQueen joined the Southampton Academy at the age of eight and has remained with the club ever since. Handed his senior debut for the club in 2014, he plays primarily as a left-sided full back or winger.",
                    "extract_html": "<p><b>Samuel James McQueen</b> is an English professional footballer who plays for Southampton. A native of the city of Southampton, McQueen joined the Southampton Academy at the age of eight and has remained with the club ever since. Handed his senior debut for the club in 2014, he plays primarily as a left-sided full back or winger.</p>",
                    "normalizedtitle": "Sam McQueen"
                }
            ],
            "year": 1995
        },...
]
```

WITH the adapter
```{
  "data": [
    {
      "type": "birth",
      "id": "199526_Sam_McQueen",
      "attributes": {
        "name": "Sam McQueen",
        "title": "Sam McQueen, English footballer",
        "description": "Samuel James McQueen is an English professional footballer who plays for Southampton. A native of the city of Southampton, McQueen joined the Southampton Academy at the age of eight and has remained with the club ever since. Handed his senior debut for the club in 2014, he plays primarily as a left-sided full back or winger.",
        "birthday": {
          "date": "1995-2-6",
          "month": 2,
          "day": 6,
          "year": 1995
        },
        "images": {
          "thumbnail": {
            "source": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Sam_McQueen_v_Augsburg_2017.jpg/218px-Sam_McQueen_v_Augsburg_2017.jpg",
            "width": 218,
            "height": 320
          },
          "originalImage": {
            "source": "https://upload.wikimedia.org/wikipedia/commons/d/d9/Sam_McQueen_v_Augsburg_2017.jpg",
            "width": 735,
            "height": 1077
          }
        }
      },
      "links": {
        "related": {
          "wikipedia-desktop": "https://en.wikipedia.org/wiki/Sam_McQueen",
          "wikipedia-mobile": "https://en.m.wikipedia.org/wiki/Sam_McQueen"
        }
      }
    },...
]
```
## Run the App locally
From project root:
```
docker build -t wm-api-adapter:v0 .
docker run -dit -p 8081:80 --name my-api-adapter wm-api-adapter:v0
```

Check that it's running:

from the terminal: `curl localhost:8081`

from your browser: `http://localhost:8081`

you should see a 200 response: 
```
{
        "api": "wikimedia-api-adapter",
        "version": "0.1.0",
        "examples": { 
            "births": "{baseUrl}/v0/births?filter[month]=12&filter[day]=25&page[limit]=30&page[offset]=1" 
}
```
to stop the container:
`docker stop my-api-adapter`


