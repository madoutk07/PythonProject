import ipaddress

def network_calculator(ip_address, subnet_mask):
    network = ipaddress.IPv4Network(f"{ip_address}/{subnet_mask}", strict=False)
    return {
        "Network Address": str(network.network_address),
        "Broadcast Address": str(network.broadcast_address),
        "Subnet Mask": str(network.netmask),
        "Number of Hosts": network.num_addresses - 2,
    }

ip_address = input("Enter IP address: ")
subnet_mask = input("Enter subnet mask: ")

result = network_calculator(ip_address, subnet_mask)
for key, value in result.items():
    print(f"{key}: {value}")
