import requests
import time

def measure_load_time(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    load_time = end_time - start_time
    return load_time

def main():
    url = "https://chatgpt.com"
    load_time = measure_load_time(url)
    print(f"Loaded {url} in {load_time:.2f} seconds")

if __name__ == "__main__":
    main()
