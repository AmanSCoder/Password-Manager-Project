from flask import Flask, render_template,request

app=Flask(__name__)

@app.route('/',methods=['GET'])
def landing_page():
    return render_template("index.html")


@app.route('/checker',methods=['POST'])
def strength_checker():
    if request.method=="POST":
        data=request.form.get('password')
        return data+" Strength"
if __name__ == '__main__':
    app.run()