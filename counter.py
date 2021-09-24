from flask import Flask
from flask import render_template
from flask import session
from flask import redirect

app = Flask( __name__ )
app.secret_key = "secret"

@app.route( '/', methods=['GET'] )
def viewsCounter():
    if "counter" not in session:
        session["counter"] = 0
    else:
        session["counter"] += 1
    return render_template('index.html')

@app.route( '/destroy_session', methods=['GET'] )
def closeSession():
    session.clear()
    return redirect( '/' )

if __name__ == "__main__":
    app.run( debug = True )