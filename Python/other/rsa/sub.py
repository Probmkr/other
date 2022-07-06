m = 12345678
p = 7
q = 11
e = 65537

m2 = pow(pow(m, e, p*q), pow(e, -1, (p-1)*(q-1)), p * q)
print(m2)
