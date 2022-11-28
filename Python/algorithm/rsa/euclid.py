def recur(p, q):
    mod = p % q
    print(f"{p} - {q} * {int(p/q)} = {mod}")
    if mod == 0:
        return q
    else:
        return recur(q, mod)

def de_recur(p, q):
    mods = [p, q]
    while mods[-1] != 0:
        mods.append(mods[-2] % mods[-1])
    return mods[-2]

print(recur(13, 7))
