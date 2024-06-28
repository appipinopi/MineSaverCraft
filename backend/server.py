# server.py

class ServerManager:
    def __init__(self):
        self.servers = {}

    def start_server(self, server_name):
        """
        指定された名前のサーバーを起動します。
        """
        if server_name in self.servers:
            print(f"{server_name} は既に稼働しています。")
        else:
            # サーバーを起動するロジック
            print(f"{server_name} を起動しています...")
            self.servers[server_name] = "稼働中"
            print(f"{server_name} を起動しました。")

    def stop_server(self, server_name):
        """
        指定された名前のサーバーを停止します。
        """
        if server_name in self.servers:
            # サーバーを停止するロジック
            print(f"{server_name} を停止しています...")
            del self.servers[server_name]
            print(f"{server_name} を停止しました。")
        else:
            print(f"{server_name} は稼働していません。")

    def list_servers(self):
        """
        現在稼働中の全てのサーバーをリストします。
        """
        if self.servers:
            print("稼働中のサーバー:")
            for server_name in self.servers:
                print(f"- {server_name}")
        else:
            print("稼働中のサーバーはありません。")

# 使用例
if __name__ == "__main__":
    # ServerManager のインスタンス化
    manager = ServerManager()

    # "MyServer" という名前のサーバーを起動
    manager.start_server("MyServer")

    # 稼働中の全てのサーバーをリストする
    manager.list_servers()

    # "MyServer" という名前のサーバーを停止する
    manager.stop_server("MyServer")

    # 稼働中の全てのサーバーを再度リストする
    manager.list_servers()
