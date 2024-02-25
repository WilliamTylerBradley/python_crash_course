messages = ['message 1', 'message 2', 'message 3']

def show_messages(messages):
    for message in messages:
        print(message)

sent_messages = []
def send_messages(messages, sent_messages):
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)

send_messages(messages, sent_messages)