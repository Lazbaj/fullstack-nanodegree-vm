from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import cgi
import crud

class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            ## Home page '/restaurants'
            if self.path.endswith('/restaurants'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += "<h1>Restaurants: </h1>"
                output += "<a href='/new'>ADD a new Restaurant</a><br>"
                output += print_restaurant_list()
                output += "</body></html>"
                self.wfile.write(output)
                return

            ## Page '/new' to create a new restaurant
            if self.path.endswith('/new'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += "<h1>Add a new Restaurant</h1>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/restaurants/new'><input name="restaurant_name" type="text" placeholder="New restaurant name"><input type="submit" value="Create"> </form>'''
                output += "</body></html>"
                self.wfile.write(output)
                return

            ## Page '/edit' to rename a restaurant
            if self.path.endswith('/edit'):
                pathlist = self.path.split("/")
                restaurant_id = pathlist [-2]
                restaurant_name = crud.getRestaurantName(restaurant_id)

                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += "<h1>%s</h1>" % restaurant_name
                output += '''<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/edit'><input name="new_name" type="text" placeholder="New name"><input type="submit" value="Rename"> </form>''' % restaurant_id
                output += "</body></html>"
                self.wfile.write(output)
                return

            ## Page '/delete' to request confirmation to delete a restaurant
            if self.path.endswith('/delete'):
                pathlist = self.path.split("/")
                restaurant_id = pathlist [-2]
                restaurant_name = crud.getRestaurantName(restaurant_id)

                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += "<h1>Are you sure you want to delete %s?</h1>" % restaurant_name
                output += '''<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/delete'><input type="submit" value="Delete"> </form>''' % restaurant_id
                output += "</body></html>"
                self.wfile.write(output)
                return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        try:
            ## POST '/new' to add a restaurant
            if self.path.endswith('restaurants/new'):
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))

                if ctype == 'multipart/form-data':
                    fields=cgi.parse_multipart(self.rfile, pdict)
                    new_restaurant_name = fields.get('restaurant_name')

                    crud.addRestaurant(new_restaurant_name[0])

                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

                    ## Output to confirm the ADD (note: change header)
                    # output = ""
                    # output += "<html><body>"
                    # output += "Created new restaurant: '%s'<br>" % new_restaurant_name[0]
                    # output += "<a href='/restaurants'>BACK</a><br>"
                    # output += "</body></html>"
                    # self.wfile.write(output)

            ## POST '/edit' to rename a restaurant
            if self.path.endswith('/edit'):
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))

                if ctype == 'multipart/form-data':
                    pathlist = self.path.split("/")
                    restaurant_id = pathlist [-2]

                    fields=cgi.parse_multipart(self.rfile, pdict)
                    new_name = fields.get('new_name')

                    crud.renameRestaurant(restaurant_id, new_name[0])

                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

            ## POST '/delete' to delete a restaurant
            if self.path.endswith('/delete'):

                pathlist = self.path.split("/")
                restaurant_id = pathlist [-2]

                crud.deleteRestaurant(restaurant_id)

                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.send_header('Location', '/restaurants')
                self.end_headers()

        except:
            pass

def print_restaurant_list():
    p = crud.getRestaurants()
    output = ""
    for e in p:
        output += "<p>"
        output += "%s<br>" % e.name
        output += "<a href = /%s/edit>Edit </a><br>" % e.id
        output += "<a href = /%s/delete>Delete </a><br>" % e.id
        output += "</p>"
    return output

def main():
    try:
        port = 8080
        server = HTTPServer(('',port),webserverHandler)
        print 'Web Server running on port %s' %port
        server.serve_forever()

    except KeyboardInterrupt:
        print '^C entered, stopping Web Server ...'
        server.socket.close()


if __name__ == '__main__':
    main()
