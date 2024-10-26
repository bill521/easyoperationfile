from datetime import datetime
import os
import re
import shutil
import json

from collections import Counter
from pathlib import Path

import pandas as pd
from jsonschema.exceptions import ValidationError
from jsonschema.validators import validate
from json_repair import repair_json, json_repair

from Output_cls_JSON import Output_cls_JSON_List, Output_cls_JSON
from ai.call_model import ChatConfig, call_model


class ExcelUtilsClass:

    def __init__(self):
        self.work_space_path = None
        self.file_path = None
        self.move_path = None
        self.api_key = None
        self.prompt_template = None
        # 是否读取文件夹中内容写入到EXCEL True：是 False：否
        self.is_open_read_file_output_excel = None
        # 设置是否读取子目录 True：是 False：否
        self.include_subdirectories = None
        # 是否启用AI解析文件名 True：是 False：否
        self.is_open_ai_parse = None
        # 是否提取歌曲名 True：提取 False：不提取
        self.is_extract_name = None
        # 是否检查歌曲名是否重复 True：检查 False：不检查
        self.is_check_duplicates = None
        # 是否开启文件移动 True：移动 False：不移动
        self.is_open_move_file = None
        # 是否开启文件复制 True：复制 False：不复制
        self.is_open_copy_file = None
        # 是否开启根据标签复制文件 True：复制 False：不复制
        self.is_open_lable_copy_file = None
        # 标签
        self.lable_name = None
        # 是否开启文件重命名 True：是 False：否
        self.is_open_rename_file = None
        # 临时变量集合
        self.elements = []
        # 筛选的文件后缀名
        self.extension = None
        # 窗口程序对象
        self.ui_main_window = None
        # 开启文件整合
        self.is_open_repair_merge_json_files = None

        self.excel_filed_01 = "文件路径"
        self.excel_filed_02 = "文件全名"
        self.excel_filed_03 = "文件名"
        self.excel_filed_04 = "提取结果"
        self.excel_filed_05 = "序号"
        self.excel_filed_06 = "提取结果"
        self.excel_filed_07 = "文件后缀"

        self.excel_filed_08 = "文件后缀"
        self.excel_filed_09 = "文件后缀"
        self.excel_filed_10 = "文件后缀"
        self.excel_filed_11 = "文件后缀"

        self.extensions = ".json"
        self.regex_pattern = r"^gpt_content_batch_.*\.json$"

    def setConfig(self, config, ui_main_window):
        self.work_space_path = Path(config.work_space_path)
        self.file_path = Path(config.work_space_path) / config.output_file
        self.move_path = Path(config.save_path_dir) / config.move_path

        self.api_key = config.api_key
        self.prompt_template = config.prompt_template
        # 是否读取文件夹中内容写入到EXCEL True：是 False：否
        self.is_open_read_file_output_excel = config.is_open_read_file_output_excel
        # 设置是否读取子目录 True：是 False：否
        self.include_subdirectories = config.include_subdirectories
        # 是否启用AI解析文件名 True：是 False：否
        self.is_open_ai_parse = config.is_open_ai_parse

        self.is_open_ai_parse_one_stage = config.is_open_ai_parse_one_stage
        # 是否提取歌曲名 True：提取 False：不提取
        self.is_extract_name = config.is_extract_name
        # 是否检查歌曲名是否重复 True：检查 False：不检查
        self.is_check_duplicates = config.is_check_duplicates
        # 是否开启文件移动 True：移动 False：不移动
        self.is_open_move_file = config.is_open_move_file
        # 是否开启文件复制 True：复制 False：不复制
        self.is_open_copy_file = config.is_open_copy_file
        # 是否开启根据标签复制文件 True：复制 False：不复制
        self.is_open_lable_copy_file = config.is_open_lable_copy_file
        # 标签
        self.lable_name = config.lable_name
        # 是否开启文件重命名 True：是 False：否
        self.is_open_rename_file = config.is_open_rename_file
        # 临时变量集合
        self.elements = []
        # 筛选的文件后缀名
        self.extension = config.extension
        # 窗口程序对象
        self.ui_main_window = ui_main_window
        # 开启文件整合
        self.is_open_repair_merge_json_files = config.is_open_repair_merge_json_files
        # 将json结果写入excel
        self.is_open_update_json_to_excel = config.is_open_update_json_to_excel
        # 模型列表
        self.model_list = config.model_list
        # 是否开启根据新名称复制
        self.is_open_copy_lable_new_name = config.is_open_copy_lable_new_name

    def console(self):

        if self.is_open_read_file_output_excel:
            folder_path = self.work_space_path
            extension_list = self.extension.split(',')
            output_excel = self.file_path
            self.write_to_excel(folder_path, extension_list, output_excel, self.include_subdirectories)
            self.ui_main_window.add_info_log(f"生成EXCEL结束")

        if self.is_open_ai_parse:

            if self.is_open_ai_parse_one_stage:
                # ai解析
                self.read_excel_in_batches_and_ai_parse(self.file_path, batch_size=10)

            if self.is_open_repair_merge_json_files:
                # 修复后的json文件
                self.repair_json_files()
                self.ui_main_window.add_info_log(f"修复JSON结束")

            if self.is_open_update_json_to_excel:
                # 将json结果写入excel
                if self.is_excel_file_open(self.file_path):
                    return False
                data = pd.read_excel(self.file_path)
                self.extract_content_to_excel(data)
                self.extract_song_names(data)
                data.to_excel(self.file_path, index=False)
                # 清除已生成的文件
                files = self.list_files(self.work_space_path, self.extensions, include_subdirectories=False,
                                        regex_pattern=self.regex_pattern)

                self.delete_files(files)

                self.ui_main_window.add_info_log(f"将json结果写入excel结束")
            self.ui_main_window.add_info_log(f"AI解析结束")

        if self.is_open_copy_file:
            if self.is_excel_file_open(self.file_path):
                return False
            data = pd.read_excel(self.file_path)
            # # 检查文件夹是否存在
            self.check_and_create_directory(self.move_path)
            # 复制文件
            for index, row in data.iterrows():
                if pd.notna(row[self.excel_filed_04]):
                    source_file = Path(row[self.excel_filed_01]) / row[self.excel_filed_02]
                    destination_file = self.move_path / row[self.excel_filed_02]
                    self.copy_file(source_file, destination_file)
            self.ui_main_window.add_info_log(f"复制文件结束")

        if self.is_open_rename_file:
            data = pd.read_excel(self.file_path)
            # 重命名
            for index, row in data.iterrows():
                if pd.notna(row[self.excel_filed_04]):
                    original_file = self.move_path / row[self.excel_filed_02]
                    new_name = f"{row[self.excel_filed_05]}_{row[self.excel_filed_06]}{row[self.excel_filed_07]}"
                    self.rename_file(original_file, new_name)
            self.ui_main_window.add_info_log(f"重命名文件结束")

        if self.is_check_duplicates:
            elements = []
            data = pd.read_excel(self.file_path)
            # 提取最新歌曲名称存入集合
            for index, row in data.iterrows():
                name = row["AI解析结果"]
                elements.append(name)

            # 判重
            for index, row in data.iterrows():
                row_index_to_modify = index
                duplicates = row["AI解析结果"]
                duplicates_result = self.check_duplicates(elements, duplicates)
                data.at[row_index_to_modify, '是否重复'] = duplicates_result["is_duplicates"]
                data.at[row_index_to_modify, '重复次数'] = duplicates_result["duplicates_num"]

            try:
                # 将修改后的数据写入新的 Excel 文件
                data.to_excel(self.file_path, index=False)
                #self.ui_main_window.add_info_log(f"标记重复数据结束")
            except Exception as e:
                self.ui_main_window.add_error_log(f"标记重复数据异常： {e}")

        if self.is_open_lable_copy_file:
            data = pd.read_excel(self.file_path)
            destination_file = self.move_path.joinpath("lable")
            # # 检查文件夹是否存在
            self.check_and_create_directory(destination_file)
            # 复制文件
            for index, row in data.iterrows():
                if row["标签"] == self.lable_name:
                    if self.is_open_copy_lable_new_name:
                        file_name = f"{row[self.excel_filed_05]}_{row[self.excel_filed_06]}{row[self.excel_filed_07]}"
                        source_file = self.move_path / file_name
                        destination = destination_file / file_name
                        self.copy_file(source_file, destination)
                    else:
                        source_file = Path(row[self.excel_filed_01]) / row[self.excel_filed_02]
                        destination_file = self.move_path / row[self.excel_filed_02]
                        self.copy_file(source_file, destination_file)
            self.ui_main_window.add_info_log(f"根据标签复制结束")

    def extract_content_to_excel(self, data):
        content_list = self.read_json_files()
        content_dict = dict(zip([obj["old"] for obj in content_list], content_list))
        # 填充字段 AI解析结果，提取结果
        for index, row in data.iterrows():
            row_index_to_modify = index
            key_to_check = row[self.excel_filed_03]
            if key_to_check in content_dict:
                obj = content_dict.get(key_to_check)
                data.at[row_index_to_modify, self.excel_filed_04] = obj["new"]

        # data.to_excel(self.file_path, index=False)

    def extract_song_names(self, data):
        """
        从 DataFrame 中提取歌曲名称并更新 'AI解析结果' 列。
         :param data: 包含歌曲信息的 DataFrame
        :return: 更新后的 DataFrame
        """
        for index, row in data.iterrows():
            row_index_to_modify = index
            column_value = row[self.excel_filed_04]
            if pd.notna(column_value):
                split_values = column_value.split('-')
                # 检查是否有第三个部分
                if len(split_values) >= 3:
                    third_part = split_values[2]  # 获取第三个部分
                else:
                    third_part = column_value
                data.at[row_index_to_modify, 'AI解析结果'] = third_part

    def read_excel_in_batches_and_ai_parse(self, file_path, batch_size=10):
        """
        分页读取 Excel 文件中的内容。
         :param file_path: Excel 文件路径
        :param batch_size: 每次读取的条数
        """
        if self.is_excel_file_open(file_path):
            return False

        # 读取 Excel 文件
        data = pd.read_excel(file_path)
        # 筛选出 'result_field' 字段为空的结果
        filtered_data = data[data['状态'].isnull() | (data['状态'] == "解析异常") | (data['提取结果'].isnull())]
        # # 获取总行数
        total_rows = len(filtered_data)
        # 时间戳
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # 格式化为 YYYYMMDD_HHMMSS
        # 分页读取数据
        for start in range(0, total_rows, batch_size):
            doc = ""
            end = min(start + batch_size, total_rows)
            batch_data = filtered_data.iloc[start:end]
            json_schema = Output_cls_JSON_List.model_json_schema()
            json_schema_str = json.dumps(json_schema, ensure_ascii=False, indent=2)
            self.prompt_template = self.prompt_template.replace('{json_schema}', json_schema_str)
            for index, row in batch_data.iterrows():
                name = row[self.excel_filed_03] + ""
                doc += name + "\n"
            formatted_prompt = self.prompt_template.replace('{doc}', doc)

            print(f"解析提示词：\n {formatted_prompt}")

            try:

                # 循环遍历 model_list
                for model in self.model_list:
                    model.prompt = formatted_prompt
                    ai_parse = self.sample_call_streaming(model)

                # 更新DataFrame中的状态字段
                update_indices = filtered_data.index[start:end].tolist()
                data.loc[update_indices, '状态'] = '已解析'
                self.ui_main_window.add_info_log(f"当前解析成功行数： {start + 1}_{end}")
                file_path_v1 = self.work_space_path / f"gpt_content_batch_{start + 1}_{end}_{timestamp}.json"
                self.write_to_file_v1(file_path_v1, ai_parse)
            except Exception as e:
                # 更新DataFrame中的状态字段
                update_indices = filtered_data.index[start:end].tolist()
                data.loc[update_indices, '状态'] = '解析异常'
                self.ui_main_window.add_error_log(f"当前解析行数： {start + 1}_{end}：{e}")

        # 保存更新后的数据回到Excel文件
        data.to_excel(file_path, index=False)

    def is_excel_file_open(self, file_path):
        """检查 Excel 文件是否被打开"""
        try:
            # 尝试以写入模式打开文件
            with open(file_path, 'a'):
                pass
            return False  # 文件没有被打开
        except PermissionError:
            self.ui_main_window.add_error_log(f"文件被打开无法继续操作，请先关闭")
            return True  # 文件被其他程序打开
        except OSError as e:
            self.ui_main_window.add_error_log(f"发生错误: {e}")
            return False  # 处理其他错误

    def validate_data(self, instance, schema):
        try:
            validate(instance=instance, schema=schema)
            return True
        except ValidationError as e:
            return False

    def repair_json_files(self):
        """
        读取指定文件夹下的所有 .json 文件并整合成一个文件。
        """
        all_obj = {}
        content_list = []
        content_list_error = []
        content_list_error_file = []
        content_list_paths = []
        folder_path = self.work_space_path
        files = self.list_files(folder_path, self.extensions, include_subdirectories=False, regex_pattern=self.regex_pattern)

        for index, file in enumerate(files):
            print(f"正在读取文件内容：{file} 合并到主集合")
            with open(file, 'r', encoding='utf-8') as f:
                # 读取文件内容
                bad_json_string = f.read()
                # 修复json
                good_json_string = repair_json(bad_json_string, ensure_ascii=False)
                json_data = json_repair.loads(good_json_string)
                file_path = self.work_space_path / f"{os.path.basename(file)}"
                self.write_to_file(file_path, json_data)
                content_list_paths.append(file)

        for index, path in enumerate(content_list_paths):
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                schema_1 = Output_cls_JSON_List.model_json_schema()
                json_data = json.loads(content)
                schema = Output_cls_JSON.model_json_schema()
                if self.validate_data(json_data, schema_1):
                    # 校验json_data 正确的进入，错误的过滤掉
                    for item in json_data["list"]:
                        if self.validate_data(item, schema):
                            content_list.append(item)
                        else:
                            content_list_error.append(item)
                else:
                    content_list_error_file.append(path)

        # 增加序号
        for index, item in enumerate(content_list):
            item["sort"] = index + 1

        for index, item in enumerate(content_list_error):
            item["sort"] = index + 1

        all_obj["list"] = content_list
        all_obj["error_list"] = content_list_error
        all_obj["error_file_list"] = content_list_error_file
        self.write_to_file(self.work_space_path / f"gpt_content_batch_all.json", all_obj)

    def delete_files(self, file_set):
        for file_path in file_set:
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    self.ui_main_window.add_error_log(f"已删除文件: {file_path}")
                else:
                    self.ui_main_window.add_error_log(f"文件不存在: {file_path}")
            except Exception as e:
                self.ui_main_window.add_error_log(f"删除文件时发生错误: {file_path} - 错误信息: {e}")

    def read_json_files(self):
        """
        读取指定文件夹下的所有 .json 文件并整合成一个文件。
        """
        # 打开文件并读取内容
        file_path = self.work_space_path / f"gpt_content_batch_all.json"
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # 将内容转换为 JSON 对象
            json_data = json.loads(content)
            return json_data["list"]

    def write_to_file_v1(self, file_path, content):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(content)

    def write_to_file(self, file_path, content):
        with open(file_path, 'w', encoding='utf-8') as file:
            # 将内容写入文件
            json.dump(content, file, ensure_ascii=False, indent=4)

    def sample_call_streaming(self, chatConfig):
        return call_model(chatConfig)

    def list_files(self, folder_path, extensions=None, include_subdirectories=False, regex_pattern=None):
        """
        查询指定文件夹下指定后缀名的文件
        :param folder_path: 要查找的文件夹路径
        :param extensions: 文件后缀名列表（例如 ['.txt', '.csv']），默认是 None 表示全扫描
        :param include_subdirectories: 是否读取子目录
        :param regex_pattern: 正则表达式，用于匹配文件名，默认是 None 表示不使用正则匹配
        """
        files = []
        # 编译正则表达式
        regex = re.compile(regex_pattern) if regex_pattern else None
        # 遍历文件
        if include_subdirectories:
            # 遍历子目录
            for root, dirs, filenames in os.walk(folder_path):
                for filename in filenames:
                    if (extensions is None or any(filename.endswith(ext) for ext in extensions)) and \
                            (regex is None or regex.search(filename)):
                        full_path = os.path.join(root, filename)
                        files.append(full_path)
        else:
            # 仅遍历当前目录
            for filename in os.listdir(folder_path):
                if (extensions is None or any(filename.endswith(ext) for ext in extensions)) and \
                        (regex is None or regex.search(filename)):
                    full_path = os.path.join(folder_path, filename)
                    files.append(full_path)
        return files

    def get_subpath(self, root_path, full_path):
        # 确保根路径和完整路径都是绝对路径
        root_path = os.path.abspath(root_path)
        full_path = os.path.abspath(full_path)
        # 检查根路径是否是完整路径的前缀
        if full_path.startswith(root_path):
            # 获取子路径
            sub_path = os.path.relpath(full_path, root_path)
            return sub_path
        else:
            raise ValueError("The full path does not start with the root path.")

    def write_to_excel(self, folder_path, extensions=None, output_excel='output.xlsx', include_subdirectories=False):
        """
        列出指定文件夹下指定后缀名的文件，并将文件名及相关信息写入到 Excel 中。
        :param folder_path: 要查找的文件夹路径
        :param extensions: 文件后缀名列表（例如 ['.txt', '.csv']），默认是 None 表示全扫描
        :param output_excel: 输出的 Excel 文件路径
        :param include_subdirectories: 是否读取子目录
        """
        files = self.list_files(folder_path, extensions, include_subdirectories)
        # 提取文件信息
        file_data = []
        for file in files:
            file_name = os.path.basename(file)  # 文件名
            file_path = os.path.dirname(file)  # 文件路径
            subdirectory = self.get_subpath(self.work_space_path, file_path)  # 获取子目录名
            file_extension = os.path.splitext(file_name)[1]  # 文件后缀
            file_name_extension = os.path.splitext(file_name)[0]  # 去后缀的文件名
            file_data.append((file_path, subdirectory, file_name, file_name_extension, file_extension))

        # 计算重复次数
        # file_names = [name for _, _, name, _, _ in file_data]

        # 创建 DataFrame
        df = pd.DataFrame(file_data, columns=[self.excel_filed_01, "子目录", self.excel_filed_02, self.excel_filed_03, self.excel_filed_07])
        df['序号'] = df.index + 1  # 添加序号
        df['AI解析结果'] = None
        df['提取结果'] = None
        df['是否重复'] = None
        df['重复次数'] = None
        df['标签'] = None
        df['状态'] = None
        # 将 DataFrame 写入到 Excel 文件
        try:
            df.to_excel(output_excel, index=False)
        except Exception as e:
            self.ui_main_window.add_error_log(f"{e}")
            return
        self.ui_main_window.add_info_log(f"文件信息已成功写入到 '{output_excel}'。")

    def rename_file(self, original_file_path, new_file_name):
        """
        重命名文件
        :param original_file_path: 原文件路径
        :param new_file_name: 新文件名（不包括路径）
        """
        try:
            # 获取原文件的目录
            directory = os.path.dirname(original_file_path)
            # 构建新文件的完整路径
            new_file_path = os.path.join(directory, new_file_name)
            # 重命名文件
            os.rename(original_file_path, new_file_path)
            self.ui_main_window.add_info_log(f"文件 '{original_file_path}' 已成功重命名为 '{new_file_path}'。")
        except FileNotFoundError:
            self.ui_main_window.add_error_log(f"文件 '{original_file_path}' 不存在。")

    def copy_file(self, source_file, destination_file):
        """
        复制文件从源路径到目标路径。
        :param source_file: 源文件路径
        :param destination_file: 目标文件路径
        """
        try:
            shutil.copy(source_file, destination_file)
            self.ui_main_window.add_info_log(f"文件 '{source_file}' 已成功复制到 '{destination_file}'。")
        except FileNotFoundError as f:
            print(f"文件 '{source_file}' 不存在。{f}")
            self.ui_main_window.add_error_log(f"文件 '{source_file}' 不存在。")
        except Exception as e:
            self.ui_main_window.add_error_log(f"复制文件时发生错误: {e}")

    def move_file(self, source_file, destination_file):
        """
        移动文件从源路径到目标路径。
        :param source_file: 源文件路径
        :param destination_file: 目标文件路径
        """
        try:
            shutil.move(source_file, destination_file)  # 移动文件
            print(f"文件 '{source_file}' 已成功移动到 '{destination_file}'。")
        except FileNotFoundError:
            print(f"文件 '{source_file}' 不存在。")
        except Exception as e:
            print(f"移动文件时发生错误: {e}")

    def check_and_create_directory(self, directory_path):
        """
        检查文件夹是否存在，如果不存在则创建它。
         :param directory_path: 要检查或创建的文件夹路径
        """
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)  # 创建文件夹

    def check_duplicates(self, elements, target):
        result = {"is_duplicates": "","duplicates_num":""}
        element_counts = Counter(elements)
        count = element_counts[target]
        if count > 1:
            self.ui_main_window.add_info_log(f"元素 '{target}' 重复了 {count} 次。")
            result["is_duplicates"] = 1
            result["duplicates_num"] = count
        elif count == 1:
            self.ui_main_window.add_info_log(f"元素 '{target}' 未重复。")
            result["is_duplicates"] = 0
            result["duplicates_num"] = count
        return result

