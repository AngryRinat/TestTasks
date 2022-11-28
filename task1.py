import sys
import requests as req
import validators
import json

http_methods_list = ['get', 'head', 'post', 'put', 'delete', 'options', 'trace', 'patch']
def link_dict(link_list):
    link_dict = {}
    for link in link_list:
        method_dict = {}
        if validators.url(link):
                _get = req.get(link, timeout=1).status_code
                _head = req.head(link, timeout=1).status_code
                _post = req.post(link, timeout=1).status_code
                _put = req.put(link, timeout=1).status_code
                _delete = req.delete(link, timeout=1).status_code
                _options = req.options(link, timeout=1).status_code
                _patch = req.patch(link, timeout=1).status_code
                if _get != 405:
                    method_dict['GET'] = _get
                if _head != 405:
                    method_dict['HEAD'] = _head
                if _post != 405:
                    method_dict['POST'] = _post
                if _put != 405:
                    method_dict['PUT'] = _put
                if _delete != 405:
                    method_dict['DELETE'] = _delete
                if _options != 405:
                    method_dict['OPTIONS'] = _options
                if _patch != 405:
                    method_dict['PATCH'] = _patch

                link_dict[link] = method_dict
        else:
            print(f'Строка {link} не является ссылкой')

    return link_dict






if __name__ == '__main__':
    link_list = sys.argv[1:]

    print(json.dumps(link_dict(link_list)))
