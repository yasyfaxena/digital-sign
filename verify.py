from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization

with open("public_key.pem", "rb") as file:
    public_key = serialization.load_pem_public_key(
        file.read()
    )
input_file = input("Enter the name of the file to verify: ")
with open(input_file, "rb") as file:
    data = file.read()
with open("signature.bin", "rb") as file:
    signature = file.read()

try:
    public_key.verify(
        signature,
        data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("SIGNATURE VALID")
    print("The original file and signature match.")
except Exception:
    print("SIGNATURE INVALID")
    print("The file may have been modified or the signature does not match.")

    