from flask import Flask
import os
app = Flask(__name__, static_url_path='')

@app.route("/", methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        return
    else:
        return app.send_static_file('./webpage.html')

@app.route("result")
def root():
    return app.send_static_file('./results.html')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
