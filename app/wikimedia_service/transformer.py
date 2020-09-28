from typing import Union, Dict, List


def adapt_resource(wm, month, day):
    attrs: Dict[Union[str, int], Union[str, int, None, Dict, List]] =\
        wm.get('pages')[0]
    return {
        'type': "birth",
        'id': f"{wm.get('year')}{month}{day}_{attrs.get('titles').get('canonical')}",
        'attributes': {
            'name': attrs.get('titles').get('display'),
            'title': wm.get('text'),
            'description': attrs.get('extract'),
            'birthday': {
                'date': f"{wm.get('year')}-{month}-{day}",
                'month': month,
                'day': day,
                'year': wm.get('year')
            },
            'images': {
                'thumbnail': attrs.get('thumbnail'),
                'originalImage': attrs.get('originalimage'),
            },
         },
        'links': {
            'related': {
                'wikipedia-desktop': attrs.get('content_urls').get('desktop').get('page'),
                'wikipedia-mobile': attrs.get('content_urls').get('mobile').get('page')
            }
        }
    }


