import string
import random

MIN_LENGTH = 4


def generate_password(
    uppercase: bool, 
    lowercase: bool, 
    digits: bool, 
    specials_char: bool, 
    length: int
) -> str:
  pool = ""
  if length < MIN_LENGTH:
    raise ValueError("length must be greater than 4")
  # assert length >= MIN_LENGTH, f"length must be greater than {MIN_LENGTH}"
  if uppercase:
    pool = string.ascii_uppercase
  if lowercase:
    pool += string.ascii_lowercase
  if digits:
    pool += string.digits
  if specials_char:
    pool += string.punctuation

  if pool == "":
    return string.ascii_letters

  return ''.join(random.choices(pool, k=int(length)))

if __name__ == '__main__':
  print(generate_password(True, True, True, False, 4))