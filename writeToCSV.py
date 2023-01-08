import pandas as pd

def fillDF(_vertetesia, dataFrame):
    i=1
    while i<=100:
        try:
            with open ("full_texts/{vertetesia}/{numri}.txt".format(vertetesia=_vertetesia, numri=i), 'r', encoding='utf-8') as file:
                var = file.read()
                fake = 0 if _vertetesia=="fake" else 1
                dictionary = {'lajmi': var, 'vertetesia': fake}
                dataFrame = dataFrame.append(dictionary, ignore_index=True)
                i=i+1
                pass
        except:  
            i=i+1;
            file.close()
    return dataFrame
