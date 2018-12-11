# 第一步创建Django项目
# 第二步，创建app python3 manage.py startapp appname
# 第三步，同步数据库 python3 manage.py migrate
# 第四步，创建表，创建超级管理员 python3 manage.py createsuperuser
# 第五步，同步创建好的模型 python3 manage.py makemigrations

import pymysql
pymysql.install_as_MySQLdb()