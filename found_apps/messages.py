def sending_message(unsent_messages, sent_messages):
    while unsent_messages: 
        current_message = unsent_messages.pop()
        sent_messages.append(current_message)

def show_sent_messages(sent_messages):
    print("The following messages have been sent:")
    for sent_message in sent_messages:
        print(sent_message)

def show_archive_messages(archived_messages):
    print("\nThese messages have been archived: ")
    for archived_message in archived_messages:
        print(archived_message)


unsent_messages = ["Hi guys I'm ready to go home.", 'Who are we drafting today?', "What's the plan for this weekend?"]
sent_messages = []

sending_message(unsent_messages[:], sent_messages)
show_sent_messages(sent_messages)
show_archive_messages(unsent_messages)
