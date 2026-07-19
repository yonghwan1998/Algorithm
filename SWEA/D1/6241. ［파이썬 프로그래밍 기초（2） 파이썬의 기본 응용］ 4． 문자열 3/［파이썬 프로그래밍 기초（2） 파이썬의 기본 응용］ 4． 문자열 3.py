url = input()
protocol = url[:url.index('://')]
host = url[url.index('://') + 3: url.index('.com') + 4]
others = url[url.index('.com/') + 5:]

print(f"protocol: {protocol}")
print(f"host: {host}")
print(f"others: {others}")