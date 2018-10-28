import socket,os,time
server = socket.socket()
server.bind(('localhost',9999))

server.listen()

while True:
	conn ,  addr =server.accept()
	print ("new conn",addr)

	while True:
		print("wait order:")
		data = conn.recv(1024)
		if not data:
			print("客户端连接中断")
			break
		print("执行命令：",data)
		cmd_res = os.popen(data.decode()).read()
		#接收字符串，执行结果也是字符串
		print("send now",len(cmd_res))
		if len(cmd_res) == 0:
			cmd_res = "send no data"

		conn.send(str(len(cmd_res.encode())).encode("utf-8"))
		time.sleep(0.5)
		conn.send(cmd_res.encode("utf-8"))
		print("send done")
		os.path.isfile(r"E:\VUL-project\Socket")
		os.stat("socket_client.py")
server.close()

import hashilb
m= hashilb.md5()