

#Program untuk menentukan IPv


from ipaddress import ip_address, IPv4Address
  
def validIPAddress(IP: str) -> str:
    try:
        return "IPv4" if type(ip_address(IP)) is IPv4Address else "IPv6"
    except ValueError:
        return "Invalid"
