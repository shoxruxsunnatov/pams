from random import choices


def get_token():
    chars = 'qwertyuiopasdfghjklzxcvbnm1234567890'
    chars += chars.upper()

    return ''.join(choices(chars, k=20))
