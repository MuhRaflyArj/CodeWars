def domain_name(url):
    url = url.split("//")[-1].split("www.")[-1].split(".")[0]
    return url

print(domain_name("https://youtube.com")) # youtube
print(domain_name("www.xakep.ru.co")) # xacep
