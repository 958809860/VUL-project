import xlwt,json

def readJsonfile():
    jsobj = json.load(open(r'E:\gitclone\VUL-project\JsonToExcel\wingProperties.json'))
    return jsobj

def jsonToexcel():
    jsonfile = readJsonfile()
    print (jsonfile)
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('json')
    ll = list(jsonfile[0].keys())
    for i in range(0,len(ll)):
        sheet1.write(0,i,ll[i])
    for j in range(0,len(jsonfile)):
        m = 0
        ls = list(jsonfile[j].values())
        for k in ls:
            sheet1.write(j+1,m,k)
            m += 1
    workbook.save('jsonExcel.xls')                
jsonToexcel()