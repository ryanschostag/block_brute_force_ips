#! /usr/bin/python3.5

import subprocess as sp


def add_ip_address_to_iptables(ip_address):
    cmd = ["iptables", "-A", "INPUT", "-s", ip_address, "-j", "DROP"]
    sp.call(cmd)
    print('Blocked ' + ip_address + '.')
    return True


def get_ip_addresses_to_block(ip_address_file):
    print('Retrieving IP addresses from ' + ip_address_file)
    with open(ip_address_file, mode='r', encoding='utf-8') as f:
        return f.readlines()


def main():
    ip_file = 'ips_to_block.txt'
    ips = get_ip_addresses_to_block(ip_file)
    for ip in ips:
        add_ip_address_to_iptables(ip)


if __name__ == "__main__":
    main()
