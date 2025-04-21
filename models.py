# models.py
class User:
    def __init__(self, id, firstname, lastname, username, email, phone_number, location, role, password):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.phone_number = phone_number
        self.location = location
        self.role = role
        self.password = password


class Topic:
    def __init__(self, id, user_id, title, content, created_at):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.content = content
        self.created_at = created_at


class Comment:
    def __init__(self, id, topic_id, user_id, content, created_at):
        self.id = id
        self.topic_id = topic_id
        self.user_id = user_id
        self.content = content
        self.created_at = created_at


class Message:
    def __init__(self, id, sender_id, receiver_id, content, created_at):
        self.id = id
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.content = content
        self.created_at = created_at
