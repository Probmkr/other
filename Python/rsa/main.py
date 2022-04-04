from Crypto.Util.number import *

message = "probmkr is super hyper dangerous"

p = getPrime(1024) # 絶対公開するな
q = getPrime(1024) # 絶対公開するな

n = p * q # nは公開
phi = (p - 1) * (q - 1) # 絶対公開するな
e = 65537 # eも公開
m = bytes_to_long(message.encode()) # messageを数字にする

c = pow(m, e, n) # m^e mod n

d = pow(e, -1, phi)
m2 = pow(c, d, n)

message = long_to_bytes(m2).decode()

print(f"(本来公開しない)p = {p}")
print(f"(本来公開しない)q = {q}")
print(f"(公開する)n = {n}")
print(f"(送りたいメッセージ){message}")
print(f"(平文m){m}")
print(f"(暗号文)c = {c}")
print(message)
