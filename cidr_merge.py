import ipaddress
def collapse_subnets(cidrs: list[str]) -> list[str]:
    nets = [ipaddress.ip_network(c) for c in cidrs]
    return [str(n) for n in ipaddress.collapse_addresses(nets)]
