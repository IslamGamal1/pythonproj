from bs4 import BeautifulSoup
import requests
import csv

csvFile = open('Results.csv', mode='a', newline="")
csvWriter = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
csvWriter.writerow(['Trade Name', 'Is Trade Seller', 'Phone Number'])

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
'Cookie': '__c7_4c89738rrujik1f721; abTestGroups=FPAI-afvI-ahC-rxC-smT-ctI-fdT-gp3-hp0I-iosellC-nhT-orI-faT-rlI-ssA-search0I-spI-ucI-um0-ut0-uhT-usrI-viI; bucket=desktop; sessVar=940eed8e-81df-4530-8ae9-bfefcc345c33; userid=ID=1d5ba57e-ff2c-469c-be2a-fd25d5e6058e; user=STATUS=0&HASH=3f5734cd9c493e34f6454f76316d777e&PR=&ID=1d5ba57e-ff2c-469c-be2a-fd25d5e6058e; GeoLocation=Town=&Northing=&Latitude=51.556568272&Easting=&ACN=0&Postcode=E113LD&Longitude=0.0094344562; SearchData=postcode=E113LD; postcode=postcode=E113LD; searches=; cookiePolicy=seen.; LPCKEY-p-245=670f7fe6-9a60-44c0-aa9d-379ed86c29ca8-34561%7Cnull%7CindexedDB%7C120; CAOCID=3a6c4132-0e8f-4a9b-9631-b7f1c99120a60-73434; __cf_bm=b7581b13160e1b28f04383c0b07cf4281726ee0e-1615044079-1800-ARgBh4gYgph7csJV0UBx+RKng7wGokuHSEoG6IYHIYnew1/R9kOoYzTYc3NxhcjJQXP3SqGFDrg6kcopHOcJ0xk=; ctmQuickQuotes=%7B%7D'
}

URL = "https://www.autotrader.co.uk/car-search?advertClassification=standard&postcode=E113LD&onesearchad=Used&onesearchad=Nearly%20New&onesearchad=New&advertising-location=at_cars&is-quick-search=TRUE&include-delivery-option=on&page=1"
req = requests.get(URL ,headers=headers)
soup = BeautifulSoup(req.text,"html.parser")
result = soup.find_all("li", class_="paginationMini__count")
firstpage = int(result[0].text.index("Page") +1)
maxpage = int(result[0].text[firstpage + 9:])

def getreqs():
    for j in range(1, maxpage):
        url = "https://www.autotrader.co.uk/car-search?advertClassification=standard&postcode=E113LD&onesearchad=Used&onesearchad=Nearly%20New&onesearchad=New&advertising-location=at_cars&is-quick-search=TRUE&include-delivery-option=on&page=" \
              + str(j)
        rsp = requests.get(url, headers=headers)
        data = rsp.text
        parsed = BeautifulSoup(data, features="html.parser")
        res1 = parsed.find_all("a", class_="js-click-handler listing-fpa-link tracking-standard-link")
        for i in range(0, len(res1)):
            try:
                temp = res1[i].attrs['href']
                carPage = temp[12:]
                prodUrl = "https://www.autotrader.co.uk/json/fpa/initial" + carPage
            except:
                print("Request Timeout")
            Req = requests.get(prodUrl, headers=headers)
            Req = Req.json()
            key = "name"
            if key in Req["seller"].keys():
                sellerName = Req["seller"]["name"]
            else:
                sellerName = " "
            phoneNo = Req["seller"]["primaryContactNumber"]
            isTrade = Req["seller"]["isTradeSeller"]
            codeCheck = phoneNo[1:3]
            if (codeCheck == "07") or (codeCheck == "44"):
                csvWriter.writerow([sellerName, isTrade, phoneNo])
getreqs()
csvFile.close()











