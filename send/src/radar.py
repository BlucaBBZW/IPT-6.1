from bs4 import BeautifulSoup
import requests

class Radar:
    url = "https://polizei.lu.ch/organisation/sicherheit_verkehrspolizei/verkehrspolizei/spezialversorgung/verkehrssicherheit/Aktuelle_Tempomessungen"

    @staticmethod
    def get():
        res = requests.get(Radar.url)

        html = BeautifulSoup(res.content, 'html.parser')

        htmlradarList = html.find(id="radarList")
        htmlradarList = htmlradarList.prettify()

        is_semi = False
        print_next = False

        radarList = []
        
        for line in htmlradarList.splitlines():
                if("Geschwindigkeitsmessanlagen semistationär" in line):
                        is_semi = True
                if("Geschwindigkeitsmessanlagen stationär" in line):
                        is_semi = False
                
                if(is_semi):
                        if(print_next):
                                radarList.append(line.lstrip(' '))
                                print_next = False

                        if("<a href" in line):
                                print_next = True

        return radarList