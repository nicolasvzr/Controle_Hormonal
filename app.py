from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime, timedelta
import os
import json

app = Flask(__name__)
app.secret_key = "nicolas-segredo"  # Necessário para usar 'session'

historico = []

if os.path.exists("data.json"):
    with open("data.json", "r") as file:
        historico = json.load(file)
else:
    historico = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        hormonio = request.form["hormonio"]
        data_aplicacao = request.form["data_aplicacao"]
        periodo = request.form["periodo"]
        tipo_periodo = request.form["tipo_periodo"]

        data_aplicacao = datetime.strptime(data_aplicacao, "%d/%m/%Y")
        periodo_conversao = int(periodo)

        if tipo_periodo == "dias":
            proxima_aplicacao = data_aplicacao + timedelta(days=periodo_conversao)
        else:
            proxima_aplicacao = data_aplicacao + timedelta(weeks=periodo_conversao)

        proxima = proxima_aplicacao.strftime("%d/%m/%Y")
        data_aplicacao_str = data_aplicacao.strftime("%d/%m/%Y")

        nova_entrada = {
            "hormonio": hormonio,
            "data_aplicacao": data_aplicacao_str,
            "proxima_aplicacao": proxima
        }

        historico.append(nova_entrada)

        with open("data.json", "w") as file:
            json.dump(historico, file, indent=4)

        # Armazena a próxima aplicação na sessão temporária
        session["proxima"] = proxima

        return redirect(url_for("index"))

    proxima = session.pop("proxima", None)  # pega e remove para não repetir
    return render_template("index.html", proxima=proxima, historico=historico)

@app.route("/delete/<int:index>", methods=["POST"])
def delete(index):
    if 0 <= index < len(historico):
        historico.pop(index)
        with open("data.json", "w") as file:
            json.dump(historico, file, indent=4)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)


