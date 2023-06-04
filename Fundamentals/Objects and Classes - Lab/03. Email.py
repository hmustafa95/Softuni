class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True
        return self.is_sent

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []

while True:
    command = input()
    if command == 'Stop':
        break
    sender, receiver, content = command.split(' ')
    email = Email(sender, receiver, content)
    emails.append(email)

send_emails = list(map(lambda x: int(x), input().split(', ')))

for x in send_emails:
    emails[x].send()

for email in emails:
    print(email.get_info())
