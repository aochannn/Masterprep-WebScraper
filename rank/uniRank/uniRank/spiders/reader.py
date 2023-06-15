import csv

with open('cons.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    names=[]
    rows = list(reader)
    count=0
    #for i in range(740):
    print(rows[0][0])
        
# with open('cons.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerows(rows)