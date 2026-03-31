import requests


class esp32():
    def __init__(self, ip:str):
        self.ip = ip
        self.is_open = False


    def open(self):
        res = requests.get(f"http://{self.ip}:80/open")
        #print(res.status_code)
        self.is_open = True
    
    def close(self):
        res = requests.get(f"http://{self.ip}:80/close")
        #print(res.status_code)
        self.is_open = False

if __name__ == "__main__":
    esp32("172.20.10.2")