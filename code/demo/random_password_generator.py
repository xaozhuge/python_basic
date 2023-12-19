import random
import string
from common.common import t

def generate_password(length=12):
	characters = string.ascii_letters + string.digits + string.punctuation
	password = ''.join(random.choice(characters) for _ in range(length))
	return password

password = generate_password()
print("Random Password:", password)


'''
docker exec python380_c python3 demo/random_password_generator.py
'''