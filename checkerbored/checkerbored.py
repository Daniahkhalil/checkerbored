from flask import Flask ,render_template 
app = Flask(__name__)    


@app.route('/')          
def hello_world():
    return render_template('index.html',rows=8,cols=4)  

    
@app.route('/<int:rows>')          
def rows(rows):
    return render_template('index.html',rows=rows,cols=4) 

@app.route('/<rows>/<cols>')          
def rows_cols(rows,cols):
    cols = int(cols)/2
    return render_template('index_2.html',rows=int(rows),cols=int(cols))  

if __name__=="__main__":     
    app.run(debug=True)    