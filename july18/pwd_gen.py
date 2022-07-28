# 87122064
import random, time

original = '87122064'
# reverse

# original = ''.join([str(random.randint(1,9)) for x in range(8)])

reverse = original[::-1]

# res = []

randomListSum = []


def count_occur_times(pwd: str):
    """
    count each item(format: str) appear times
    :param pwd:
    :return: As dict, key: item ; value: appear times
    """
    count_dict = {}
    for i in pwd:
        if not i in count_dict.keys():
            count_dict[i] = 1
        else:
            count_dict[i] += 1
    return count_dict


def filter_pwd(pwd: str):
    global randomListSum
    #print('count_occur_times:', count_occur_times(pwd))
    #print('count_occur_times(pwd).values()', count_occur_times(pwd).values())
    for i in count_occur_times(pwd).values():
        if i > 2:
            print('too many duplicate')
            #pprint.pprint(count_occur_times(pwd))
            break
    else:
        print("Success to create password!!!")
        pprint.pprint(count_occur_times(pwd))
        print("reverse_randomListSum:" , randomListSum[::-1])
        return pwd
    return set_pwd(pwd)

def set_pwd(pwd: str):
    """
    :param pwd: input the original password
    :return: reverse the pwd and add a random number into each items, then output w/o digit 4
    """
    global randomListSum
    # pwd_res, res = [], []
    pwd_res, res, randomList = [], [], []
    reverse_pwd = pwd[::-1]
    #for i in pwd[::-1]:
    for i in reverse_pwd:
        random_num = random.randint(1, 9)
        #print('random_num:', random_num)
        randomList.append(random_num)
        res.append(int(i) + random_num)
    randomListSum.append(randomList)
    print("\n There is a turn\n RandomList is", randomList, '\n')
    pwd_res = ''.join([str(x - 10) if x > 9 else str(x) for x in res])
    print('The current pwd is', pwd_res)
    if '4' in pwd_res:
        print('pwd has digit 4')
        return set_pwd(pwd_res)
    else:
        return filter_pwd(pwd_res)


import importlib, importlib.util


def module_directory(name_module, path):
    """
    :param name_module: given custom module name
    :param path: absolute path
    :return: Create a module based on the provided spec
    """
    # specify the module that needs to be
    # imported relative to the path of the
    # module
    P = importlib.util.spec_from_file_location(name_module, path)
    # creates a new module based on spec
    import_module = importlib.util.module_from_spec(P)
    # executes the module in its own namespace
    # when a module is imported or reloaded.
    P.loader.exec_module(import_module)
    return import_module  # Create a module based on the provided spec.


def list_func_in_module(path: str):
    """
    Get the list of func/class in module via file path.
    :param path: input the absolute file path 
    :return: list of func/class
    """
    for module in os.listdir(path):
        # print([func for func in dir(module1) if not func.startswith('__') ])
        # module_name = module[:-3]
        if not module.startswith('__') and module.endswith('.py'):
            print('module name is', module)
            # result = module_directory('result', path + '/' + module)          # << Another way to solve import issue
            module = importlib.import_module(module[:-3])  # Import a module by assignment statement
            print([func for func in dir(module) if not func.startswith('__')])







if __name__ == '__main__':
    import pprint
    #
    # pprint.pprint(count_occur_times('87122064'))
    #
    #
    # def selfTest(n=100):
    #     for i in range(n):
    #         # if '4' in set_pwd('87122064'):
    #         #     print('failed')
    #         res = set_pwd('132131231')
    #         print(res)
    #         pprint.pprint(count_occur_times(res))
    #
    #
    # selfTest(10)
    #
    # import os, importlib
    #
    # for module in os.listdir("/home/jpcc/PycharmProjects/pythonProject_july/july12"):
    #     # print([func for func in dir(module1) if not func.startswith('__') ])
    #     # module_name = module[:-3]
    #     if not module.startswith('__') and module.endswith('.py'):
    #         print('module name is', module)
    #         my_module = importlib.import_module(module[:-3])
    #         # result = module_directory('result', "/home/jpcc/PycharmProjects/pythonProject_july/july12" + '/' + module)
    #         print([func for func in dir(my_module) if not func.startswith('__')])
    #
    # list_func_in_module("/home/jpcc/PycharmProjects/pythonProject_july/july12")
    #
    # from mapattrs import set_random_dict
    #
    # sample_dict = set_random_dict(10)
    # print(sample_dict)
    #
    # sample_dict_1 = {'Richard Amos': 5, 'Alvin Barton': 1, 'Larry Chestnut': 9, 'Richard Ivey': 4, 'Rico Plunkett': 7,
    #                  'Angela Samuels': 7, 'William Phillips': 8, 'Alma Hernandez': 8, 'Ernestine Hamberg': 9,
    #                  'Chana Rembert': 7}

    # print('New password:', filter_pwd(set_pwd('87122064')))
    # print('New password:', set_pwd('87122064'))
    # pprint.pprint("randomListSum: ", randomListSum)
    # print("randomListSum: ", randomListSum)

    set_pwd('87122064')
    randomListSum = []
    random_pwd = ''.join([str(a) for a in [random.randint(1,10) for x in range(10)]])
    print('random_pwd', random_pwd)
    set_pwd(random_pwd)