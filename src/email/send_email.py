'''
Created on Jul 2, 2019

@author: m509575
'''
import smtplib

class SendEmail(object):
    '''
    classdocs
    '''

    gmail_user = 'you@gmail.com'  
    gmail_password = 'P@ssword!'
    
    sent_from = gmail_user  
    to = ['me@gmail.com', 'bill@gmail.com']  
    subject = 'OMG Super Important Message'

    def __init__(self):
        '''
        Constructor
        '''
        gmail_user = '<your_email@gmail.com>'  
        gmail_password = '<your_P@ssword!>'
        
        sent_from = gmail_user  
        to = ['sara23kumar@gmail.com']
        
    def send_email(self,subject,body):
        body = body
        email_text = """\  
        From: %s  
        To: %s  
        Subject: %s
        
        %s
        """ % (self.sent_from, ", ".join(self.to), subject, body)

        try:  
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(self.gmail_user, self.gmail_password)
            server.sendmail(self.sent_from, self.to, email_text)
            server.close()
            print("Email sent successfully about " +subject)
        except Exception as e: 
            print ("Something went wrong..." + e)