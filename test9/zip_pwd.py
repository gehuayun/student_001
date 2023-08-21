import zipfile


f = open('password.txt', 'w')
for id in range(1000000):
    password = str(id).zfill(6) + '\n'
    f.write(password)
f.close()


def pwd_file(zipFlie, password):
    try:
        zipFlie.extractall(pwd=bytes(password, 'utf8'))
        print('压缩包密码:', password)
    except:
        pass


def main():
    zipFlie = zipfile.ZipFile('./1.zip')
    pwd_list = open('./password.txt')
    for line in pwd_list.readlines():
        pwd = line.strip('\n')
        pwd_file(zipFlie, pwd)


if __name__ == '__main__':
    main()

