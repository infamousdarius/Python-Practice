import webbrowser

if __name__ == '__main__':

    url = 'http://google.com'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'.lower()
    print(chrome_path)
    i = 1
    while i <= 5:
        webbrowser.get(chrome_path).open(url)
        i += 1
