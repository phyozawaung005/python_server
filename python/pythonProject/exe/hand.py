from flask import Flask, render_template, request
import re

app = Flask(__name__)

def detect_phishing_link(url):
    if not (url.startswith("http://") or url.startswith("https://")):
        return True  

    ip_address_pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
    if re.search(ip_address_pattern, url):
        return True  

    phishing_keywords = ["paypal", "login", "bank", "secure", "account", "confirm", "signin"]
    for keyword in phishing_keywords:
        if keyword in url:
            return True  

    domain = url.split("//")[-1].split("/")[0]
    if len(domain) > 30:
        return True  

    return False  

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        if detect_phishing_link(url):
            result = "might be a phishing link"
        else:
            result = "is not a phishing link"
        return render_template("index.html", result=result, input=url)
    return render_template("index.html", result=None, input=None)

if __name__ == "__main__":
    app.run(debug=True)
