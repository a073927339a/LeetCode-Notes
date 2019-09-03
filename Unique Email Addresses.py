class Solution(object):
    def numUniqueEmails(self, emails):
        lists = []
        mail = ''
        for i in emails:
            name, domain = i.split('@')
            name = name.split('+')[0]
            name = name.replace('.','')
            mail = name+'@'+domain
            if mail not in lists:
                lists.append(mail)
                mail = ''
            else:
                mail = ''
        return len(lists)
            
        