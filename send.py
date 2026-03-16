import requests

class esp32():
    def __init__(self, ip):
        self.ip = ip

    def open(self):
        res = requests.get(f"http://{self.ip}:80/servo")
        print(res.status_code)

if __name__ == "__main__":
    esp32("172.20.10.2")