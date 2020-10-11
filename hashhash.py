
import string  
import random 


def randString():
	return ''.join(random.choice(string.ascii_uppercase) for _ in range(20))

def generate():
	strings = []

	for i in range(10**6):
		strings.append(hash(randString()))

	return len(set(strings))


print(generate())