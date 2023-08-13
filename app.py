from flask import Flask, render_template, request
from gradio_client import Client

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    global client
    global result
    if request.method == 'POST':
        query = request.form.get('query')  # Access the value of the 'query' form field
        if query:
            
            try:


                client = Client("https://ysharma-explore-llamav2-with-tgi.hf.space/")
                if not client:
                    return render_template("index.html", input= "70B is in Cooling mode. Sorry!")
                result = client.predict(
                query,
                api_name="/chat_1"
                )
                if not result:
                    return render_template("index.html", input= "GPU is unable to respond :X")
                else:
                    return render_template("index.html", input= result)
            except:
                return render_template("index.html", input="Seems my brain has stopped working! Report has been sent to owner")
    return render_template("index.html", input="Start conversation by asking me anything...")

if __name__ == '__main__':
    app.run(debug=True)
