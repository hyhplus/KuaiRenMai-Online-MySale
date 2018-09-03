# mysale

<h2>数据库my_sale</h2>
create database my_sale default charset=utf8;


<h2>项目主要目录：</h2>
1.前端页面：</br>
html --> 放在对应板块<br>
static --> 注意js/css/images的路径

2.后台代码：</br>
已经分了三个主要模块：</br>
user	用户信息展示<br>
pub		需求主页<br>
login	登录注册<br>



<h3>配置djaogo基本环境</h3>



<h3>加模块</h3>
pip3 install Pillow


<h3>项目结构</h3>
├── manage.py
├── mysale				# 项目配置文件夹
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── README.md			# 说明文档
├── static				# 静态文件
│   ├── css
│   │   ├── bootstrap.css
│   │   ├── main.css
│   │   ├── main.main.css
│   │   └── y.css
│   ├── images
│   └── js
│       ├── bootstrap.js
│       ├── jquery.js
│       └── popper.js
├── templates
│   ├── login			# 登录注册模板
│   ├── pub				# 需求模板
│   └── user			# 用户信息模板
├── user				# user app
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-36.pyc
│   │       └── __init__.cpython-36.pyc
│   ├── models.py
│   ├── tests.py
│   ├── urls_pub.py     # 主页url
│   ├── urls.py			#
│   ├── urls_user.py	# 用户个人信息url
│   ├── views_login.py  # 登录注册逻辑
│   ├── views_pub.py	# 发布需求,回复需求逻辑
│   ├── views.py		#
│   └── views_user.py	# 个人信息逻辑
