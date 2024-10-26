import json
import os


def save_cache(content, file_name="config.json"):
    # 获取当前用户的主目录
    home_directory = os.path.expanduser("~")

    # 构建 .cache 目录的路径
    cache_directory = os.path.join(home_directory, '.cache')

    cache_directory = os.path.join(cache_directory, 'ding')

    # 如果 .cache 目录不存在，则创建它
    os.makedirs(cache_directory, exist_ok=True)

    # 构建完整的文件路径
    file_path = os.path.join(cache_directory, file_name)

    # 使用'w'模式打开文件，如果文件不存在，将创建一个新文件
    with open(file_path, 'w', encoding='utf-8') as file:
        # 将内容写入文件
        file.write(content)


def load_cache(file_name: object = "config.json") -> object:
    """加载缓存文件，如果文件存在则返回内容，否则返回 None
    :rtype: object
    """
    # 获取当前用户的主目录
    home_directory = os.path.expanduser("~")
    # 构建 .cache 目录的路径
    cache_directory = os.path.join(home_directory, '.cache')
    cache_directory = os.path.join(cache_directory, 'ding')
    # 构建完整的文件路径
    file_path = os.path.join(cache_directory, file_name)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as cache_file:
            return json.load(cache_file)
        
    return None