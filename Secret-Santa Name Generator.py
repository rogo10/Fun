import random
import smtplib
import re


###Final Draft of what worked
###This function will be nested in secret_santa()


###Takes in dictionary of form
###names = {'name':'email', ...}
###Makes sure person A does not get person A
###...except if all that's left is person A from names...this is caught by ValueError

def pick(names):
    pairings = []
    length = len(names)
    givers = dict(names)    ###this and givers are copies. running dicts of who is left after pairing
    givees = dict(names)

    for _ in names:
        
        give = random.choice(list(givers.keys()))    ###reset the giver and receiver
        rec = random.choice(list(givees.keys()))

        while(give == rec):                      ###if giver = receiver then choose new receiver at random
            if(len(givers) == 1):
                raise ValueError('Unsuccessful in picking names. The last person has themself for secret santa. Please try again')
            rec = random.choice(list(givees.keys()))
        
        pairings.append([give, names[give], ' has ', rec, names[rec], 'for secret santa!'])
        givers.pop(give)      ###update running dicts
        givees.pop(rec)

    
    
    return pairings


###Putting it all together
###pick with dictionary of emails
###along with sending the actual emails for all participants

def clean_message(message):
    
    message = message.replace(']','').replace('[','').replace("'","").replace(',',' ')
    
    emails = re.findall(r"[\.\w\d]+@[\w\d]+\.[\w]+",message)
       
    message = message.replace(emails[0],'').replace(emails[1],'').replace('  ',' ')
    
    return message

def secret_santa(names):
    
    pairings = pick(names)    ###call pick2 to make pairing assignments

    mail = smtplib.SMTP(host='smtp.gmail.com',port=587)    ###connect host using port number (gmail)

    mail.ehlo()         ###not necessary but identifies yourself to ESMTP server

    mail.starttls()      ###all smtp commands after will be encrypted
    
    mail.ehlo()         ###not necessary but identifies yourself to ESMTP server
    
    mail.login('your.email@gmail.com','password')    ###log in to email(username, password)
    
    for i in range(len(pairings)):
        giver_email = str(pairings[i][1])      ###takes giver's email from pick2
        text = str(pairings[i])                ###whole message
        text = clean_message(text)
        message = 'Subject: {}\n\n{}'.format('Secret Santa 2020', text)         ###formats email with subject header
        mail.sendmail('your.email@gmail.com', giver_email, message)         ###sends email(from,to,message)
        
    mail.close()   ###closes connection
    
    return 'Emails successfully sent'

names = {'Name 1':"Name 1's email", "Name 2":"Name 2's email"}  ###add people and their emails in dictionary here
secret_santa(names)
