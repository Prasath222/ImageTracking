from http.server import HTTPServer,BaseHTTPRequestHandler
content='''
<html>
    <title>SEMESTER</title>
    <body align="center">

        SEMESTER COURSE
        <Table align="center" border="5" celpadding="1">
            <tr><th>S.NO</th><th>COURSE NAME</th> </tr>
            <tr><th>1</th><th>WEB APPLICATION</th> </tr>
            <tr><th>2</th><th>PHYSICS</th> </tr>
            <tr><th>3</th><th>CHEMISTRY</th> </tr>
            <tr><th>4</th><th>C PROGRAMING</th> </tr>
            <tr><th>5</th><th>DIGITIAL ELECTRONICS</th> </tr>
        </Table>
    </body>
</html>
'''
class Myserver(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")
        self.end_headers()
        self.wfile.write(content.encode())
        print("This is my webserver") 
        server_address =('',8000)
        httpd = HTTPServer(server_address,Myserver)
        httpd.serve_forever()
