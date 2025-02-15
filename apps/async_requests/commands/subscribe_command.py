from apps.async_requests.commands.command import Command


class SubscribeCommand(Command):
    def __init__(self, email, first_name, last_name):
        super(SubscribeCommand, self).__init__(True)
        self.contacts = [{"email": email, "first_name": first_name, "last_name": last_name}]

    def merge(self, list_commands):
        for command in list_commands:
            self.contacts.extend(command.contacts)

    def execute(self):
        from apps.async_requests.factory import Factory

        newsletter_service = Factory.get_newsletter_service()
        newsletter_service.add_subscription(self.contacts)

    def __eq__(self, other):
        return super().__eq__(other) and self.contacts == other.contacts
