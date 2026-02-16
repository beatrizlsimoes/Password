import itertools
import string
import time

# Secret password to be guessed (controlled by the user)
secret_password = "abc"

characters = (
string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
)

start_time = time.time()
attempts = 0
max_length = 3

for length in range(1, max_length + 1):
    for combinatiion in itertools.product (characters, repeat = length):
        guess = ''.join(combinatiion)
        attempts += 1

        if guess == secret_password:
            end_time = time.time()
            print(f"Password found: {guess}")
            print(f"Attempts: {attempts}")
            print(f"Time taken: {end_time - start_time:.2f} seconds")
            exit()

print("Password not found within tested length.")
