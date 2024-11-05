import string
import random

def generate_password(
    uppercase: bool, 
    lowercase: bool, 
    digits: bool, 
    specials_char: bool, 
    length: int
) -> str:
  pool = ""
  if uppercase:
    pool = string.ascii_uppercase
  if lowercase:
    pool += string.ascii_lowercase
  if digits:
    pool += string.digits
  if specials_char:
    pool += string.punctuation

  return ''.join(random.choices(pool, k=int(length)))

if __name__ == '__main__':
  print(generate_password(True, True, True, False, 4))