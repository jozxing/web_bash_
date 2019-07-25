环境 python3
pip install -r requirements.txt
需要修改Pcommand/websocket/views.py 目录里的linux服务器信息
python3 manage.py runserver 8088

访问localhost:8088/command 即可通过web执行linux bash命令。

具体的只是通过django + websockets 实现的web页面执行bash命令，实际使用看个人所需
