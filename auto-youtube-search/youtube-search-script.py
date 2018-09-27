import json
from bs4 import BeautifulSoup
import webbrowser

def main():
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    filepath ='./data.txt'
    urlbase = 'https://www.youtube.com/results?search_query='
    objdict = {}
    songdict = {}
    obj = ""

    with open(filepath) as f:
        for line in f:
            line_s = line.rstrip()
            if line_s == "ENDFILE":
                break
            elif obj == "":
                obj = line_s
            elif line == "\n":
                objdict[obj] = songdict
                songdict = {}
                obj = ""
            else:
                song = line_s
                url = urlbase + obj + '+' + song
                webbrowser.get(chrome_path).open(url)
                print("Currently Viewing:",obj,song)
                print("Link:", end=' ')
                link = input()
                print("Description:", end=' ')
                desc = input()
                songinfo = {
                    'link':link,
                    'desc':desc
                }
                songdict[song] = songinfo
    with open('songdesc.json', 'w') as fp:
        json.dump(objdict, fp, indent = 4)

if __name__ == '__main__':
    main()
