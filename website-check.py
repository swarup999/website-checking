import requests

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
    with open("website-status.txt", "w") as file:     # File will be saved as website-status.txt
        file.write("Working websites:\n")
        for website in working_websites:
            file.write(website + "\n")

        file.write("\nNot working websites:\n")
        for website in not_working_websites:
            file.write(website + "\n")

def main():
    file_path = "/home/path/websites.txt"  # Update with the path to your .txt file
    with open(file_path, "r") as file:
        domain_list = file.readlines()

    working_websites, not_working_websites = check_website_status(domain_list)

    save_results(working_websites, not_working_websites)
    print("Results saved to website-status.txt")

if __name__ == "__main__":
    main()
