import hashlib


def hash_pwd(pwd_):
    return hashlib.sha256(pwd_.encode(encoding='utf-8')).hexdigest()
