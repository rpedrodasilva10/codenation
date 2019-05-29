# tst.py


# vld_site = re.compile(r'[@+[a-zA-Z0-9-]')
# vld_user = re.compile(r'[a-zA-Z0-9_.-]')
# vld_ext  = re.compile(r'\.[a-zA-Z0-9-.]{3}$')

# eml = re.compile(r'(^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$)')
# email = 'lara@@codenation.com'



# site = '@@codenation'
# user = 'lara'
# ext  =  '.com'

# emails = ['matt23@@india.in', 'lara@codenation.com']

# print("User: ",vld_user.fullmatch(user))
# print("Site: ",vld_site.fullmatch(site))
# print("Ext: ", vld_ext.fullmatch(ext))

# print('nada' if eml.fullmatch(email) is None else 'match')

# milhar = re.compile(r'\d{4}$')
# print(milhar.match('123'))

import re
from main import filter_email, valid_email

#lis = [1, 2, 3, 4]



#print(list(filter(lambda x : x % 2 == 0, lis)))

emails = [
            'fjladfk_iasdfad234@sdlkjf23335.in',
            'ha@git@int.cz',
            'prashant24_@gmail.com',
            'mike13445@yahoomail9.server'
        ]

print(filter_email(emails))

