from calendar import c
from flask import g
import pyotp
import segno

import config


def generate_authenticator_uri(email):
    secret = pyotp.random_base32()
    uri = pyotp.totp.TOTP(secret).provisioning_uri(name=email, issuer_name=config.APP_NAME)
    return uri

def generate_qr_code(text):
    qr = segno.make_qr(text)
    qr.save("qr.png", scale=10)

def verify_code(code, uri):
    totp = pyotp.parse_uri(uri)
    return totp.verify(code)

if __name__ == "__main__":
    user_email = input("Enter your email: ")
    uri = generate_authenticator_uri(user_email)
    generate_qr_code(uri)
    code = input("Enter code from Authenticator: ")
    validated = verify_code(code, uri)
    if validated:
        print("Validated")
    else:
        print("Invalid")
