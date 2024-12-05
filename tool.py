import validators
import requests

def validating_email(email):

    if validators.email(email):
        return True
    else:
        return False


def identifying_breaches(email, api_key):

    url =  f"https://leakcheck.io/api/public?check={email}"
    headers = {
         "Authorization" : f"Bearer {api_key}"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            info = response.json()
            return info
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"An Error has occurred: {e}")
        return None


def displaying_breaches(info, email):

    if info and info.get("success"):
        found = info.get("found", 0)
        if found > 0:

            print(f"The email has been found in {found} breaches.")
            print(f"Fields exposed: {', '.join(info.get('fields', []))}")
            print(f"Breaches have been found in the following sources: ")

            for source in info.get("sources", []):
                name = source.get("name", "Unknown")
                date = source.get("date", "Unknown date")
                print(f"+ {name} (Date: {date})")
            give_security_advice()

        else:
            print(f"No breaches found for {email}")

    else:
        print("No data to display or maybe an error has occurred.")

def give_security_advice():
    print("\nSecurity Advice to Keep Your Account Safe:")
    print("1.Change your password immediately.")
    print("2.Enable Two-Factor Authentication (2FA) if possible.")
    print("3.Use a password manager to generate and store a complex password.")
    print("4.Be cautious of phishing attempts. Do not click on suspicious links.")
    print("5.Review your account activity regularly for any unusual behavior.")
    print("6.Use unique passwords for every service to prevent one breach from affecting your other accounts.")



def main():

    email = input("Enter email address: ")
    n = validating_email(email)
    while n != True:
        email = input("Please enter a valid email address: ")
        n = validating_email(email)

    api_key = "333e6ffff7e97ae22dc91c2ebaa2d9379c96bf10"

    info = identifying_breaches(email, api_key)
    displaying_breaches(info, email)

if __name__ == "__main__":
    main()