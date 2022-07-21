#!/usr/bin/env python3.5
# coding=utf-8
import os
import datetime
from time import sleep

dict = {}

fileInfoToList = []

#import webCrawl_cookie_2nd
import session_study

def save_as_file(sw_list:list):
    myfile = open("packageName.txt", 'w')
    for i in sw_list:
        if i is sw_list[-1]:
            myfile.write(i)
        else:
            myfile.write(i + '\n')
    myfile.close()




def readFile():
    L = []
    f = open("packageName.txt", "r")
    while True:
        test = f.readline()
        # test = test.strip()
        print("test is", test)
        sleep(0.5)
        if test == "":  # if not line:
            break
        elif test.startswith('#') or test.isspace():
            continue
        # if test.startswith('#') or test.isspace():
        #     continue
        # elif test == "":  # if not line:
        #     break
        L.append(test)
        print("L", L)
    f.close
    return L


def getNowTime():
    return str(datetime.datetime.now())


def setMd5sum(str):
    os.system("md5sum " + str + " |tee -a md5sum.txt")
    os.system("echo " + getNowTime() + " |tee -a md5sum.txt")


def setSha1sum(str):
    os.system("sha1sum " + str + " |tee -a sha1sum.txt")
    os.system("echo " + getNowTime() + " |tee -a sha1sum.txt")


# for i in readFile():
#     print i


# print fOut[1]
# print type(fOut[1])
# lastBlank = fOut[1].rindex('/')
# firstBlank = fOut[1].index('/')
# print "Last Black is", lastBlank
# print "First Black is", firstBlank
# print fOut[1][lastBlank + 1:]
def getPackageNameList(fOut):
    # fOut = readFile()
    newL = []
    for i in fOut:
        packageName = i[i.rindex("/")+1:].strip()
        newL.append(packageName)
    return newL


# print getPackageNameList()[0]
# print getPackageNameList()[1]

# print readFile()[0]

print("\n current os.path is", os.path, "\n")


# import os
# os.path.exists(test_file.txt)
# #True
# os.path.exists(no_exist_file.txt)
# #False

def fileExist(str):
    return os.path.exists(str)


def adv_wget(user_account: str,user_password: str, downloadLink: str, timesTry: int = 5) :
    #print("wget -c -t "+ str(timesTry) + " --no-check-certificate " + "--http-user=" + user_account + " --http-password=" + user_password + " " + downloadLink)
    os.system("wget -c -t "+ str(timesTry) + " --no-check-certificate " + "--http-user=" + user_account + " --http-password=" + user_password + " " + "'"+downloadLink +"'")


def packageDownload(L):
    for i in range(len(L)):
        if not fileExist(L[i]):
            # os.system("wget -c " + L[i])
            adv_wget("wu_j7", "'Tianyuan==xuu'", L[i])
            os.system("sync")
        else:
            print("Duplicate file")
            setMd5sum(L[i])


def fType():
    global dict
    L = getPackageNameList()
    for i in range(len(L)):
        lastComma = L[i].rindex(".")
        lastStr = L[i][lastComma + 1:]
        dict[L[i]] = lastStr


def cutLastComma(str):
    lastComma = str.rindex(".")
    lastStr = str[lastComma + 1:]
    return lastStr


def cutLastDash(str):
    lastComma = str.rindex("-")
    lastStr = str[lastComma + 1:]
    print("lastStr", lastStr)
    return lastStr


def tarFile(L):
    # L = getPackageNameList()
    for i in range(len(L)):
        try:
            #if cutLastDash(L[i]) == "REL.tgz":
            if L[i][-3:] == "tgz":
                if fileExist(L[i]):
                    if not fileExist("UpdateContainer"):
                        print("======================= Start to extract =======================")
                        os.system("tar xvf " + L[i])
                        os.system("sync")
                    else:
                        print('UpdateContainer already exist!!')
                        # raise ValueError('Duplicate extract file')
                else:
                    print("File does not exist!!!")
            #elif cutLastDash(L[i]) == "flashcontainer.tgz":
            elif L[i][-3:] == "flashcontainer.tgz":
                if fileExist(L[i]):
                    if not fileExist("FlashContainer"):
                        print("======================= Start to extract =======================")
                        os.system("tar xvf " + L[i])
                        os.system("sync")
                    else:
                        print
                        ('FlashContainer already exist!!')
                        # raise ValueError('Duplicate extract file')
                else:
                    print("File does not exist!!!")
        except ValueError:
            print("Sorry, it's not a Tar file")


def delFile(fileName):
    if fileExist(fileName):
        os.system("rm -rf " + fileName)
        print(fileName, "have been deleted")
    else:
        print("File is not exist!!!")


# packageDownload()
# tarFile()
# L = getPackageNameList()
# for i in range(len(L)):
#     setMd5sum(L[i])
# delFile('packageName.txt')
# delFile('test1.py')


def main():
    website = input("Please input the SVN address:")
    #SW address
    #website = "http://cnninvmlgcldc01:82/37w-gbt-cl1/linux/weekly_release/20220526.1_7140-rc3-37W-GBT-CL1/VW_CHN/CNS3.0_37W-VW_CHN-C714_RC3-MAIN-20220526.1-REL.tgz"
    sw_list = session_study.fetch_the_sw_list(website)
    save_as_file(sw_list)
    L = readFile()
    print("\n Step1 \n")
    packageDownload(L)
    print("\n Step2 \n")
    LName = getPackageNameList(L)
    # print("LName:",LName)
    for i in range(len(LName)):
        setMd5sum(LName[i])
        setSha1sum(LName[i])
    #tarFile(LName)
    # delFile('packageName.txt')
    # delFile('test1.py')


def main2():
    #website = input("Please input the SVN address:")
    #sw_list = session_study.fetch_the_sw_list(website)
    #save_as_file(sw_list)
    L = readFile()
    LName = getPackageNameList(L)
    print(LName)
    #tarFile(LName)
    for i in LName:
        try:
            #print(cutLastDash(i))
            print(i[-3:])
        except ValueError:
            print("Cannot be cut by last dash")


def main3():
    website = input("Please input the SVN address:")
    sw_list = session_study.fetch_the_sw_list(website)
    save_as_file(sw_list)


print("name1", __name__)

if __name__ == '__main__':
    main()
    #main3()
    #os.system("mv `pwd`/UpdateContainer/* `pwd`")
    #os.system("sync")
    # Map address
    # website = "http://cnninvmlgcldc01:82/37w-c-sample/linux/signature_release/20201127.2_9200-rc2-37W/zr3-navimap-TW_sec/CNS3.0_37W-zr3-navimap-TW_sec-0920_RC2-MAIN-20201127.2-REL.tgz"
    # main()
