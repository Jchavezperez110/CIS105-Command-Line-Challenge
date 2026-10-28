import base64

print("Base64 Decoder")

text = "SGVsbG8gV29ybGQ="

decoded = base64.b64decode(text).decode()

print("Encoded text:", text)
print("Decoded message:", decoded)
