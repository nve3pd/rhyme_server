import sys
sys.path.append("server")
import server

server.app.run(port=8080)
