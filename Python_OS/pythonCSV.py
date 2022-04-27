import csv
f = open("products_exports.csv")
csv_f = csv.reader(f)
for row in csv_f:
    print(row)

f.close()

hosts = [["workstation.local","192.168.25.46"],["workstation.cloud","10.2.5.6"]]
with open('hosts.csv','w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)
