import requests
from bs4 import BeautifulSoup

# if __name__ == '__main__':
def fetch_the_sw_list(website:str) -> list:
    session = requests.session()
    # url = "http://cnninvmjnkns03.joynext.com:8082/view/MQB/job/SOP2-BM-DEVELOPERS/295/artifact"

    if website.endswith("/"):
        url = website[:-1]
    else:
        url = website
    r = requests.get(url)
    #print(r.status_code)
    # soup = BeautifulSoup(r.text)
    # print(r.text, 'lmxl')
    soup = BeautifulSoup(r.text, 'lxml')
    sw_list = []
    for link in soup.find_all('a'):
        # if not link.get('href').startswith(('?', "/","UpdateContainer","main")):
        link_href = link.get('href')
        if link_href is not None:
            if link_href.startswith(("CNS3",'sha1sum','md5sum'))\
                    and link_href.endswith(("txt", 'tgz')) \
                    and not link_href.endswith(("flashcontainer.tgz", "symbols.tgz")) is True:
                # print(link_href)
                sw_list.append(url + '/' + link_href)
        # if link_href.startswith(("CNS3",'sha1sum','md5sum')) is True:
        # if link_href.startswith(("CNS3", 'sha1sum', 'md5sum')) is True:
        #     print(link_href)
        #     if link_href:

    r.close()
    return sw_list

if __name__ == '__main__':
    print(fetch_the_sw_list("http://cnninvmjnkns03.joynext.com:8082/view/MQB/job/SOP2-BM-DEVELOPERS/295/artifact"))