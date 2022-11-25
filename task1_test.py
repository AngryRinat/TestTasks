from task1 import check_link, link_dict




def test_check_link_success():
        link = 'https://google.com'
        result = bool(check_link(link))

        assert result == True


def test_check_link_wrong():
        link = 'google.com'
        result = bool(check_link(link))

        assert result != True
def test_success_link_dict():
        link = ['https://google.com']
        result = link_dict(link)

        assert   result == {'https://google.com': {'get': 200}}

def test_wrong_link_dict():
        link = ["hello"]
        result = link_dict(link)
        print(result)
        ref = {}
        assert result == ref

