import csv

def get():
    with open('respostes.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        respostes = []
        
        for i, row in enumerate(csv_reader):
            if not i == 0:
                dic = {}
                dic["time"] = row[0]
                dic["age"] = row[1]
                dic["age_int"] = int(row[1][:2:])
                dic["Precupacio"] = int(row[2])
                dic["knows"] = 0 if row[3] == "No" else 1
                dic["xarxes"] = row[4].split(", ")
                dic["perque"] = row[5]
                dic["us"] = row[6]
                dic["idees"] = row[7]
                dic["altres"] = row[8]
                #print(dic["age"], dic["age_int"])
                
                respostes.append(dic)
                
    return respostes


print(get())