import pandas as pd

i=1
while i<101:
    try:
        with open("WriteToCsv.csv", "r") as file:
            print(file, file=open("full_texts/{vertetesia}/{numri}.txt".format(vertetesia='true', numri=i), 'w'))
            i = i + 1
    except:
        break
