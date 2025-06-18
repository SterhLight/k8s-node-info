# app.py - part of k8s-node-info
# Copyright (C) 2025 krasava <al.popytaev@yandex.ru>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route('/')
def hello_world():
    hostname = socket.gethostname()
    node_name = os.getenv('NODE_NAME', 'unknown')
    return f"<h1>Hello from Kubernetes!</h1><p>Pod name: {hostname}</p><p>Node name: {node_name}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
