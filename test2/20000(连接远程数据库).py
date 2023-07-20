import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    passwd="admin123",
    user="root"
)

print(mydb)

#
# import requests
#
# #the required first parameter of the 'get' method is the 'url':
# x = requests.get('https://www.baidu.com/')
#
# #print the response text (the content of the requested file):
# print(x.text)
#



