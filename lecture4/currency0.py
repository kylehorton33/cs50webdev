import requests

key = open("../../API_KEYS/fixer_io.txt").read()

def main():
  res = requests.get(f"http://data.fixer.io/api/latest?access_key={key}&symbols=EUR,USD")
  if res.status_code != 200:
    raise Exception("ERROR: Request API Unsuccessful")
  data = res.json()
  print(data)

if __name__ == "__main__":
    main()