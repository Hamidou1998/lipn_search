from flask import Flask, render_template,request
import sys
sys.path.append('../index_inverse/src')
from IndexInverse import IndexInverse

#Initialize the Flask application
app = Flask(__name__, template_folder='.')

#creation de l'index_inverser

doc=['lipn.fr_1','lipn.fr_2','lipn.fr_3']
textes=['I love shanghai','i am from shanghai now i study in tongji university',
        'i am from lanzhou now i study in lanzhou university of science  and  technolgy']
index=IndexInverse(doc,textes)
# index.test()
# print(index)
@app.route('/')
def index():
    return render_template('/html/index.html')
@app.route('/index')
def route_index():
    return render_template('/html/index.html')

@app.route('/recherche', methods=['GET'])
def recherche():
    index=IndexInverse(doc,textes)
    
    return render_template("/html/recherche.html",
    requete =request.args.get('recherche',default=""),
    tab_resultat = index.search(request.args.get('recherche',default="")))
    
if __name__ == '__main__':
    app.run(
        host="localhost",
        port=int("8011")
        #,debug=True
    )