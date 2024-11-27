import requests

def fetch_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data.get("type") == "single":
            print(data["joke"])
        elif data.get("type") == "twopart":
            print(data["setup"])
            print(data["delivery"])
        else:
            print("No joke found!")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_joke()
