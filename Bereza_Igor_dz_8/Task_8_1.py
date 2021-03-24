import re


def email_parse(email_address):
    try:
        address = re.findall(r'^[\w\-]+@[\w\-]+\.\w{2,3}$', email_address)
        if not address:
            raise ValueError
        result = re.split(r'@', address[0])
        email_dict = {'username': result[0], 'domain': result[1]}
        print(email_dict)
    except ValueError:
        print(f'ValueError: wrong email: {email_address}')


email_parse('sdn66lfk-345_123wer@mail.com')
