import requests  # εισαγωγή της βιβλιοθήκης

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break

url = input("Insert url:")  # προσδιορισμός του url

with requests.get(url) as response:  # το αντικείμενο response
    html = response.text
    more(html)

    header = response.headers
    print("Ο εξυπηρετητής χρησιμοποιεί λογισμικό:", header['server'])
    cookies = response.cookies
    print("Η σελίδα χρησιμοποιεί τα παρακάτω cookies:\n",cookies.get_dict())

    print("Ο εξυπηρετητής χρησιμοποιεί λογισμικό:", header['server'])
