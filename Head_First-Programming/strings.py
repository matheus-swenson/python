import time
import urllib.request
price = 99
while price > 4.74:
    time.sleep(1)
    page = urllib.request.urlopen("http://beans.itcarlow.ie/prices-loyalty.html")
    text = page.read().decode("utf8")
    where = text.find("$")
    start_of_price = where + 1
    end_of_price = where  + 5
    price = float(text[start_of_price:end_of_price])
    print(price)
print("Buy")