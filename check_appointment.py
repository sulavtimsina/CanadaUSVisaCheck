import subprocess
import time
from bs4 import BeautifulSoup

def check_appointments():
    # Curl command
    curl_command = """
    curl 'https://ais.usvisa-info.com/en-ca/niv/schedule/64507641/payment' \
    -H 'Host: ais.usvisa-info.com' \
    -H 'Connection: keep-alive' \
    -H 'Cache-Control: max-age=0' \
    -H 'sec-ch-ua: "Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"' \
    -H 'sec-ch-ua-mobile: ?0' \
    -H 'sec-ch-ua-platform: "macOS"' \
    -H 'Upgrade-Insecure-Requests: 1' \
    -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36' \
    -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
    -H 'Sec-Fetch-Site: same-origin' \
    -H 'Sec-Fetch-Mode: navigate' \
    -H 'Sec-Fetch-User: ?1' \
    -H 'Sec-Fetch-Dest: document' \
    -H 'Referer: https://ais.usvisa-info.com/en-ca/niv/schedule/64507641/continue_actions' \
    -H 'Accept-Language: en-US,en;q=0.9,cs;q=0.8' \
    --cookie '_gid=GA1.2.794927080.1734245149; _ga=GA1.2.636675795.1733867442; _ga_CSLL4ZEK4L=GS1.1.1734245149.6.1.1734245163.0.0.0; _yatri_session=LoF1cY4SMJ%2BwcJ4TwOPKvDf4nSeQf5HuBu%2FMFkgPHdPphCyqtgW2irr%2BKAuZJ3pRc8BDXICKg4csLlYAH%2FJGZpPLCNRYYmqa5N%2FSXQkPV8hGq5%2FC4h%2B7DcSqcbkd%2FYUdocud0v7GmDKJVhYKG1p%2FATtUnSX5GOSeEtrpX4Neoq2k4W0GhoOmMBVGmA9CCLNxN2wuQwFY1Em%2FMXkpuZr53m5Jbv65sxefuUF7AHXlW2ixCp%2Fv%2F2vN5lxj%2BqJmZ%2BEH%2FZDVTddZSoIb7ZGlUFcTH8OnUUIszXhKska4Z590Qztuz%2BJSEBxwUYFKm1AlaAOMuObrrvZSNKlRQOJXzNjoOw10HJnde73ygx%2FKgwqPSETKK5ZT2v9jzjtaiAYTmVTmk%2BQth0M3xb93wXoXM%2B3rNfrrpipSm1lq7R43sU2uOHzD5pzY9wykgYfIcXiGr%2FJj72mW95JG8guArxpno0swiHxHqxIHSD9jEZQz%2B73zu4COYNmBjcCXph00SaC5Lzcy8Yi4cdmDwlT%2BaWru1RqNXuzrrn0BrNdqEzicKcJsFZffXF5T2o%2Fu3mD5GEj7dt0b5B9w%2BMK5Mu66vCmSxWfXegUuTryjy3cyrgA6whxIRl%2F35vPb2%2BHtDYAk0g1bj47tKdqzVbHMc2pOr6Qs2x0rIBJZTDum1xlYsar8R%2BxISqarEgqAoah8pWqo8ZMO%2BalGiBKkAfjXf7lh79Pb%2BjsKcbvCfirGogm8gxyukdTk2yJpgCDBZUkkddRATHRNYAlTQSNzJtGWTf8UJm8obUsRSFvO96nXJrzSKaOjomrQc3hG8kFElosdvc3F3xH6PQ%3D%3D--BPsKO31eF0R4giPN--FDkNNQ3MmfAw0rgqbxTNgw%3D%3D; _gat=1; _ga_W1JNKHTW0Y=GS1.2.1734245149.5.1.1734245362.0.0.0' \
    --proxy http://localhost:9090 -s
    """

    try:
        # Run the curl command and get output
        result = subprocess.check_output(curl_command, shell=True, text=True)

        # Parse HTML with BeautifulSoup
        soup = BeautifulSoup(result, 'html.parser')

        # Extract relevant part
        toronto_section = soup.find('td', text='Toronto')
        if toronto_section:
            status = toronto_section.find_next_sibling('td', class_='text-right')
            print(f"Appointment Status: {status.text.strip() if status else 'Not Found'}")
        else:
            print("Toronto section not found in the response")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    while True:
        check_appointments()
        time.sleep(60)  # Run every minute