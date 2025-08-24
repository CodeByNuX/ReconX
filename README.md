# ReconX

Late one night I was watching traffic traverse my firewall. I wanted a faster, simpler way to dig into domains and IP addresses without juggling multiple tools. From that glow of the monitor, ReconX was born.

What started as a quick helper script became a Django web app that can pull WHOIS information and IP threat-risk assessments on demand. ReconX is meant to be straightforward, useful, and extendable — the same qualities I needed in the middle of that investigation.

---

## Features

- Validate domains and IPv4 addresses before querying  
- WHOIS lookups using [whois40](https://rapidapi.com/devXprite/api/whois40)  
- Threat and geolocation checks using [IP Geolocation Threat Risk API](https://rapidapi.com/agushimuso/api/ip-geolocation-threat-risk-api)  
- Results displayed as JSON in the browser  
- Graceful handling of invalid input and failed API requests  
- Easy to extend with new APIs  

---

## Getting Started

### Prerequisites

- Python 3.10+  
- Django  
- requests  
- A [RapidAPI](https://rapidapi.com/) account with subscriptions to:  
  - [whois40](https://rapidapi.com/devXprite/api/whois40)  
  - [IP Geolocation Threat Risk API](https://rapidapi.com/agushimuso/api/ip-geolocation-threat-risk-api)  

### Installation

Clone the repository:  

```bash
git clone https://github.com/CodeByNuX/ReconX.git
cd ReconX
```

Install Django and requests (Ubuntu example):  

```bash
sudo apt install -y python3-django python3-requests
```

Copy the example environment file and edit it with your own API key:  

```bash
cp .env.example .env
```

Your `.env` should look like this:  

```dotenv
RAPIDAPI_KEY=your-rapidapi-key-here
WHOIS_API_HOST=whois40.p.rapidapi.com
IP_RISK_API_HOST=ip-geolocation-threat-risk-api.p.rapidapi.com
```

Run migrations and start the server:  

```bash
python3 manage.py migrate
python3 manage.py runserver
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## Usage

- Enter a domain (e.g., `example.com`) -> WHOIS lookup  
- Enter an IP (e.g., `8.8.8.8`) -> WHOIS and IP risk check  
- Results are returned as JSON  

---

## Error Handling

- Empty input -> usage message in the browser  
- Invalid domain/IP -> validation error  
- Timeout or failed request -> JSON error object, for example:  

```json
{"error": "Request to API timed out"}
```

---

## Roadmap

- Improve JSON display formatting  
- Add export functionality (CSV/JSON)  
- Support for additional RapidAPI integrations  

---

## Security Notice

ReconX does not include an authentication system. It is intended for local or lab use only.
Do not expose this application directly to the internet.  If you plan to deploy it beyound you own machine, place it behind a reverse proxy with proper access control.

---

## License

This project is open-sourced under the MIT License.
