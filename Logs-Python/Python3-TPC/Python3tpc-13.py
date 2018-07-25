#! python3
# -*- coding: utf-8 -*-

import http.client
import xmlrpc.client


# curl -u huge:file http://www.pythonchallenge.com/pc/return/evil4.jpg --proxy 10.144.1.10:8080
# Bert is evil! go back!


class ProxiedTransport(xmlrpc.client.Transport):

    def set_proxy(self, host, port=None, headers=None):
        self.proxy = host, port
        self.proxy_headers = headers

    def make_connection(self, host):
        connection = http.client.HTTPConnection(*self.proxy)
        connection.set_tunnel(host, headers=self.proxy_headers)
        self._connection = host, connection
        return connection


transport = ProxiedTransport()
transport.set_proxy('10.144.1.10', 8080)
conn = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php", transport=transport)

# conn = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")  # 不用代理


print(conn.system.listMethods())
print(conn.system.methodHelp('phone'))
print(conn.phone('Bert'))

# 根据提示获得线索信息
# Link: http://www.pythonchallenge.com/pc/return/disproportional.html
# Next: http://www.pythonchallenge.com/pc/return/italy.html
#
# Points：
# - XML-RPC（XML Remote Procedure Call，XML远程方法调用）的定义
# - 标准库http模块：https://docs.python.org/3/library/http.html
# - 标准库xmlrpc模块：https://docs.python.org/3/library/xmlrpc.html
