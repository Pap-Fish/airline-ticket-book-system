# README

## 一、运行环境

1. python 3.7 或以上

2. django环境

   若有虚拟环境Anaconda,即可通过如下命令简单创建django环境

   ```cmd
   conda create --name <env_name> <package_names>
   ```

3. mysql数据库

   数据库相关配置在airticket文件夹的settings.py文件中，位置如下，可根据自己的情况修改

   ```python
   DATABASES = {
       # 'default': {
       #     'ENGINE': 'django.db.backends.sqlite3',
       #     'NAME': BASE_DIR / 'db.sqlite3',
       # }
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'airticket_book_sys',  # 自定义数据库连接名
           'USER': 'xxx',  # 数据库连接账户
           'PASSWORD': 'xxxxxxxxxxxx',  # 数据库连接密码
           'HOST': '127.0.0.1',  # 数据库服务地址
           'PORT': '3306',  # 数据库连接端口
       }
   }
   ```

   

## 二、项目启动步骤

1. 进入到源文件中manage.py所在的路径

2. 输入以下命令，项目即可启动 

   ```cmd
   python manage.py runserver
   ```

3. 输入网址 http://127.0.0.1:8000/airticket/ 即可进入网页



备注： 数据库中后缀为5074的表才是本项目涉及的表，其余表为django连接mysql数据库时生成的系统表
