from plyer import notification
import requests
from bs4 import BeautifulSoup


def notifyMe(title,message):
    notification.notify(
        title=title,
        message = message,
        app_icon = "D:\Corona Virus\icon.ico",
        timeout = 10
    )

def getData(url):
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
    # notifyMe("Subha", "Stay Home & Stay Safe")
    myHtmData = getData("https://www.mohfw.gov.in/")

    print(myHtmData)
    soup = BeautifulSoup( myHtmData, 'html.parser')
    # print(soup.prettify())
    for tr in soup.find_all('thead')[4].find_all("tr"):
        print(tr.get_text())
