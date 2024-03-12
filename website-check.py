import sys
import requests
from datetime import datetime

def check_website_status(domain_list):
    working_websites = []
    not_working_websites = []

    for domain in domain_list:
        url = "https://" + domain.strip()  # strip to remove any leading/trailing whitespace
        try:
            response = requests.get(url)
            if response.status_code == 200:
                working_websites.append(url)
            else:
                not_working_websites.append(url)
        except requests.exceptions.RequestException as e:
            not_working_websites.append(url)

    return working_websites, not_working_websites

def save_results(working_websites, not_working_websites):
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"website-status_{timestamp}.txt"
    
    with open(filename, "w") as file:
        file.write("Working websites:\n")
        for website in working_websites:
            file.write(website + "\n")

        file.write("\nNot working websites:\n")
        for website in not_working_websites:
            file.write(website + "\n")

    return filename

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <domain_list_file>")
        return

    file_path = sys.argv[1]
    with open(file_path, "r") as file:
        domain_list = file.readlines()

    working_websites, not_working_websites = check_website_status(domain_list)

    filename = save_results(working_websites, not_working_websites)
    print(f"Results saved to {filename}")

if __name__ == "__main__":
    main()
