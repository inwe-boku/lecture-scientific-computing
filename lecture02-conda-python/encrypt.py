import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Taken from here:
# https://cryptography.io/en/latest/fernet/#using-passwords-with-fernet

password = b"password"

salt = os.urandom(16)
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password))
f = Fernet(key)

group_members = (
b"""First Last;1234565;nickname
First Last;1234565;nickname
First Last;1234565;nickname
"""
)

with open('group_members', 'w') as f:
    f.encrypt(group_members)
