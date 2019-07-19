import requests

url = "https://uinames.com/api"

headers = {
    'Content-Type': "application/json",
    'X-RapidAPI-Host': "free-nba.p.rapidapi.com",
    'X-RapidAPI-Key': "SIGN-UP-FOR-KEY",
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "f256a76e-197b-48ac-8b12-f6f6ec20a2bb,2ad0b1b5-7b0e-4523-a76d-3e03fb79864f",
    'accept-encoding': "gzip, deflate",
    'referer': "https://uinames.com/api",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers)
# noinspection PyBroadException
try:
    assert response.status_code == 200
    print('[Passed]')
except:
    print('[Failed]\nstatus code is not 200')
