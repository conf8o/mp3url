import requests

print("Download mp3 file having .mp3 extension from URL.")
print("Input URL. Exit when input \"exit\".")
i = 0
while (url := input("URL(https://[domain]/[file].mp3): >>")) != "exit":
    doc = requests.get(url)
    open(f"output/{i}.mp3", "wb").write(doc.content)
    i += 1
