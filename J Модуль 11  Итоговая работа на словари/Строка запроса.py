def build_query_string(params):
    return "&".join(sorted(f'{k}={v}' for k, v in params.items()))
