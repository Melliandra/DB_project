import re
def check_mail(mail):
    pattern = '[a-zA-Z0-9\.]+@[a-z]+\.(ru|org|com)'
    if re.match(pattern,mail) is None:
        return False
    else:
        return True

