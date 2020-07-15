import re

def domain_name(url):
    reserved_words = {'www', 'http', 'https'}
    pattern = re.compile("[^A-Za-z\-0-9]")
    return [e for e in re.split(pattern,url) if e and e not in reserved_words].pop(0)



def test_domain_name():
    assert domain_name("http://google.com") ==  "google"
    assert domain_name("http://google.co.jp") ==  "google"
    assert domain_name("www.xakep.ru") ==  "xakep"
    assert domain_name("https://youtube.com") ==  "youtube"