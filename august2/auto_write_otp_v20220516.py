import os
import shelve
import time

otp_status = False


def greenFont(str):
    return "\033[32m" + str + "\033[0m"


def redFont(str):
    return "\033[31m" + str + "\033[0m"


class AttrDisplay:
    """
    Provides an inheritable(inˈherədəb(ə)l) display overload method that shows instance with their class
    names and a name=value pair for each attribute stored on the instance itself (but not attrs inherited from its
    class). Can be mixed into any class, and will work on any instance
    """

    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%+3s' % (key, getattr(self, key)))
        return ', '.join(attrs)

    def __repr__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.gatherAttrs())


def auto_fill_zero(count_num: str) -> str:
    """

    :param count: input str
    :return: str which format as "0001"
    """
    if len(count_num) == 4:
        return count_num
    else:
        count_num = "0" + count_num
        return auto_fill_zero(count_num)


class serialNum(AttrDisplay):
    def __init__(self, year, month, day, model= None, count='1'):
        self.year = year
        self.month = month
        self.day = day
        self.model = '' if model is None else model
        self.count = count

    def __repr__(self):
        return self.year + self.month + self.day + self.model + auto_fill_zero(str(self.count))


def get_current_date():
    """

    :return: (str(year),str(month),str(day))
    """
    from time import localtime
    year = str(localtime().tm_year)
    if len(str(localtime().tm_mon)) == 1:
        month = "0" + str(localtime().tm_mon)
    else:
        month = str(localtime().tm_mon)
    if len(str(localtime().tm_mday)) == 1:
        day = "0" + str(localtime().tm_mday)
    else:
        day = str(localtime().tm_mday)

    # return year+month+day
    return (year, month, day)


def get_count_from_db(db='serial_num_list'):
    """

    :param db:
    :return: int
    """
    with shelve.open(db) as serial_num_db:
        a = serial_num_db.keys()
        # print(list(a))
        # convert list(str) to list(int)
        list_int = list(map(int, list(a)))
        return max(list_int)


def get_db_info(db='serial_num_list'):
    with shelve.open(db) as serial_num_db:
        print("The size of db is", len(serial_num_db))
        for key in serial_num_db:
            print('%-3s=> %s' % (key, serial_num_db[key]))


def get_newest_value(db='serial_num_list'):
    with shelve.open(db) as serial_num_db:
        return serial_num_db[str(get_count_from_db(db))]

def get_db_value(key, db = 'serial_num_list'):
    with shelve.open(db) as serial_num_db:
        return serial_num_db[str(key)]

def save_to_db(head_unit: str, db='serial_num_list'):
    """

    :param head_unit: give instance's name
    :param db: give shelve.file's name
    :return: show db's internal info.
    """
    with shelve.open(db) as serial_num_db:
        serial_num_db[head_unit.count] = head_unit
        print(greenFont("Save %s to %s successfully!!" % (head_unit, db)))


def main():
    date = get_current_date()
    test1 = serialNum(date[0], date[1], date[2])
    # test1 = serialNum(date[0], date[1], date[2], count='2')
    with shelve.open('otp_scripts/serial_num_list') as serial_num_db:
        serial_num_db[test1.count] = test1


def main2():
    with shelve.open('otp_scripts/serial_num_list') as serial_num_db:
        print(len(serial_num_db))
        for key in serial_num_db:
            # print('%-3s=>%s' % (key, db[key]))
            print("%-s=>%s" % (key, serial_num_db[key]))
        a = serial_num_db.keys()
        print(list(a))


def repr_message(message: str):
    padding_len = '%' + str(int(len(message) / 2) + 35) + 's'
    return "=" * 70 + "\n" + padding_len % message + "\n" + "=" * 70 + "\n"



def otp_pexpect(head_unit: str):
    """
    Do pexpect process
    :return:
    """
    global otp_status
    import pexpect, sys
    dir_path = 'record_data'
    if os.path.exists(dir_path):
        with open(dir_path + '/' + head_unit + '_MQB_GBT' +".txt", 'a')as my_log_file:
            my_log_file.write(repr_message(time.asctime()))
            print(repr_message(time.asctime()))
            # my_log_file = '' if record_file == '' else sys.stdout
            print(repr_message(head_unit))
            my_log_file.write(repr_message(head_unit))
            print("sudo ./MQB_VW_CHN_Banma.sh " + head_unit)
            p1 = pexpect.spawn("sudo ./MQB_VW_CHN_Banma.sh " + head_unit, timeout=None, logfile=my_log_file,
                               encoding="utf-8")
            response = p1.expect(["password for jpcc", "This can be only done ONCE"], timeout=10)
            if response == 0:
                p1.sendline("jpcc")
            elif response == 1:
                pass
            # try:
            #     issue_info = "HW version"
            #     p1.expect("HW version: 18",timeout=5)
            #     my_log_file.write("=>"+"HW version: 18")
            #     issue_info = 'HW variant'
            #     p1.expect("HW variant: 65591",timeout=5)
            #     my_log_file.write("=>"+"HW variant: 65591")
            #     issue_info = 'System variant'
            #     p1.expect("System variant: 702001",timeout=5)
            #     my_log_file.write("=>"+"System variant: 702001")
            #     issue_info = "PCB serial number"
            #     p1.expect("PCB serial number: " + str(head_unit),timeout=5)
            #     my_log_file.write("=>"+"PCB serial number: " + str(head_unit))
            try:
                issue_info = "HW version"
                p1.expect("HW version: 18", timeout=5)
                my_log_file.write("=>" + "HW version: 18")
                issue_info = 'HW variant'
                p1.expect("HW variant: 65590", timeout=5)
                my_log_file.write("=>" + "HW variant: 65590")
                issue_info = 'System variant'
                p1.expect("System variant: 304001", timeout=5)
                my_log_file.write("=>" + "System variant: 304001")
                issue_info = "PCB serial number"
                p1.expect("PCB serial number: " + str(head_unit), timeout=5)
                my_log_file.write("=>" + "PCB serial number: " + str(head_unit))
            except pexpect.TIMEOUT:
                raise pexpect.TIMEOUT('\n' + repr_message("There is no matched base_info of " + issue_info))
            except pexpect.EOF:
                print(redFont(repr_message("pexpect.EOF Error_1")))
                # print("We are here, Position 3")
                return otp_status
            p1.expect("Is this correct")
            p1.sendline("yes")
            try:
                # p1.expect('otp cell \[1\]')
                # Have to add '\' (backslash) before '[' or ']'(bracket)
                p1.expect("otp cell \[2\] written", timeout=60)
                print(greenFont(repr_message("OTP has written done")))
                otp_status = True
                return otp_status
            except pexpect.EOF:
                print(redFont(repr_message("pexpect.EOF Error_2")))
                # print("We are here, Position 3")
                return otp_status
            except pexpect.TIMEOUT:
                print(redFont(repr_message("pexpect.TIMEOUT Error")))
                # print("We are here, Position 3")
                # p1.close()
                # pexpect.EOF
                return otp_status
    else:
        print(redFont(repr_message("record directory path is not found")))


def delete_hu_in_db(count: str, db='serial_num_list'):
    with shelve.open(db) as serial_num_db:
        if count in serial_num_db.keys():
            del serial_num_db[count]
            print(greenFont(count + " is deleted now!!!!"))
        else:
            print(redFont(count + " is not found, cannot be deleted!!!!"))
            # greenFont("Save %s to %s successfully!!" % (head_unit, db))


def test_value():  # Change global in module
    global otp_status
    otp_status = True


def get_latest_db_item(db='serial_num_list'):
    with shelve.open(db) as serial_num_db:
        latest = serial_num_db[max(list(serial_num_db.keys()))]
    return latest


if __name__ == '__main__':
    # print(get_current_date())
    # main()
    # main2()
    print(greenFont(repr_message("The newest db[value] is " + str(get_newest_value()))))
    print("Max count:", str(get_count_from_db()))
    print("type(Max count):", type(get_count_from_db()))
    get_db_info()
    date = get_current_date()
    print('str(get_count_from_db() + 1):', str(get_count_from_db() + 1))
    newHU = serialNum(date[0], date[1], date[2],count=str(get_count_from_db() + 1))
    # newHU = serialNum(date[0],date[1],day='22',count='7')
    # save_to_db(newHU)
    # print(str(newHU))
    print(greenFont(repr_message("Serial Num: " + str(newHU))))
    # save_to_db(newHU)
    # otp_pexpect(str(newHU))
    # delete_hu_in_db('0008')
    #
    res = input(repr_message("Input \" correct \" to continue"))
    # res = 'correct'                             # test-only
    if res.lower() == 'correct':
        if otp_pexpect(str(newHU)):
            print(greenFont(repr_message(str(otp_status))))
            save_to_db(newHU)
            get_db_info()
        else:
            print(redFont(repr_message('otp status: ' + str(otp_status))))
    else:
        pass