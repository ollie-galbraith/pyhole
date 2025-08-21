# PyHole

PyHole is a Python client library for interacting with the Pi-hole API, designed to simplify programmatic management of DNS and configuration settings on your Pi-hole instance. It provides a convenient interface for authentication, session management, and DNS record manipulation, including hosts and CNAME records.

## Features

- Authenticate and manage sessions with Pi-hole
- Retrieve and update DNS configuration
- Manage local DNS hosts (add, delete, update, modify)
- Manage CNAME records (add, delete)
- Extensible for additional Pi-hole API endpoints

## Installation

Install via pip (after packaging):

```bash
pip install pyhole
```

## Usage

```python
from pyhole import PiHole

# Initialize client
pihole = PiHole(base_url='https://your-pihole/api', password='your_password')

# Access DNS configuration
config = pihole.Config()
dns = config.DNS()

# List DNS hosts
hosts = dns.Hosts().get()

# Add a host
dns.Hosts().create('192.168.1.2', 'example.local')

# Delete a host
dns.Hosts().delete('192.168.1.2', 'example.local')

# List CNAME records
cname_records = dns.CNames().get()

# Add a CNAME record
dns.CNames().create('alias.local', 'target.local')

# Delete a CNAME record
dns.CNames().delete('alias.local', 'target.local')
```

## Project Structure

- `src/pyhole/main.py`: Main PiHole client class
- `src/pyhole/classes/local_dns.py`: DNS and configuration management classes
- `tests/`: Unit tests

## License

See [LICENSE](LICENSE) for details.
