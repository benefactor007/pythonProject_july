from bs4 import BeautifulSoup
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import base64


def fetch_the_sw_list(website:str) -> list:
    session = requests.session()
    # ignore SSL warning
    requests.packages.urllib3.disable_warnings()

    # url = "https://cnninvmsvn01.joynext.com/CNS3.0_GP/60_ReleaseLibrary/02_External/02_SW/06_SwIntegration/C078-RC7_15inch/01%20CarImage/"
    url = website
    if url.endswith(".tgz") is True:
        url = url[:url.rindex('/')]

    def get_auth(user_name, user_passwd):
        return str(base64.b64encode((user_name + ":" + user_passwd).encode('utf-8')), encoding='utf-8')

    dic_headers = {
        # "Authorization":"Basic d3Vfajc6VGlhbnl1YW49PXh1dQ==",
        "Authorization": "Basic {}".format(get_auth("wu_j7", "Tianyuan==xuu")),
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0"
    }
    r = requests.get(url, verify=False, headers=dic_headers)
    # print(r.status_code)
    # print(r.text)
    soup = BeautifulSoup(r.text, 'lxml')
    sw_list = []
    for link in soup.find_all('a'):
        # if not link.get('href').startswith(('?', "/","UpdateContainer","main")):
        link_href = link.get('href')
        # if link_href.startswith(("CNS3",'sha1sum','md5sum')) is True:
        if link_href.startswith(("VW_CHN", 'sha1sum', 'md5sum')) is True:
            print(link_href)
            if link_href:
                sw_list.append(url + '/' + link_href)
    print(sw_list)
    r.close()
    return sw_list

if __name__ == '__main__':
    print("please remove the '#'")
    # session = requests.session()
    # # ignore SSL warning
    # requests.packages.urllib3.disable_warnings()
    #
    # url = "https://cnninvmsvn01.joynext.com/CNS3.0_GP/60_ReleaseLibrary/02_External/02_SW/06_SwIntegration/C078-RC7_15inch/01%20CarImage/"
    #
    # def get_auth(user_name, user_passwd):
    #     return str(base64.b64encode((user_name + ":" + user_passwd).encode('utf-8')), encoding='utf-8')
    #
    #
    # dic_headers = {
    #     # "Authorization":"Basic d3Vfajc6VGlhbnl1YW49PXh1dQ==",
    #     "Authorization" : "Basic {}".format(get_auth("wu_j7", "Tianyuan==xuu")),
    #     "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0"
    # }
    # r = requests.get(url, verify = False, headers =  dic_headers)
    # # print(r.status_code)
    # # print(r.text)
    # soup = BeautifulSoup(r.text, 'lxml')
    # sw_list = []
    # for link in soup.find_all('a'):
    #     # if not link.get('href').startswith(('?', "/","UpdateContainer","main")):
    #     link_href = link.get('href')
    #     # if link_href.startswith(("CNS3",'sha1sum','md5sum')) is True:
    #     if link_href.startswith(("VW_CHN", 'sha1sum', 'md5sum')) is True:
    #         print(link_href)
    #         if link_href:
    #             sw_list.append(url + '/' + link_href)
    # print(sw_list)
    # r.close()
