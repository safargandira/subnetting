 

#Program untuk mencari broadcast ip
#Parameter yang dibutuhkan adalah network ID dan wild card


def broadcast(network, wildcard):
    Broadcast_list = {}
    for z in range(4):
        Broadcast_list[z] = int(network.split(".")[z]) | int(wildcard.split(".")[z])
    broadcast = ".".join(str(Broadcast_list[c]) for c in range(4))
    return broadcast
