import csv
# f = open("products_exports.csv")
# csv_f = csv.reader(f)
# for row in csv_f:
    # print(row)

# f.close()

hosts = [["workstation.local","192.168.25.46"],["workstation.cloud","10.2.5.6"]]
with open('hosts.csv','w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts) # writes all rows available
# while writerow only writes one row at a time

with open("products_exports.csv") as products:
    reader = csv.DictReader(products)
    for row in reader:
        print("{} has price {}.".format(row["Handle"],row["Variant Price"]))
users = [{"name":"Sol Mansi","username":"solm","department":"IT infrastructure"},
         {"name":"Lio Nelson","username":"lion","department":"User Experience Research"},
         {"name":"Charlie Grey","username":"greyc","department":"Development"}]
keys = ["name","username","department"]
with open("by_department.csv","w") as by_department:
    writer = csv.DictWriter(by_department,fieldnames=keys)
    writer.writeheader()   # creates first line of the csv based on the keys we have provided
    writer.writerows(users)


