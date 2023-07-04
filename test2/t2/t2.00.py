import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin123"
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



