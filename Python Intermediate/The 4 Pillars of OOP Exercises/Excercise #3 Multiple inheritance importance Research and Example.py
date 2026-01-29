# What is multiple inheritance and what is it used for?

# Multiple inheritance occurs when a class inherits from more than one base class.

# ✅ Common uses of multiple inheritance

# 1)Combining behaviors
# When a class needs functionality from different sources.

# 2)Mixins
# Small classes that add a specific capability (logging, validation, permissions).

# 3)Code reuse
# Avoids duplicating common logic.

# 4)Modeling complex entities
# When something “is” multiple things at the same time.

#Example of Code 
class Authentication:
    def login(self, username: str) -> None:
        print(f"User '{username}' logged in successfully.")


class Logger:
    def log_action(self, action: str) -> None:
        print(f"Action logged: {action}")


class AdminUser(Authentication, Logger):
    def __init__(self, username: str):
        self.username = username

    def delete_user(self, user_to_delete: str) -> None:
        self.log_action(f"Admin {self.username} deleted user {user_to_delete}")
        print(f"User '{user_to_delete}' has been deleted.")

# Example of Code Used 
def main() -> None:
    admin = AdminUser("leo_admin")

    admin.login("leo_admin")
    admin.delete_user("test_user")


if __name__ == "__main__":
    main()

# Summary of Research 
# Multiple Inheritance

# Multiple inheritance allows a class to inherit behaviors from more than one base class. 
# It is commonly used to combine independent functionalities, such as authentication, logging, or validations, into a single class without duplicating code. 
# In Python, multiple inheritance can be used safely and effectively when it is properly designed, thanks to the Method Resolution Order (MRO), which defines a clear and predictable order for method lookup and helps prevent ambiguity.
