import requests
import dns.resolver



def get_subdomains(domain):
    subdomains = []
    try:
        with open('subdomains.txt', 'r') as file:
            subdomains = file.read().splitlines()
    except FileNotFoundError:
        print("subdomains.txt file not found!")
        return []

    discovered_subdomains = []
    for subdomain in subdomains:
        url = f"http://{subdomain}.{domain}"
        try:
            requests.get(url)
            discovered_subdomains.append(url)
        except requests.ConnectionError:
            pass
    return discovered_subdomains

def main():
    domain = input("Enter the domain to enumerate subdomains for: ")
    subdomains = get_subdomains(domain)
    if subdomains:
        print("Discovered subdomains:")
        for sub in subdomains:
            print(sub)
    else:
        print("No subdomains discovered.")

if __name__ == "__main__":
    main()
