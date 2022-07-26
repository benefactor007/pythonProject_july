from pwd_gen import count_occur_times
# import os
# import sys
# current_dir = os.path.abspath(os.path.dirname(__file__))
# sys.path.append(current_dir)
# sys.path.append("..")

"""
example 1:
New password: 53223701
randomListSum:  [[5, 8, 5, 6, 1, 2, 3, 8], [3, 3, 8, 2, 2, 8, 7, 5], [1, 2, 9, 2, 8, 6, 7, 2]]

example 2:
New password: 65756991
randomListSum:  [[2, 9, 7, 3, 4, 8, 2, 3]]

example 3:
New password: 39769107
randomListSum:  [[7, 3, 4, 1, 7, 5, 2, 5], [5, 2, 5, 1, 2, 6, 2, 8], [6, 4, 4, 8, 1, 2, 1, 1], [2, 8, 2, 9, 3, 7, 5, 2], [7, 3, 4, 1, 4, 1, 5, 5], [7, 4, 1, 2, 2, 6, 7, 3]]

"""

#  for a in (x for x in dir(I) if not x.startswith('__')):


def check_count_in_dict(pwd: str):
    for i in count_occur_times(pwd).values():
        if i > 2:
            return False

    else:
        return True



def decode_pwd(new_pwd:str, rls: list):
    print(len(rls))
    # res = []
    for i in range(len(rls)):
        res = []
        # for j in rls[i]:
            # print(j)
            # res.append(j)
        # print('res', res)
        for p, j in zip(new_pwd,rls[i]):
            # print(j,':', p)
            if j > int(p):
                res.append(str(int(p) + 10 - j))
            else:
                res.append(str(int(p) - j))
        print(res[::-1])
        if 4 in res[::-1]:
            print('\n we got 4\n')
            print(count_occur_times(''.join(new_pwd)))
            new_pwd = ''.join(res[::-1])
            print('new pwd', new_pwd)
        elif not check_count_in_dict(''.join(res[::-1])):
            print('digit appears more than 2 times')
            print(count_occur_times(''.join(new_pwd)))
            new_pwd = ''.join(res[::-1])
            print('current new_pwd', new_pwd)

        else:
            new_pwd = res[::-1]
            new_pwd = [str(x) for x in new_pwd]
            new_pwd = ''.join(new_pwd)
            print(new_pwd)
            print(count_occur_times(''.join(new_pwd)))

if __name__ == '__main__':
    decode_pwd('65756991', [[2, 9, 7, 3, 4, 8, 2, 3]])
    decode_pwd('53223701', [[5, 8, 5, 6, 1, 2, 3, 8], [3, 3, 8, 2, 2, 8, 7, 5], [1, 2, 9, 2, 8, 6, 7, 2]])
    print('*'* 60)
    decode_pwd('39769107', [[7, 3, 4, 1, 7, 5, 2, 5], [5, 2, 5, 1, 2, 6, 2, 8], [6, 4, 4, 8, 1, 2, 1, 1], [2, 8, 2, 9, 3, 7, 5, 2], [7, 3, 4, 1, 4, 1, 5, 5], [7, 4, 1, 2, 2, 6, 7, 3]])