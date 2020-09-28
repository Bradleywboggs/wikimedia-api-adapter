import urllib.parse

#  fastAPI mostly does query string parsing out of the box quite nicely; however, I couldn't find anything that parsed:
#  ?foo[bar]=bazz&foo[bizz]=buzz  as {'foo': {'bar': 'bazz, 'bizz': 'buzz'}};
#  hence, this parser
#  TODO: add recursion to look for deeper nesting


class QueryParser:
    def __init__(self):
        pass

    def __call__(self, query):
        params = urllib.parse.parse_qs(str(query))
        return parse(params)


def parse(params: dict):
    accum = {}
    for (k, v) in params.items():
        if '[' in k and ']' in k:
            accum = array_q_to_dict(k, v, accum)
        else:
            accum = {**accum, k: v}
    return accum


def array_q_to_dict(key: str, value: list, accum):
    bracket_start = key.find('[')
    bracket_end = key.find(']')

    outer_key = key[0: bracket_start]
    inner_key = key[bracket_start + 1: bracket_end]

    if outer_key in accum.keys():
        return {**accum, outer_key: {**accum[outer_key], inner_key: int(value[0])}}
    return {**accum, outer_key: {inner_key: int(value[0])}}






