import nmap

def SYNSCan():
    
    scanner.scan(ip, '1-1024', '-v -sS')
    
    print(scanner.scaninfo())
    print(f"[Ip-Status]: {scanner[ip].state()}")
    print(f"[Protocols]: {scanner[ip].all_protocols()}")
    print(f"[PORTS    ]: {list(scanner[ip]['tcp'].keys())}")


def UDPScan():
    scanner.scan(ip, '1-1024', '-v -sU')

    print(scanner.scaninfo())
    print(f"[Ip-Status]: {scanner[ip].state()}")
    print(f"[Protocols]: {scanner[ip].all_protocols()}")
    print(f"[PORTS    ]: {list(scanner[ip]['udp'].keys())}")

def CompScan():
    scanner.scan(ip, '1-1024', '-v -sS -sV -sC -A -O')
    
    print(scanner.scaninfo())
    print(f"[Ip-Status]: {scanner[ip].state()}")
    print(f"[Protocols]: {scanner[ip].all_protocols()}")
    print(f"[PORTS    ]: {list(scanner[ip]['tcp'].keys())}")



scanner = nmap.PortScanner()

ip = input("[ip-address] : ")

scan_type = input("""
            Scan Type:
            [1] SYN ACK Scan
            [2] UDP Scan
            [3] Comprehensive Scan\n
        """)

scans = [SYNScan, UDPScan, CompScan]



scan = scans[int(scan_type) - 1]
scan()
