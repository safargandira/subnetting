

#Program untuk mencari network ID
#Parameter yang dibutuhkan IP dan subnet


def networkID(ip, subnet):
    ID_list = {}
    for y in range(4):
        ID_list[y] = int(ip.split(".")[y]) & int(subnet.split(".")[y])
    ID = ".".join(str(ID_list[z]) for z in range(4))
    return ID
