

#Program untuk mencari prefix/ CIDR
#Parameter yang dibutuhkan adalah jumlah host


def host_max(host):
    for x in range (0,32):
        if host > (2**x):
            continue
        elif host <= 2**x :
            return x
       
def tukar(host_id):
    x = 32 - host_id
    return x

def cari_prefix(host):
    x = host_max(host)
    y = tukar(x)
    return y
