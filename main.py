from flask import Flask, render_template #importamo knjižnico iz objekta Flask

app = Flask(__name__) # naredimo objekt iz tega classa flask; main je ime trenutni porgram, ki teče

@app.route('/') #dekoratorji, funkcijo oplemenitijo; na določenem programu se bo izvajala funkcija
def index():
    return render_template("index.html")

@app.route('/o-meni')
def about_me():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(use_reloader=True)
