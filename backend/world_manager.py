# world_manager.py

class WorldManager:
    def __init__(self):
        self.worlds = {}

    def create_world(self, world_name, world_type="normal", seed=None, has_nether=False, game_time=0):
        """
        指定された名前で新しいワールドを作成します。
        """
        if world_name in self.worlds:
            print(f"{world_name} は既に存在します。別の名前を選択してください。")
        else:
            # ワールドの作成ロジック
            print(f"{world_name} を作成しています...")
            self.worlds[world_name] = {"status": "created", "type": world_type, "seed": seed, "has_nether": has_nether, "game_time": game_time}
            print(f"{world_name} を作成しました。")

    def delete_world(self, world_name):
        """
        指定された名前のワールドを削除します。
        """
        if world_name in self.worlds:
            # ワールドの削除ロジック
            print(f"{world_name} を削除しています...")
            del self.worlds[world_name]
            print(f"{world_name} を削除しました。")
        else:
            print(f"{world_name} は存在しません。")

    def list_worlds(self):
        """
        現在存在する全てのワールドをリストします。
        """
        if self.worlds:
            print("存在するワールド:")
            for world_name, info in self.worlds.items():
                has_nether_str = "あり" if info['has_nether'] else "なし"
                print(f"- {world_name}: Type - {info['type']}, Seed - {info['seed']}, ネザー - {has_nether_str}, ゲーム内時間 - {info['game_time']} ticks")
        else:
            print("ワールドは存在しません。")

    def update_world_info(self, world_name, world_type=None, seed=None, has_nether=None, game_time=None):
        """
        指定されたワールドの情報を更新します。
        """
        if world_name in self.worlds:
            if world_type:
                self.worlds[world_name]['type'] = world_type
            if seed:
                self.worlds[world_name]['seed'] = seed
            if has_nether is not None:
                self.worlds[world_name]['has_nether'] = has_nether
            if game_time is not None:
                self.worlds[world_name]['game_time'] = game_time
            print(f"{world_name} の情報を更新しました。")
        else:
            print(f"{world_name} は存在しません。")

# 使用例
if __name__ == "__main__":
    # WorldManager のインスタンス化
    manager = WorldManager()

    # ワールドの作成
    manager.create_world("world1", world_type="normal", seed="12345", has_nether=True, game_time=6000)
    manager.create_world("world2", world_type="flat", seed="98765", has_nether=False, game_time=12000)
    manager.list_worlds()

    # ワールド情報の更新
    manager.update_world_info("world1", world_type="amplified")
    manager.update_world_info("world2", seed="54321", has_nether=True, game_time=18000)
    manager.list_worlds()

    # ワールドの削除
    manager.delete_world("world1")
    manager.list_worlds()
