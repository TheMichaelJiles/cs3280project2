#! /usr/bin/python

import sys
import validation
import masker
import http.server

import http.server


class Server(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            path = self.path
            self.log_message("resource: %s", path)
            resource = path[1:]
            if not resource.startswith('subnet'):
                self.send_error(404, "ERROR: RESOURCE NOT VALID")

            resource_parts = resource[7:].split('&')
            print(resource[7:])
            subnet = get_subnet(resource_parts)
            response = get_response(subnet)

            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(response.encode('UTF-8'))
        except ValueError as error:
            self.send_error(400, str(error))

def get_response(subnet):
    html = "<!DOCTYPE html><html>"
    html += "<head><title>"
    html += "Calculated Subnet Michael"
    html += "</title></head>"
    html += "<body><p><h1>"
    html += "Subnet:<br>" + subnet.replace('\n', '<br>')
    html += "</h1></p></body>"
    html += "</html>"
    return html

def get_subnet(resources):
    ip = resources[0]
    mask = resources[1]

    if (validation.isValidIPV4Address(ip)):
        if validation.isValidBitNumberNotationNetmask(mask):
            mask = masker.convertN_NotationToOctet(mask)
        if validation.isValidOctectNetmask(mask):
            return masker.applyIPV4SubnetMask(ip, mask)
        else:
            print("ERROR: MASK INVALID")
            #throw mask invalid error
    elif (validation.isValidIPV6Address(ip)):
        if validation.isValidOctetNetmask(mask):
            return masker.apply

if __name__ == '__main__':
    DAEMON = http.server.HTTPServer(('localhost', 3280), Server)
    DAEMON.serve_forever()
