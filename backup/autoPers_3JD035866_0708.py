#! /usr/bin/env python3.5
import binascii
import sys

import pexpect
from auto_write_otp_v20220516 import *

write_status = False


def str_to_hexStr(str_info):
    return binascii.hexlify(str_info.encode('utf-8')).decode('utf-8')

def str_to_hexStr_v2(char):
    # print([x for x in '3GB035866A'])
    # print([str_to_hexStr(i) for i in [x for x in char]])
    # print(' '.join(['33', '47', '42', '30', '33', '35', '38', '36', '36', '41']))
    return ' '.join([str_to_hexStr(i) for i in [x for x in char]])


def do_pexpect(**kwargs):
    ip = "192.168.1.4"
    global write_status
    assert 'serial_num' in kwargs, redFont(
        "\n" + "?" * 70 + "\n" + "%35s%s\n" % ('serial_num', ' is missing') + "?" * 70 + "\n")
    log_file = kwargs['serial_num'] + "_pers" + "_log_file" + '.txt'
    hu_zone = "/var/tmp/"
    # hu_zone = "/tmp/"
    with open(log_file, 'a') as my_log_file:
        p = pexpect.spawn("ssh root@" + ip, timeout=None, logfile=my_log_file, encoding='utf-8')
        # p.expect("login")
        # p.sendline("root")
        p.expect("password")
        p.sendline("root")
        print(repr_message(greenFont(kwargs['serial_num'])))
        # # initial vkms
        # p.sendline("cd /tmp/")
        # # p.sendline("chmod +x vkms_init_pss.sh")
        # # p.sendline("./vkms_init_pss.sh")
        # p.sendline("chmod +x " + hu_zone + "vkms_init_pss.sh")
        # p.sendline(hu_zone + "vkms_init_pss.sh")
        # try:
        #     p.expect("Finished", timeout=5)
        #     print(greenFont(repr_message("Initializing VKMS finished")))
        #     write_status = True
        # except pexpect.TIMEOUT:
        #     write_status = False
        #     print(redFont(repr_message("VKMS error")))
        p.sendline("mount-read-write.sh")
        # If HU is brand new, have to InitPersistence script
        p.sendline("chmod +x " + hu_zone + "tsd.persistence.client.mib3.app.InitPersistence")
        p.sendline(hu_zone + "tsd.persistence.client.mib3.app.InitPersistence")
        p.sendline("chmod +x " + hu_zone + "tsd.persistence.client.mib3.app.SetKey")
        p.sendline(hu_zone + "tsd.persistence.client.mib3.app.SetKey --ns 0x80000008 --key 0x00  --val 0xe5")
        # Set serial_num
        time.sleep(5)
        if 'serial_num' in kwargs:
            p.sendline(
                hu_zone + "tsd.persistence.client.mib3.app.SetKey --ns 0x3000000 --key 0xF18C  --val 0x" + str_to_hexStr(
                    kwargs['serial_num']).upper())
        else:
            print(redFont("?" * 70 + "\n" + "%35s%s\n" % ('serial_num', ' no change') + "?" * 70 + "\n"))
        # # Set Fazit-id
        if 'fazit' in kwargs:
            p.sendline(
                hu_zone + "tsd.persistence.client.mib3.app.SetKey --ns 0x3000000 --key 0xF17C  --val 0x" + str_to_hexStr(
                    kwargs['fazit']).upper())
        else:
            print(redFont("?" * 70 + "\n" + "%30s%s\n" % ('fazit', ' no change') + "?" * 70 + "\n"))
        # Set Hardware version >> X13 (SOP1.5)/(37W_SOP1.0)
        if 'hw_version' in kwargs:
            p.sendline(
                hu_zone + "tsd.persistence.client.mib3.app.SetKey --ns 0x3000000 --key 0xF1A3  --val 0x" + str_to_hexStr(
                    kwargs['hw_version']).upper())
            try:
                p.expect("key: 61859 slot: 0 status: 0", timeout=5)
                print(greenFont(repr_message("Key(61859) has written")))
                write_status = True
            except pexpect.TIMEOUT:
                write_status = False
                print(redFont(repr_message("Something is going wrong")))
        else:
            print(redFont("?" * 70 + "\n" + "%35s%s\n" % ('hw_version', ' no change') + "?" * 70 + "\n"))
        # Set Software version >> C420
        if 'sw_version' in kwargs:
            p.sendline(
                hu_zone + "tsd.persistence.client.mib3.app.SetKey --ns 0x3000000 --key 0xF189  --val 0x" + str_to_hexStr(
                    kwargs['sw_version']).upper())
            try:
                p.expect("key: 61833 slot: 0 status: 0", timeout=5)
                print(greenFont(repr_message("Key(61833) has written")))
                write_status = True
            except pexpect.TIMEOUT:
                write_status = False
                print(redFont(repr_message("Something is going wrong")))
        else:
            print(redFont("?" * 70 + "\n" + "%35s%s\n" % ('sw_version', ' no change') + "?" * 70 + "\n"))
        # Set PartNum >> 3GB035866A
        if 'part_num' in kwargs:
            # Oct   Dec   Hex   Char
            # 040   32    20    SPACE
            # p.sendline(
            #     hu_zone + "tsd.persistence.client.mib3.app.SetKey --ns 0x03000000 --key 0xF187 --val 0x" + str_to_hexStr(
            #         kwargs['part_num']).upper())
            # p.sendline(
            #     hu_zone + "tsd.persistence.client.mib3.app.SetKey --ns 0x03000000 --key 0xF191 --val 0x" + str_to_hexStr(
            #         kwargs['part_num']).upper())
            p.sendline(
                hu_zone + "tsd.persistence.client.mib3.app.SetKey --ns 0x03000000 --key 0xF187 --val 0x" + str_to_hexStr(
                    kwargs['part_num']).upper() + '2020')
            p.sendline(
                hu_zone + "tsd.persistence.client.mib3.app.SetKey --ns 0x03000000 --key 0xF191 --val 0x" + str_to_hexStr(
                    kwargs['part_num']).upper() + '2020')
            try:
                # p.expect("key: 61841 slot: 0 status: 0", timeout=5)
                # key: 61841 slot: 0 status: 0 data: 33 47 42 30 33 35 38 36 36 44 20
                p.expect("key: 61831 slot: 0 status: 0 data: " + str_to_hexStr_v2(
                    kwargs['part_num'])+ " 20 20", timeout=5)
                print(greenFont(repr_message("Key(61831):" + kwargs['part_num'] + "(space) has written")))
                p.expect("key: 61841 slot: 0 status: 0 data: " + str_to_hexStr_v2(
                    kwargs['part_num'])+ " 20 20", timeout=5)
                print(greenFont(repr_message("Key(61841):" + kwargs['part_num'] + "(space) has written")))
                write_status = True
            except pexpect.TIMEOUT:
                write_status = False
                print(redFont(repr_message("Something is going wrong")))
        else:
            print(redFont("?" * 70 + "\n" + "%35s%s\n" % ('part_num', ' no change') + "?" * 70 + "\n"))
        pexpect.EOF
        p.sendline("sync")
        p.sendline("exit")
        p.expect("closed")
        # p.expect(pexpect.EOF)
        # print("\033[32m" + "PASS" + "\033[0m")  # print Green font


def copy_file_to_HU(file_path: str):
    ip = "192.168.1.4"
    hu_zone = "/var/tmp/"
    # hu_zone = "/tmp/"
    dest_path = " root@192.168.1.4:" + hu_zone
    # os.system('scp' + file_path + dest_path )
    print("scp " + file_path + dest_path)
    p = pexpect.spawn("scp " + file_path + dest_path, timeout=60, logfile=sys.stdout, encoding='utf-8')
    p.expect("password")
    p.sendline("root")
    p.expect("100%")
    print(greenFont("*" * 70 + "\n" + "%35s\n" % ('copy file to HU') + "*" * 70 + "\n"))


# def copy_file_to_HU_v2():
#     p_scp = pexpect.spawn("scp /home/jpcc/Documents/modify_systeminfo/vkms_init_pss.sh root@192.168.1.4:/tmp/", timeout=60, logfile=sys.stdout, encoding='utf-8')
#     p_scp.expect("password")
#     p_scp.sendline("root")
#     p_scp.expect("100%  117KB")
#     print(greenFont("*" * 70 + "\n" + "%35s\n" % ('copy file to HU') + "*" * 70 + "\n"))
#     p_scp.close()

def set_fazit_dict(keyNum = 8):
    list1 = [x for x in range(1,keyNum)]
    list_svw = ['X9G-10103.05.2299990507','X9G-10103.05.2299990508','X9G-10103.05.2299990509','X9G-10103.05.2299990510']
    list_faw = ['X9G-10203.05.2299990537','X9G-10203.05.2299990538','X9G-10203.05.2299990539','X9G-10203.05.2299990540']
    return dict(zip(list1,list_svw+list_faw))


if __name__ == '__main__':
    # ##print(get_serial_num())
    # # copy vkms_init_pss.sh to HU
    # p_scp = pexpect.spawn("scp /home/jpcc/Documents/modify_systeminfo/vkms_init_pss.sh root@192.168.1.4:/tmp/",
    #                       timeout=60, logfile=sys.stdout, encoding='utf-8')
    # p_scp.expect("password")
    # p_scp.sendline("root")
    # p_scp.expect("100%  117KB")
    # print(greenFont("*" * 70 + "\n" + "%35s\n" % ('copy file to HU') + "*" * 70 + "\n"))

    #
    # do_pexpect(serial_num ="20220420W0002",sw_version="C071",hw_version="X30",part_num="5HG035866F")
    ####
    # serialNum = "VWX9GA88880006"
    # #fazitId = "X9G-10127.05.2299990501"
    # #fazitId = "X9G-10127.05.2299990502"
    # #fazitId = "X9G-10130.05.2299990501"
    # #fazitId = "X9G-10130.05.2299990507"
    # #fazitId = "X9G-10130.05.2299990508"
    # #fazitId = "X9G-10130.05.2299990509"
    ### 6/13/2022
    # serialNum_0613 = "VWX9GA88880013"
    # fazit_0613_list = ["X9G-10103.05.2299990501", "X9G-10103.05.2299990502", "X9G-10103.05.2299990503",
    #               "X9G-10103.05.2299990504", "X9G-10103.05.2299990505", "X9G-10203.05.2299990534",
    #               "X9G-10203.05.2299990535"]
    # do_pexpect(serial_num=serialNum, sw_version="C814", hw_version="X30", part_num="3GB035866D")

    # do_pexpect(serial_num=serialNum_0613, hw_version="X15", sw_version="C460", part_num="3GB035866A",
    #            fazit=fazit_0613_list[6])

    copy_file_to_HU("/home/jpcc/Documents/modify_systeminfo/tsd.persistence.client.mib3.app.InitPersistence")
    copy_file_to_HU("/home/jpcc/Documents/modify_systeminfo/tsd.persistence.client.mib3.app.SetKey")
    import pprint
    #fazit_dict = set_fazit_dict()
    serialNum_0704 = input("Please input the serial num (i.e. 0701202200XX):")
    print(repr_message("Serial number: " + serialNum_0704))
    # fazitId_0712 = input("Please input the fazit id (i.e. X9G-101XX.XX.XX9999XXXX")
    #choice = input("Please select the fazit-id from the below list:\n" + pprint.pformat(fazit_dict))
    fazitId_0715 = input("Please select the fazit-id (i.e. X9G-10XXX.XX.XX9999XXXX:")
    #fazitId_0712 = fazit_dict[int(choice)]
    print(repr_message("Fazit id: " + fazitId_0715))
    # serialNum_0620 = 'VWX9GY0170935'
    # serialNum_0620 = '202206170014'
    # serialNum_0620 = 'VWX9GA88880014'
    #do_pexpect(serial_num=serialNum_0704, hw_version="X02", sw_version="C051", part_num="3JD035866")
    do_pexpect(serial_num=serialNum_0704, fazit= fazitId_0715,hw_version="X03", sw_version="C078", part_num="3JD035866")
    #do_pexpect(serial_num=serialNum_0704, hw_version="X02")
    # do_pexpect(serial_num = serialNum, sw_version = 'C814')
    if write_status:
        print(greenFont("=" * 70 + "\n" + "%35s%s\n" % ('write_status:', write_status) + "=" * 70 + "\n"))
    else:
        print(redFont("?" * 70 + "\n" + "%35s%s\n" % ('write_status:', write_status) + "?" * 70 + "\n"))
    def str_to_hexStr(str_info):
        return binascii.hexlify(str_info.encode('utf-8')).decode('utf-8')
