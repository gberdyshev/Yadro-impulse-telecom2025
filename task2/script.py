import requests

def log(r):
    if r.status_code // 100 in [1, 2, 3]:
        print(f"Запрос: {r.status_code} {r.content}")
    else:
        raise Exception("Запрос завершился с кодом 4xx или 5xx!")


list_s = ["https://httpstat.us/200", "https://httpstat.us/203", "https://httpstat.us/502", "https://httpstat.us/305", "https://httpstat.us/404"]

for s in list_s:
    r = requests.get(s)
    log(r)