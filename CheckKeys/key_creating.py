import random
import string

def generate_key():
    characters = string.ascii_uppercase + string.digits
    key = ''.join(random.choice(characters) for _ in range(25))
    return '-'.join([key[i:i+5] for i in range(0, len(key), 5)])

print(generate_key())
