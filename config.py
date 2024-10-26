import json

from ai.call_model import ChatConfig


class Config:
    def __init__(self,
                 work_space_path,
                 output_file,
                 move_path_str,
                 api_key,
                 prompt_template,
                 extension,
                 save_path_dir,
                 is_open_read_file_output_excel=False,
                 include_subdirectories=False,
                 is_open_ai_parse=False,
                 is_open_ai_parse_one_stage=False,
                 is_open_starfire=True,
                 starfire_app_id=None,
                 starfire_api_key=None,
                 starfire_api_secret=None,
                 starfire_model_name=None,
                 is_open_ty=False,
                 ty_api=None,
                 ty_model_name=None,
                 is_extract_name=False,
                 is_check_duplicates=False,
                 is_open_move_file=False,
                 is_open_copy_file=False,
                 is_open_lable_copy_file=False,
                 lable_name=None,
                 is_open_rename_file=False,
                 is_open_repair_merge_json_files=False,
                 is_open_update_json_to_excel=False,
                 is_open_copy_lable_new_name=True):

        self.work_space_path = work_space_path
        self.output_file = output_file

        # 保存目录
        self.save_path_dir = save_path_dir
        self.move_path = move_path_str

        self.api_key = api_key
        self.prompt_template = prompt_template
        self.is_open_read_file_output_excel = is_open_read_file_output_excel == 2 if True else False
        # 设置是否读取子目录 True：是 False：否
        self.include_subdirectories = include_subdirectories == 2 if True else False

        # 是否提取歌曲名 True：提取 False：不提取
        self.is_extract_name = is_extract_name == 2 if True else False
        # 是否检查歌曲名是否重复 True：检查 False：不检查
        self.is_check_duplicates = is_check_duplicates == 2 if True else False
        # 是否开启文件移动 True：移动 False：不移动
        self.is_open_move_file = is_open_move_file == 2 if True else False
        # 是否开启文件复制 True：复制 False：不复制
        self.is_open_copy_file = is_open_copy_file == 2 if True else False
        # 是否开启根据标签复制文件 True：复制 False：不复制
        self.is_open_lable_copy_file = is_open_lable_copy_file == 2 if True else False
        # 标签
        self.lable_name = lable_name
        # 是否开启文件重命名 True：是 False：否
        self.is_open_rename_file = is_open_rename_file == 2 if True else False
        # 筛选的文件后缀名
        self.extension = extension


        # 是否启用AI解析文件名 True：是 False：否
        self.is_open_ai_parse = is_open_ai_parse == 2 if True else False
        # AI解析源文件
        self.is_open_ai_parse_one_stage = is_open_ai_parse_one_stage == 2 if True else False
        # 修复JSON 开启文件整合
        self.is_open_repair_merge_json_files = is_open_repair_merge_json_files == 2 if True else False
        # 将json结果写入excel
        self.is_open_update_json_to_excel = is_open_update_json_to_excel == 2 if True else False

        # 星火模型是否开启
        self.is_open_starfire = is_open_starfire
        # 星火模型APP_ID
        self.starfire_app_id = starfire_app_id
        # 星火模型API_KEY
        self.starfire_api_key = starfire_api_key
        # 星火模型API_SECRET
        self.starfire_api_secret = starfire_api_secret
        # 星火模型模型名称
        self.starfire_model_name = starfire_model_name

        # 通义模型是否开启
        self.is_open_ty = is_open_ty
        # 通义模型API_KEY
        self.ty_api = ty_api
        # 通义模型模型名称
        self.ty_model_name = ty_model_name
        # 是否开启根据新名称复制
        self.is_open_copy_lable_new_name = is_open_copy_lable_new_name

        self.model_list = []

        if self.is_open_starfire:
           self.model_list.append(ChatConfig(app_id=self.starfire_app_id,
                                   api_key=self.starfire_api_key,
                                   api_secret=self.starfire_api_secret,
                                   model_name=self.starfire_model_name))

        if self.is_open_ty:
           self.model_list.append(ChatConfig(api_key=self.ty_api,
                                             model_name=self.ty_model_name))

    def to_dict(self):
        # 将Config类实例转换为字典
        config_dict = self.__dict__.copy()
        # 将model_list中的ChatConfig实例也转换为字典
        config_dict['model_list'] = [model.__dict__ for model in config_dict['model_list']]
        return config_dict

    def to_json(self):
        # 使用to_dict方法将Config类实例转换为字典
        config_dict = self.to_dict()
        # 将字典转换为JSON格式的字符串
        return json.dumps(config_dict, ensure_ascii=False, indent=4)



