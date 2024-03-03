

#Program untuk mencari class IP
#Parameter yang diperlukan adalah alamat IP


def findClass(ip):
    if(ip in range(1, 127)):
        return 'A'
    elif(ip in range(128, 191)):
        return 'B'
    elif(ip in range(192, 223)):
        return 'C'
    elif(ip in range(224, 239)):
        return 'D'
    else:
        return 'E'


