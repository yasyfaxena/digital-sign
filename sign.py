from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization

with open("private_key.pem", "rb") as file:
    private_key = serialization.load_pem_private_key(
        file.read(),
        password=None
    )
input_file = input("Enter the name of the file to be signed: ")
with open(input_file, "rb") as file:
    data = file.read()
signature = private_key.sign(
    data,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
with open("signature.bin", "wb") as file:
    file.write(signature)

print("Digital signature successfully created.")
print("Signature saved as signature.bin")


