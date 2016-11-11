import base64

#giftcard = "HZvbp1XQ7JpKXeCWLGT/ndoInD6H7S1j2uaW74WCv7tLAqM="
giftcard = "svdWSiyFmTq2vob939piIuzqic7Ht6tQRjz3ouXXRMQPzEZd"
cardbytes = bytearray(base64.standard_b64decode(giftcard))
print(map(hex, cardbytes))
print(base64.standard_b64encode(cardbytes))

#cardbytes[32] = cardbytes[32] ^ ord("1") ^ ord("9")
cardbytes[33] = cardbytes[33] ^ ord("1") ^ ord("9")

print(map(hex, cardbytes))
print(base64.standard_b64encode(cardbytes))