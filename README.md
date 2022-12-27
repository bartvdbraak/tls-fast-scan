```
████████╗██╗░░░░░░██████╗░░░░░░███████╗░█████╗░░██████╗████████╗░░░░░░░██████╗░█████╗░░█████╗░███╗░░██╗
╚══██╔══╝██║░░░░░██╔════╝░░░░░░██╔════╝██╔══██╗██╔════╝╚══██╔══╝░░░░░░██╔════╝██╔══██╗██╔══██╗████╗░██║
░░░██║░░░██║░░░░░╚█████╗░█████╗█████╗░░███████║╚█████╗░░░░██║░░░█████╗╚█████╗░██║░░╚═╝███████║██╔██╗██║
░░░██║░░░██║░░░░░░╚═══██╗╚════╝██╔══╝░░██╔══██║░╚═══██╗░░░██║░░░╚════╝░╚═══██╗██║░░██╗██╔══██║██║╚████║
░░░██║░░░███████╗██████╔╝░░░░░░██║░░░░░██║░░██║██████╔╝░░░██║░░░░░░░░░██████╔╝╚█████╔╝██║░░██║██║░╚███║
░░░╚═╝░░░╚══════╝╚═════╝░░░░░░░╚═╝░░░░░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░░░░░░░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝
```

A Python script that uses the `nmap` tool and multiprocessing to quickly scan a list of hostnames and retrieve the TLS versions supported by each host.
Prerequisites

- [nmap](https://nmap.org/) must be installed and available in the system path.

## Usage

To use the `tls-fast-scan` script, run the following command:

```commandline
python tls-fast-scan.py
```

The script will scan the list of hostnames in the `hostname_list` variable and print the TLS versions supported by each host.

## Modifying the Hostname List

To modify the list of hostnames that are scanned by the script, edit the `hostname_list` variable at the top of the `tls-fast-scan.py` script. The list should contain the hostnames to be scanned, with one hostname per line.

## Multiprocessing

The script uses the `concurrent.futures` module to parallelize the scanning of the hostnames using multiple worker processes. The number of worker processes used is determined by the number of CPU cores available on the system.

## Output

The script will print the TLS versions supported by each host, in the following format:

```commandline
TLS versions available on www.example.com: ['TLSv1.2', 'TLSv1.3']
```

If the `nmap` tool is not installed or is not available in the system path, the script will print an error message:

```commandline
nmap is not installed on this system
```

## Additional Options

You can specify additional options for the `nmap` command by modifying the arguments passed to the `subprocess.run()` function in the `get_nmap_xml` function. For example, to scan a different port, you can modify the `'-p'`, `'443'` arguments to specify a different port number.

For more information on the options available for the nmap command, refer to the [nmap documentation](https://nmap.org/docs.html).

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
