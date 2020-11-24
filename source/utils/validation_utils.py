import regex as re


def email_checker(email):
    """
    A helper function to validate a entry of email type, don't be fooled anymore!
    :param email: A string containing a email, maybe.
    :return: A boolean
    """
    pattern = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(pattern, email):
        return True
    else:
        return False
