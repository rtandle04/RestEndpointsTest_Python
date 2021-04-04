import pandas
import requests

#print(response.json())
#print(response.text())
#print(response.content())
class ExcelDTO(object):
    def __init__(self,sno,requestType,apiEndpoint,body,param):
        self.sno=sno
        self.requestType=requestType
        self.apiEndpoint=apiEndpoint
        self.body=body
        self.param=param
        
data = pandas.read_excel('C:\\pythonworkspace\\APIEndpoints.xlsx', sheet_name='Sheet1')
list=data.values.tolist()
list_instances = []
for p in list:
    list_instances.append(ExcelDTO(*p))
    print(p)
count=0
for obj in list_instances:
    count=count+1
    print("===================== ============================ ========================= ======================== ===================== ==========================")
    print(obj.requestType,obj.apiEndpoint)
    if(obj.requestType =='GET'):
        response=requests.get(obj.apiEndpoint)
        
        if (response.status_code == 200):
            print(count,". The request was a success")
        elif (response.status_code !=200):
            print(count,"The request was failed")
    elif(obj.requestType=='POST'):
        response=requests.post(obj.apiEndpoint)
        if (response.status_code == 200):
            print(count,"The request was a succsss")
        elif (response.status_code !=200):
            print(count,"The request was failed")