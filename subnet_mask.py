

#Program untuk mencari subnet-mask
#Parameter yang dibutuhkan adalah prefix/CIDR


def oktet1 (prefix):
    total = 0
    t = 8 - prefix
    if 1 <= prefix < 8 :
        for q in range (7,t-1,-1):
            nilai = 2**q
            total += nilai
    elif prefix < 0:
        total = 0
    else:
        total = 255
    return total


def oktet2 (prefix):
    t = 16 - prefix
    if 8 < prefix < 16 :
        total = 0
        for q in range (7,t,-1):
            nilai = 2**q
            total += nilai
    elif prefix < 8:
        total = 0
    else:
        total = 255
    return total


def oktet3 (prefix):
    total = 0
    t = 24 - prefix
    if 16 < prefix < 24 :
        for q in range (7,t-1,-1):
            nilai = 2**q
            total += nilai
    elif prefix < 16:
        total = 0
    else:
        total = 255
    return total


def oktet4 (prefix):
    total = 0
    t = 32 - prefix
    if 24 < prefix:
        for q in range (7,t-1,-1):
            nilai = 2**q
            total += nilai
    elif prefix <= 24:
        total = 0
    else:
        total = 255
    return total


def subnetmask(prefix):
    lssubnetmask = []
    w = oktet1 (prefix)
    lssubnetmask.append(w)
    x = oktet2 (prefix)
    lssubnetmask.append(x)
    y = oktet3 (prefix)
    lssubnetmask.append(y)
    z = oktet4 (prefix)
    lssubnetmask.append(z)

    subnet_mask = ".".join(str(lssubnetmask[i]) for i in range(4))
    return subnet_mask
