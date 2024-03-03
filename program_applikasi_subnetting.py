

#program app subnetting

import IPSubnet as ips
import broadcast, wildcard, prefix, subnet_mask, network, lastaddress, firstaddress,ipv


ip = input("Masukkan alamat IP: ")
host = int(input("Masukkan jumlah host: "))

prefix = prefix.cari_prefix(host)
subnet = subnet_mask.subnetmask(prefix)

ipver = ipv.validIPAddress(ip)
print("IP versi ke: ", ipver)

print("CIDR dari alamat tersebut adalah: ", prefix)
print("Subnet masknya adalah: ", subnet)

networkID = network.networkID(ip, subnet)
print("Network IDnya: ", networkID,"/",prefix, sep="")

wildcard_binary = wildcard.find_wildcard(ips.Int2Bin(subnet))
WildCard = wildcard.convert_decimal(wildcard_binary)
print("Wild cardnya: ", WildCard)

broadcastIP = broadcast.broadcast(networkID, WildCard)
print("Broadcastnya: ", broadcastIP)

minIP = firstaddress.miniIP(networkID)
print("First Addresnya: ", minIP)

maxIP = lastaddress.maxiIP(broadcastIP)
print("Last Addresnya: ", maxIP)
