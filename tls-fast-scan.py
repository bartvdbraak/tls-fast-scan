import multiprocessing
import subprocess
from xml.etree import ElementTree
import concurrent.futures
import os

hostname_list = [
    "www.google.com",
    "www.youtube.com",
    "www.facebook.com",
    "www.twitter.com",
    "www.instagram.com",
    "www.wikipedia.org",
    "www.yahoo.com",
    "www.whatsapp.com",
    "www.amazon.com",
    "www.live.com",
    "www.netflix.com",
    "www.tiktok.com",
    "www.reddit.com",
    "www.office.com",
    "www.linkedin.com",
    "www.samsung.com",
    "www.vk.com",
    "www.turbopages.org",
    "www.naver.com",
    "www.bing.com",
    "www.discord.com",
    "www.twitch.tv",
    "www.pinterest.com",
    "www.zoom.us",
    "www.weather.com",
    "www.qq.com",
    "www.microsoft.com",
    "www.msn.com",
    "www.globo.com",
    "www.duckduckgo.com",
    "www.roblox.com",
    "www.quora.com",
    "www.ebay.com",
]


def check_if_nmap_is_installed():
    result = subprocess.run(['nmap', '--version'], stderr=subprocess.PIPE)
    if result.returncode == 0:
        return True
    else:
        return False


def get_nmap_xml(hostname, xml_data):
    if hostname not in xml_data:
        xml_data[hostname] = subprocess.run(
            ['nmap', '--script', 'ssl-enum-ciphers', '-p', '443', '-oX', '-', hostname],
            stdout=subprocess.PIPE).stdout
    return xml_data[hostname]


def get_nmap_tls_version(hostname, xml_data):
    xml_str = get_nmap_xml(hostname, xml_data)
    root = ElementTree.fromstring(xml_str)
    unique_tls_versions = [table.attrib['key'] for table in root.findall(".//script[@id='ssl-enum-ciphers']/table")]
    return unique_tls_versions


def main():
    if check_if_nmap_is_installed():
        manager = multiprocessing.Manager()
        xml_data = manager.dict()

        num_workers = os.cpu_count()
        with concurrent.futures.ProcessPoolExecutor(num_workers) as executor:
            results = list(executor.map(get_nmap_tls_version, hostname_list, [xml_data]*len(hostname_list)))

        for hostname, tls_versions in zip(hostname_list, results):
            print(f'TLS versions available on {hostname}: {tls_versions}')

    else:
        print('nmap is not installed on this system')


if __name__ == '__main__':
    main()
