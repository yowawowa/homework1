# task 1
def domain_name(self, url: str) -> str:
    domain = ""  # creating variable to store domain name (not necessary)
    s = url.split("/")  # splitting url by backslashes  if present
    # check if protocol http or https
    if s[0] == 'https:' or s[0] == 'http:':
        s = s[2].split('.')  # if present domain will be on 3rd place
    else:
        s = s[0].split('.')  # if no protocol specified, domain will be on 1st place
    # check if url contains www by measuring length of url
    if len(s) == 2:  # if no www present, there is only 2 element in list. we need first element
        domain = s[0]
        print(domain)
    else:  # if www is present it will be on first index of list, so we need second element
        domain = s[1]
    return domain

