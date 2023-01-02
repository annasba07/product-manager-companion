import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        table1name = "Employee"
        table1fields = "id, name, department_id"
        
        query = request.form["query"]
        print(generate_single_sql_prompt(table1name,table1fields,table2name,table2fields, table3name, table3fields))
        response = openai.Completion.create(
            model="code-davinci-002",
            prompt=generate_single_sql_prompt(table1name,table1fields,table2name,table2fields, table3name, table3fields),
            temperature=0,
            max_tokens=150,
            stop=";",
           

        )
        print(response)
        
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result="Select "+ str(result))



def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )



def generate_single_sql_prompt(table1name, table1fieldnames,table2name,table2fieldnames, table3name, table3fieldnames):
    return """Provide SQL tables, with their properties:
    {}({})
    {}({})
    {}({})
    A query to list the names of the departments which employed more than 10 employees in the last 3 months
SELECT 
    """.format(table1name,table1fieldnames,table2name,table2fieldnames,table3name,table3fieldnames)


def takeindata():
    print('helloworld')


#schema_str = "Employees (id, name, department, salary); Departments (id, name, location)"
#schema_list = schema_str.split(";")
#tables = []
#for item in schema_list:
#  table_name, fields = item.split("(")
#  fields = fields.replace(")", "").split(",")
#  tables.append({
#    "name": table_name,
#    "fields": fields,
#  })

