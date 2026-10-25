#!/usr/bin/env python3
"""Run this INSIDE your sandbox: can it reach services running on the host?

In the episode, a session working inside a "sealed" container found an AI server running
on the host machine. The container couldn't see the host's files — but it could reach
its network. This script checks that one thing, and nothing else.

It tries a TCP connection to a list of ports on the addresses a container typically uses
to reach its host, and prints what answers. It sends no data and reads nothing.

Usage:
    python3 probe_host.py                    # default ports
    python3 probe_host.py --ports 22 80 443  # your own list
    python3 probe_host.py --hosts 10.0.2.2   # add an address (e.g. a VM's host)

Only run it on a machine that is yours.
"""
import argparse
import socket
import struct

# Ports where local tools often listen. Edit to match what runs on your machine.
DEFAULT_PORTS = {
    1234: "local AI model server (common default)",
    11434: "local AI model server (common default)",
    8080: "development server / web UI",
    3000: "development server",
    8000: "development server",
    5432: "PostgreSQL",
    6379: "Redis",
    22: "SSH",
}

# Names a container commonly uses to reach its host.
DEFAULT_HOSTS = ["host.docker.internal", "host.containers.internal", "gateway.docker.internal"]


def default_gateway():
    """The container's default gateway, read from the Linux routing table (often the host)."""
    try:
        with open("/proc/net/route") as f:
            for line in f.readlines()[1:]:
                fields = line.split()
                if fields[1] == "00000000" and int(fields[3], 16) & 2:
                    return socket.inet_ntoa(struct.pack("<L", int(fields[2], 16)))
    except (OSError, IndexError, ValueError):
        pass
    return None


def resolve(name):
    try:
        return socket.gethostbyname(name)
    except OSError:
        return None


def is_open(address, port, timeout):
    try:
        with socket.create_connection((address, port), timeout=timeout):
            return True
    except OSError:
        return False


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--ports", type=int, nargs="+", help="ports to try")
    parser.add_argument("--hosts", nargs="+", default=[], help="extra addresses to try")
    parser.add_argument("--timeout", type=float, default=0.5, help="seconds per attempt")
    args = parser.parse_args()

    ports = args.ports or list(DEFAULT_PORTS)

    targets = {}
    for name in DEFAULT_HOSTS + args.hosts:
        address = resolve(name)
        if address:
            targets.setdefault(address, name)
    gateway = default_gateway()
    if gateway:
        targets.setdefault(gateway, "default gateway")

    if not targets:
        print("No host address found from inside this box (no known name, no gateway).")
        print("That's a good sign, not a proof. Add an address with --hosts if you know one.")
        return 0

    reachable = []
    for address, label in targets.items():
        print(f"Trying {address} ({label})...")
        for port in ports:
            if is_open(address, port, args.timeout):
                what = DEFAULT_PORTS.get(port, "")
                reachable.append((address, port))
                print(f"  OPEN    port {port:<5} {what}")

    print()
    if reachable:
        print(f"{len(reachable)} service(s) on the host answered from inside the box.")
        print("This box is sealed for files, maybe. Not for the network.")
        return 1
    print("Nothing answered on these ports. Good sign for this list, not a proof.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
