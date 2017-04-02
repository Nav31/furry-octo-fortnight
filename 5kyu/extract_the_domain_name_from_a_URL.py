import re
def domain_name(url):
    url = re.split(r"https?:\/\/(www\.)?|(www.)", url)[-1:]
    url = re.split(r"\.", url[0])[0]
    return url

# Best
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]