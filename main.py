import speedtest

test = speedtest.Speedtest()
print("loading...")
test.get_servers()
print("Serverni tanlab olish...")
best = test.get_best_server()
print(f"Host: {best['host']}, Mamlakat: {best['country']}")


yuklash = test.download()
jonatish = test.upload()

print(f"Yuklash tezligi: {yuklash / 1024 / 1024:.2f} Mbit/s")
print(f"Jo'natish tezligi: {jonatish / 1024 / 1024:.2f} Mbit/s")