from task1 import link_dict





def test_success_link_dict():
        link = ['http://google.com']
        result = link_dict(link)

        assert   result == {'http://google.com': {'GET': 200, 'HEAD': 301}}


def test_wrong_link_dict():
        link = ["hello"]
        result = link_dict(link)
        print(result)
        ref = {}
        assert result == ref

