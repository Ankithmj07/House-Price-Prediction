from flask import render_template,Flask,request,jsonify,json,url_for
from model_files.ml_model import objPredict,ClusterSimilarity
from model_files.ml_model import column_ratio,ratio_name,ratio_pipeline,pipeline_transformer,predict_data


app = Flask('__name__')
app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def test():
    return render_template('index.html')


@app.route('/send-details',methods=['GET','POST'])
def sendDetails():
    longitude=request.form['longitude']
    latitude=request.form['latitude']
    medianAge=request.form['medianAge']
    totalRooms=request.form['totalRooms']
    totalBedrooms=request.form['totalBedrooms']
    population=request.form['population']
    households=request.form['households']
    income=request.form['income']
    oceanProximity=request.form['oceanProximity']
    oceanStr=str(oceanProximity)

    if not longitude and not latitude and not medianAge and not totalRooms and not totalBedrooms and not population and not households and not income and not oceanProximity:
        return '[{"errFlag":1,"message":"Some Fields are Empty"}]'
    
    else:
        data=objPredict.makeDict(longitude,latitude,medianAge,totalRooms,totalBedrooms,population,households,income,oceanProximity)
        return predict_data(data)

@app.route('/Prediction',methods=['GET'])
def returnPrediction():
    return render_template('result.html')
    




if __name__=='__main__':
    app.run(host='0.0.0.0',debug = True,port=8081)