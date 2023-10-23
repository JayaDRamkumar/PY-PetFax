from flask import ( Blueprint, render_template ) 

bp = Blueprint('fact', __name__, url_prefix="/add_fun_fact")


@bp.route('/add_fun_fact')
def funfact():
    
    return render_template('add_fun_fact.html')