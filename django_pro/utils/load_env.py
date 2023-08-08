import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv, dotenv_values

# 加载.env文件中的环境变量
load_dotenv()


# 使用os.getenv获取环境变量的值
def get_env(key: str) -> str:
    return os.getenv(key=key)


def get_many_env(keys: list) -> list:
    return [get_env(key=k) for k in keys]


def load_values() -> dict:
    config = dotenv_values()
    return config


def find_env():
    return find_dotenv('.env')


if not find_env():
    env_path = Path(__file__).parent.parent.parent
    raise EnvironmentError(f"缺少.env文件，请手动创建. 创建路径：{env_path / '.env'}")


if __name__ == '__main__':
    print(get_many_env(["DB_USER", "DB_PWD", "DB_NAME"]))
    print(load_values().get("DB_USER"))
    print(find_env())