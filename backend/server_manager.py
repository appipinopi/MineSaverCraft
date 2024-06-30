import subprocess
import os
import shutil

class ServerManager:
    def __init__(self, server_directory):
        self.server_directory = server_directory
        self.current_process = None

    def start_server(self, server_jar, server_args=[]):
        """
        指定されたサーバーJARファイルでMinecraftサーバーを起動します。
        """
        if self.current_process and self.current_process.poll() is None:
            print("サーバーは既に起動しています。")
            return

        server_path = os.path.join(self.server_directory, server_jar)
        command = ["java", "-jar", server_path] + server_args

        print(f"サーバーを起動しています... コマンド: {' '.join(command)}")
        self.current_process = subprocess.Popen(command, cwd=self.server_directory)

    def stop_server(self):
        """
        現在実行中のMinecraftサーバーを停止します。
        """
        if self.current_process and self.current_process.poll() is None:
            print("サーバーを停止しています...")
            self.current_process.terminate()
            self.current_process.wait()
            print("サーバーを停止しました。")
        else:
            print("サーバーは実行されていません。")

    def check_server_status(self):
        """
        現在のサーバーの実行状態を確認します。
        """
        if self.current_process and self.current_process.poll() is None:
            print("サーバーは実行中です。")
        else:
            print("サーバーは停止しています。")

    def add_plugin(self, plugin_file):
        """
        指定されたプラグインファイル（.jar）をサーバーに追加します。
        """
        plugin_path = os.path.abspath(plugin_file)
        if not os.path.exists(plugin_path):
            print(f"{plugin_file} が見つかりません。")
            return

        plugin_name = os.path.basename(plugin_path)
        plugin_dest = os.path.join(self.server_directory, "plugins", plugin_name)

        try:
            shutil.copyfile(plugin_path, plugin_dest)
            print(f"{plugin_name} をサーバーに追加しました。")
        except Exception as e:
            print(f"プラグインの追加中にエラーが発生しました: {e}")
