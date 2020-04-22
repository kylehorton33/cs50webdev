import requests

key = open("../../API_KEYS/fixer_io.txt").read()

def main():
  res = requests.get(f"http://data.fixer.io/api/latest?access_key={key}&symbols=EUR,USD") #fre subscription plan does not support changing base currency
  if res.status_code != 200:
    raise Exception("ERROR: Request API Unsuccessful")
  data = res.json()
  rate = data['rates']['USD']
  print(f"1 EUR is equal to {rate} USD")

if __name__ == "__main__":
    main()