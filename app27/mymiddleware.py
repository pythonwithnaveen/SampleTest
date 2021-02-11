import requests
from bs4 import BeautifulSoup

# Global Variable
current_date = "";

class TimeMiddleware:
    def __init__(self, get_response):
        print("I am Constructor")
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        global current_date
        res = requests.request("GET", "https://www.timeanddate.com/worldclock/india")
        bs = BeautifulSoup(res.text, "html.parser")
        current_date = bs.find("span", {"id": "ctdat"}).text
        return response


def showDate():
    return current_date