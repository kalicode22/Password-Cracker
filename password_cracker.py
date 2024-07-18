import hashlib
import itertools
import string

# Function to perform a dictionary attack
def dictionary_attack(password_hash, dictionary_file):
    with open(dictionary_file, 'r', encoding='utf-8') as file:
        for line in file:
            password = line.strip()
            hashed = hashlib.sha256(password.encode()).hexdigest()
            if hashed == password_hash:
                return password
    return None

# Function to perform a brute-force attack
def brute_force_attack(password_hash, max_length=4):
    characters = string.ascii_lowercase + string.digits  # Change as needed
    for length in range(1, max_length + 1):
        for combination in itertools.product(characters, repeat=length):
            password = ''.join(combination)
            hashed = hashlib.sha256(password.encode()).hexdigest()
            if hashed == password_hash:
                return password
    return None

# Example hashed password (SHA-256)
hashed_password = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"

if __name__ == "__main__":
    dictionary_file = "dictionary.txt"
    
    # Attempt dictionary attack
    result = dictionary_attack(hashed_password, dictionary_file)
    if result:
        print(f"Password found using dictionary attack: {result}")
    else:
        print("Password not found using dictionary attack.")
    
    # Attempt brute-force attack
    result = brute_force_attack(hashed_password, max_length=4)  # Adjust max_length as needed
    if result:
        print(f"Password found using brute-force attack: {result}")
    else:
        print("Password not found using brute-force attack.")
