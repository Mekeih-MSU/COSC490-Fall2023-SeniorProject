import os
import gnupg
import pickle

GPG = gnupg.GPG()
PERSONAL_KEY_FILE = "PERSONAL_KEYS.pkl"
CONTACTS_KEY_FILE = "CONTACTS_KEYS.pkl"

# FILE I/O ------------------------------->
def save_data(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)

def load_data(filename):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []

def add_contact_key(first_name, last_name, phone_number, email, public_key):
	file_entry = {
		"First Name": first_name,
		"Last Name": last_name,
		"Phone Number": phone_number,
		"Email": email,
		"Public Key": public_key,
	}

	add_entry(file_entry, CONTACTS_KEY_FILE)

def add_personal_key(name):
	key_pair = create_asymmetric_key()
	public_key = get_public_key(key_pair)
	private_key = get_private_key(key_pair)

	file_entry = {
		"Name": name,
		"Public Key": public_key,
		"Private Key": private_key,
	}

	add_entry(file_entry, PERSONAL_KEY_FILE)

def add_entry(contact_entry, file):
	data = load_data(file)
	data.append(contact_entry)
	save_data(data, file)

def delete_entry(index, file):
	data = load_data(file)
	if (0 <= index < len(data)):
		data.pop(index)
		save_data(data, file)

def print_page(file):
	data = load_data(file)
	for i in range(len(data)):
		print(f"#{i}: {data[i]}")


# PGP ALGO ------------------------------->

def create_asymmetric_key():
	input_data = GPG.gen_key_input(key_type='RSA')
	return GPG.gen_key(input_data)

def get_public_key(key):
	return GPG.export_keys(key.fingerprint)

def get_private_key(key):
	return GPG.export_keys(key.fingerprint, True)

def encrypt_text(plaintext, recipient_key):
	encrypted_data = GPG.encrypt(plaintext, recipient_key, always_trust=True)
	if encrypted_data.ok:
		return str(encrypted_data)
	else:
		raise Exception(f"Encryption failed: {encrypted_data.status}")

def decrypt_text(encrypted_text):
	decrypted_data = GPG.decrypt(encrypted_text)
	if decrypted_data.ok:
		return str(decrypted_data)
	else:
		raise Exception(f"Decryption failed: {decrypted_data.status}")


# TEST GROUNDS ------------------------------->
