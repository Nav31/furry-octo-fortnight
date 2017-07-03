def remove_url_anchor(url):
    url = url.split("#")
    return url[0]

print(remove_url_anchor("http://www.github.com/nav31/repository?page=1"))
print(remove_url_anchor('www.codewars.com#about'))