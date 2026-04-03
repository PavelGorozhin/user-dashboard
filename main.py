import os
import json
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class UserDashboard:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def get_user_info(self):
        return {
            'username': self.username,
            'email': self.email
        }

    def save_user_info(self, user_info):
        with open('user_info.json', 'w') as f:
            json.dump(user_info, f)

    def load_user_info(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return None

    def update_user_info(self, user_info):
        with open('user_info.json', 'w') as f:
            json.dump(user_info, f)

    def delete_user_info(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info = json.load(f)
            del user_info[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass

    def get_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def load_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def update_user_info_list(self, user_info_list):
        with open('user_info.json', 'w') as f:
            json.dump(user_info_list, f)

    def delete_user_info_list(self):
        try:
            with open('user_info.json', 'r') as f:
                user_info_list = json.load(f)
            del user_info_list[self.username]
            with open('user_info.json', 'w') as f:
                json.dump(user_info_list, f)
        except FileNotFoundError:
            pass