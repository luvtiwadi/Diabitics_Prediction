from flask import Flask, request , render_template
import pickle

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

# @app.route('/math',methods=['POST','GET'])

@app.route('/math',methods=["POST"])
def inputs():
    return render_template('input.html')

# @app.route('/result',methods=['POST'])

# @app.route('/result',methods=['POST','GET'])
# def calculating():
#     if request.method=='POST':

#         pregnant=request.form['preg']
#         # pregnant=int(request.form.get('preg'))
#         glucose=float(request.form['glucose'])
#         # glucose=request.form.get('glucose')

#         bp=float(request.form['bp'])
#         # bp=request.form.get('bp')

#         st=float(request.form['st'])
#         # st=request.form.get('st')
#         insulin=float(request.form['insulin'])
#         # insulin=request.form.get('insulin')
#         bmi=int(request.form['bmi'])
#         # bmi=request.form.get('bmi')
#         dpf=float(request.form['dpf'])
#         # dpf=request.form.get('dpf')

#         age=int(request.form['age'])
#         # age=request.form.get('age')
#         # ,res=glucose
#         # print('pregenant')
#         return render_template('Result.html',res=pregnant)



@app.route('/result', methods=['POST'])
def calculating():
    if request.method == 'POST':
        pregnant = int(request.form.get('preg'))
        glucose = float(request.form.get('glucose'))
        bp = float(request.form.get('bp'))
        st = float(request.form.get('st'))
        insulin = float(request.form.get('insulin'))
        bmi = float(request.form.get('bmi'))
        dpf = float(request.form.get('dpf'))
        age = int(request.form.get('age'))

        # Perform calculations or any other logic here
        scaler=pickle.load(open("/config/workspace/model/scaler11.pkl","rb"))
        model=pickle.load(open("/config/workspace/model/regressor11.pkl","rb"))
        scaled_data=scaler.transform([[pregnant,glucose,bp,st,insulin,bmi,dpf,age]])
        predict=model.predict(scaled_data)

        if predict[0]==1:
            result="Diabetic"
        else:
            result="Not a Diabitic"

        return render_template('Result.html', res=result)
    else:
        return render_template('input.html')
 


if __name__=="__main__":
    app.run(host="0.0.0.0")
