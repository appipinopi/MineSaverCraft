# auth.py

class Authenticator:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        """
        ユーザーを追加します。
        """
        if username in self.users:
            print(f"{username} は既に存在します。別のユーザー名を選択してください。")
        else:
            self.users[username] = password
            print(f"{username} を追加しました。")

    def remove_user(self, username):
        """
        指定されたユーザーを削除します。
        """
        if username in self.users:
            del self.users[username]
            print(f"{username} を削除しました。")
        else:
            print(f"{username} は存在しません。")

    def authenticate(self, username, password):
        """
        ユーザー名とパスワードを認証します。
        """
        if username in self.users and self.users[username] == password:
            print(f"{username} は認証されました。")
            return True
        else:
            print(f"{username} は認証できませんでした。ユーザー名またはパスワードが正しくありません。")
            return False

    def list_users(self):
        """
        現在登録されている全てのユーザーをリストします。
        """
        if self.users:
            print("登録されているユーザー:")
            for username in self.users:
                print(f"- {username}")
        else:
            print("登録されているユーザーはありません。")

# 使用例
if __name__ == "__main__":
    # Authenticator のインスタンス化
    authenticator = Authenticator()

    # ユーザーの追加
    authenticator.add_user("user1", "password1")
    authenticator.add_user("user2", "password2")
    authenticator.list_users()

    # 認証の試行
    authenticator.authenticate("user1", "password1")
    authenticator.authenticate("user1", "wrongpassword")
    authenticator.authenticate("user3", "password3")

    # ユーザーの削除
    authenticator.remove_user("user2")
    authenticator.list_users()
