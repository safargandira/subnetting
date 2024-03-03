

#Program untuk menampilkan IP & Subnet dalam bentuk biner


def Int2Bin(integer):
    binary = '.'.join([bin(int(x)+256)[3:] for x in integer.split('.')])
    return binary
