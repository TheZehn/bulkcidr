import re
from flask import Flask, render_template, request 
import ipaddress


def cidr_to_ip_range(cidr):
    try:
        # Create an IP network object
        network = ipaddress.ip_network(cidr, False)

        first = str(network.network_address)
        last = str(network.broadcast_address)

        return (first, last)
    except ValueError as e:
        return None 

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/cidr", methods=["POST"])
def cidr():
    answer = {}
    cidrtext = request.form.get("cidr")
    list_cidr = cidrtext.split()
    for cidr in list_cidr:
        ip_range = cidr_to_ip_range(cidr)
        if ip_range:
            answer[cidr] = ip_range


    return render_template("data.html", data_dict=answer)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
