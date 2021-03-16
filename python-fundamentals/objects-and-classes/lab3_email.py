class Email:
    def __init__(self, sender, receiver, content, is_sent = False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True
    
    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent {self.is_sent}'


class MailBox:
    def __init__(self):
        self.emails = []

    def add_email(self, email):
        self.emails.append(email)

    def send_emails(self, indices):
        for email_index in indices:
            self.emails[email_index].send() 

    def print_mailbox(self):
        for email in self.emails:
            print(email.get_info())


mailbox = MailBox()

# read emails
while True:
    input_email = input()
    if input_email == 'Stop':
            break
    
    sender, receiver, content = input_email.split(' ', maxsplit = 2)

    email = Email(sender, receiver, content)

    mailbox.add_email(email)


# get the indices of the emails to send
emails_to_send = list(map(int, input().split(', ')))

# mark emails as sent
mailbox.send_emails(emails_to_send)

# print the mail box
mailbox.print_mailbox()