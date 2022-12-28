import subprocess as sp
from xml.etree import ElementTree
import concurrent.futures
import os
import functools

hostname_list = [
    "www.google.com",
    "www.youtube.com",
    "www.facebook.com",
    "www.twitter.com",
    "www.instagram.com",
]

def check_nmap():
    check_version = sp.run(['nmap', '--version'], stderr=sp.PIPE, stdout=sp.PIPE)
    return check_version.returncode == 0

def xml_to_tls_versions(xml_data):
    root = ElementTree.fromstring(xml_data)
    return [table.attrib['key'] for table in root.findall(".//script[@id='ssl-enum-ciphers']/table")]

class Scanner:
    # Constructor
    def __init__(self, hostnames, workers=os.cpu_count()):
        self.nmap = None
        self.results = {}
        self.hostnames = hostnames
        self.workers = workers

    def tls_versions(self, hostname, port=443):
        self.nmap = f'nmap -sV --script ssl-enum-ciphers -p {port} -oX - {hostname}'
        self.results[hostname] = xml_to_tls_versions(sp.run(self.nmap, stdout=sp.PIPE).stdout)
        print('hi')

    def process_hostnames(self):
        print('hi')
        with concurrent.futures.ProcessPoolExecutor(max_workers=self.workers) as executor:
            executor.map(self.tls_versions, self.hostnames)


if __name__ == '__main__':
    scan = Scanner(hostnames=hostname_list)
    scan.process_hostnames()
    print(scan.results)
