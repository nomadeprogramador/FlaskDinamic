from flask import Flask
app=Flask(__name__)
@app.route('/dinamica/')
@app.route('/dinamica/<nome>')
def dinamica(nome=''):
    return '<h1> Hello {}</h1>'.format(nome)
if __name__ =='__main__':
    app.run(debug=True)