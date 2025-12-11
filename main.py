import ipaddress
from core.utils import get_valid_ip, get_valid_mask
from core.output_string import *

def main():
    ip = get_valid_ip()
    mask = get_valid_mask()
    network = ipaddress.IPv4Network(f"{ip}/{mask}", strict=False)
    network_address = network.network_address
    broadcast_address = network.broadcast_address
    total_hosts = network.num_addresses - 2 if network.num_addresses > 2 else 0
    cidr = network.prefixlen
    output = (
        format_input_ip(ip),
        format_subnet_mask(mask),
        format_network_address(network_address),
        format_broadcast_address(broadcast_address),
        format_num_hosts(total_hosts),
        format_cidr_mask(cidr)
    )
    with open(f'subnet_info_{ip}_342743846.txt', 'w') as f:
        for row in output:    
            f.write(row)
    
    
if __name__ == '__main__':
    main()