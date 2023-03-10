
mas = ["Afnr", "12"," red"]

def CountQuanntityElementByArray(arr):

    massiv = []
    for i in mas:
        countEl = 0
        for j in i:
            # print(j)
            countEl +=1
        if countEl<=3:
            massiv.append(i)
    print(massiv)

CountQuanntityElementByArray(mas)
print("==="*10)
mas = ["5fnfaa","45", "afvar","gh","alcrc","ty6"]
CountQuanntityElementByArray(mas)
print("==="*10)
mas = ["c;dao", "vnzk3.", ",.h", ")(-", "dsar(n"]
CountQuanntityElementByArray(mas)
