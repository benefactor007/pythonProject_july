from mapattrs import set_random_dict

if __name__ == '__main__':
    # open('temp', 'w').write('abd\n')
    dict_case =  set_random_dict(10000)
    # print(dict_case)
    for i in dict_case.keys():
        with open('temp_case', 'a') as f:
            f.write(("%s => %s\n")%(i, str(dict_case[i])))
