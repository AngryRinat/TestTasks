import re
import requests as req


def check_link(link:str):
    link_ref = "^((ftp|http|https):\/\/)(www\.)?([A-Za-zА-Яа-я0-9]{1}[A-Za-zА-Яа-я0-9\-]*\.?)*\.{1}[A-Za-zА-Яа-я0-9-]{2,8}(\/([\w#!:.?+=&%@!\-\/])*)?"

    if re.match(link_ref, link) is not None:
        return True
    else:
        return False

def link_dict(link_list):
    link_dict = {}
    for link in link_list:
        method_dict = {}
        if check_link(link) != False:
            if  (req.get(link).status_code) != 405:
                method_dict['get'] = req.get(link).status_code
            elif (req.post(link).status_code) != 405:
                method_dict['post'] = req.post(link).status_code
            link_dict[link] = method_dict
        else:
            print(f'Строка {link} не является ссылкой')

    return link_dict






if __name__ == '__main__':
    link_list = []
    while True:
        elem = input('Введите строку...')
        if bool(elem) == True:
            link_list.append(elem)
        else:
            break
    print(link_dict(link_list))
