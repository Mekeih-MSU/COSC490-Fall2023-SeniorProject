import os
import gnupg

gpg = gnupg.GPG()

def create_asymmetric_key():
	input_data = gpg.gen_key_input(
		name_real='FirstName LastName',
		name_comment="123-456-7890",
	    name_email='youremail@example.com',
	    key_type='RSA'
	)

	return gpg.gen_key(input_data)

def get_public_key(key):
	return gpg.export_keys(key.fingerprint)

def get_private_key(key):
	return gpg.export_keys(key.fingerprint, True)

def get_name(key):
	#to-do
	print(1)

def get_phone_number(key):
	#to-do
	print(1)

def get_email(key):
	#to-do
	print(1)

def encrypt_text(plaintext, recipient_key):
	encrypted_data = gpg.encrypt(plaintext, recipient_key, always_trust=True)
	if encrypted_data.ok:
		return str(encrypted_data)
	else:
		raise Exception(f"Encryption failed: {encrypted_data.status}")

def decrypt_text(encrypted_text):
    decrypted_data = gpg.decrypt(encrypted_text)
    if decrypted_data.ok:
    	return str(decrypted_data)
    else:
    	raise Exception(f"Decryption failed: {decrypted_data.status}")

key = create_asymmetric_key()
public_key = get_public_key(key)
private_key = get_private_key(key)
print(public_key)
print(private_key)
print("")

text = "Hello, how are you!"
en_t = encrypt_text(text, key.fingerprint)
de_t = decrypt_text(en_t)

print(text)
print(en_t)
print(de_t)
