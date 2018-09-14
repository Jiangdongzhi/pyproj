import SocketServer
class MyServer(SocketServer.BaseRequestHandler):
    def handle(self):
        conn = self.request
        conn.sendall('multi-threading')
        Flag = True
        while Flag:
            data = conn.recv(1024)
            if data == 'exit':
                Flag = False
            elif data == '0':
                conn.sendall('0 inputted')
            else:
                conn.sendall('Re-enter')

if __name__ == '__main__':
    server = SocketServer.ThreadingTCPServer(('127.0.0.1',8009),MyServer)
    server.serve_forever()
