from flask import Flask, render_template,request
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pickle

app=Flask(__name__)
vectorizer = pickle.load(open('model/vector.pkl', 'rb'))
clf=pickle.load(open('model/model.pkl','rb'))

@app.route('/',methods=['GET'])
def landing_page():
    return render_template("index.html")

def predict(password):
    sample_array = np.array([password])
    
    # 151 dimension
    sample_matrix = vectorizer.transform(sample_array) 
    
    # +2 dimension
    length_pass = len(password)
    length_normalised_lowercase = len([char for char in password if char.islower()])/len(password)
    
    # 151 + 2 
    new_matrix2 = np.append(sample_matrix.toarray() , (length_pass , length_normalised_lowercase)).reshape(1,155)

    
    
    result = clf.predict(new_matrix2)
    
    if result == 2 :
        return "Password is strong"
    elif result == 1 :
        return "Password is normal"
    else:
        return "password is strong"

@app.route('/checker',methods=['POST'])
def strength_checker():
    if request.method=="POST":
        data=request.form.get('password')
        return predict(data)
if __name__ == '__main__':
    app.run()