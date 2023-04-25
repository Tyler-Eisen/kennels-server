from http.server import BaseHTTPRequestHandler, HTTPServer
from views import get_all_animals, get_single_animal, get_all_locations, get_single_location, get_single_employee, get_all_employees, get_single_customer, get_all_customers, delete_customer, delete_animal, delete_employee, delete_location, update_animal, update_customer, update_employee, update_location, get_customer_by_email, get_animal_by_location, get_employee_by_location, get_animal_by_status
import json
from urllib.parse import urlparse, parse_qs

class HandleRequests(BaseHTTPRequestHandler):
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """
    def parse_url(self, path):
        """Parse the url into the resource and id"""
        parsed_url = urlparse(path)
        path_params = parsed_url.path.split('/')  # ['', 'animals', 1]
        resource = path_params[1]

        if parsed_url.query:
            query = parse_qs(parsed_url.query)
            return (resource, query)

        pk = None
        try:
            pk = int(path_params[2])
        except (IndexError, ValueError):
            pass
        return (resource, pk)

    
    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Another method! This supports requests with the OPTIONS verb.
    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_GET(self):
        self._set_headers(200)

        response = {}

        # Parse URL and store entire tuple in a variable
        parsed = self.parse_url(self.path)

        # If the path does not include a query parameter, continue with the original if block
        if '?' not in self.path:
            ( resource, id ) = parsed

            # It's an if..else statement
            if resource == "animals":
                if id is not None:
                    response = get_single_animal(id)

                else:
                    response = get_all_animals()

            if resource == "locations":
                if id is not None:
                    response = get_single_location(id)

                else:
                    response = get_all_locations()
            if resource == "employees":
                if id is not None:
                    response = get_single_employee(id)

                else:
                    response = get_all_employees()
            if resource == "customers":
                if id is not None:
                    response = get_single_customer(id)

                else:
                    response = get_all_customers()

        else: # There is a ? in the path, run the query param functions
            (resource, query) = parsed

            # see if the query dictionary has an email key
            if query.get('email') and resource == 'customers':
                response = get_customer_by_email(query['email'][0])
            if query.get('location_id') and resource == 'animals':
                response = get_animal_by_location(query['location_id'][0])
            if query.get('status') and resource == 'animals':
                response = get_animal_by_status(query['status'][0])
            if query.get('location_id') and resource == 'employees':
                response = get_employee_by_location(query['location_id'][0])

        self.wfile.write(json.dumps(response).encode())    

    def do_DELETE(self):
    # Set a 204 response code
     self._set_headers(204)

    # Parse the URL
     (resource, id) = self.parse_url(self.path)

    # Delete a single animal from the list
     if resource == "animals":
         delete_animal(id)
    
     elif resource == "customers":
           delete_customer(id)
           
     elif resource == "employees":
           delete_employee(id)
           
     elif resource == "locations":
           delete_location(id)
            

    # Encode the new animal and send in response
     self.wfile.write("".encode())
   
    def do_POST(self):
        """Handles POST requests to the server
        """
        
        self._set_headers(201)

        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        response = f"received post request:<br>{post_body}"
        self.wfile.write(response.encode())

   

    def do_PUT(self):
     self._set_headers(204)
     content_len = int(self.headers.get('content-length', 0))
     post_body = self.rfile.read(content_len)
     post_body = json.loads(post_body)

    # Parse the URL
     (resource, id) = self.parse_url(self.path)

    # Delete a single animal from the list
     if resource == "animals":
           update_animal(id, post_body)
     elif resource == "customers":
           update_customer(id, post_body)
     elif resource == "employees":
           update_employee(id, post_body)
     elif resource == "locations":
           update_location(id, post_body)

    # Encode the new animal and send in response
     self.wfile.write("".encode())



def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8000
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
