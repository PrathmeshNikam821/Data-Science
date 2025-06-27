from flask import Flask, render_template,request

app = Flask(__name__)


@app.route("/")
def Welcome():
    return "<html><h1>Hello World <h1></html>"

@app.route("/index")
def index():
  return render_template('index.html')

@app.route("/about")
def about():
  return render_template('about_us.html')


@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

#variable rule 
@app.route('/success/<int:score>')
def success(score):
  if score>50:
    res='PASS'
  else:
    res='FALSE'
  
  return render_template('result.html',results=res , marks=score)


@app.route('/successres/<int:score>')
def success_results(score):
  if score>50:
    res='PASS'
  else:
    res='FALSE'
    
  exp = {'score':score , 'res':res}
  
  return render_template('result1.html',results=exp)



#if else 
@app.route('/successif/<int:score>')
def successif(score):
  return render_template('results2.html', marks=score)




if __name__ == "__main__":
  app.run(debug=True)