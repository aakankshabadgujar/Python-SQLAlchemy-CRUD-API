import os 
from flask import Flask, jsonify, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import NotFound #good for not found errors
#create flask app
app = Flask(__name__)


#database now
#using sqllite and tasks.db 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #not to track as it requires extrea memory adn raises warnings


#secret key for security in sessions
app.secret_key = os.urandom(24) #24 byte key each time app starts



#creating db instance
db = SQLAlchemy(app)


#now lets make the database model having columns representing a todo task and represnt the thing in dict type for json
class Task(db.Model): #pass ur db instance here for making table
    id = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String(100), nullable=False) #this is sqllite so this is how u do it here
    desc = db.Column(db.String(300), nullable = True)
    
    def __repr__(self):
        return f"Task(ID: {self.id}, Title: {self.title})"
    
    

#end the class here 
# --- Utility to Create Database Tables ---
# This runs once to create the database file and table if they don't exist
with app.app_context():
    db.create_all()


#lets make routes now and each func whateever it will do

@app.route('/', methods=['GET', 'POST']) 
def index(): 
    if request.method == 'POST':
        title = request.form.get('title') 
        desc = request.form.get('desc')
        #get all things
        
        if not title:
            return "Error: Title is required", 400 #enter status code as error
        
        newtask = Task(
            title = title,
            desc = desc
        ) #make this input form as a task object
        db.session.add(newtask) #add to session
        db.session.commit() #commit to db
        
        return redirect(url_for('index')) #redirect to new wala same index page after adding task
    
    #if no adding into table so just display all ur todos there on page 
    #tasks = Task.query.all() #get all tasks from table
    tasks = Task.query.order_by(Task.id.desc()).all() #get all tasks from table in descending order
    return render_template('index.html', tasks=tasks) #pass tasks with queried one


#now route to delete a task
@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    #get task by id 
    delwalatask = db.session.get(Task, id) #db session madhun task  ghetla id ne but purn ahe full row
    
    if delwalatask is None: #no id 
        raise NotFound(description=f"Task with ID {id} not found.") #here we use werkzeug exception for not found error
    
    db.session.delete(delwalatask) #delete from session task object of that id
    db.session.commit() #commit to db
    
    return redirect(url_for('index')) #redirect to index page after deletion


#now update the task
@app.route('/edit/<int:id>', methods = ['GET']) #only get method here no post allowed because we are displaying the thing which we wanna edit in here not update uet
def edit(id):
    editwalatask = db.session.get(Task, id)
    
    if editwalatask is None: 
        raise NotFound(description=f"Task with ID {id} not found.")
    
    return render_template('edit.html', task=editwalatask) #pass the task  to edit.html


#ata when u click btn u update it in db table
@app.route('/edit/<int:id>', methods = ['POST']) 
def update(id):
    editwalatask = db.session.get(Task, id)
    
    if editwalatask is None: 
        raise NotFound(description=f"Task with ID {id} not found.")
    
    editwalatask.title = request.form['title']
    editwalatask.desc = request.form['desc']
    #get things to update of that id from form
    
    db.session.commit() #commit changes to db
    
    
    return redirect(url_for('index')) 


#this will handle all error 404
@app.errorhandler(404)
def page_not_found(e):
    id = 'N/A'
    type = 'Page'
    
    if 'Task with ID' in str(e.description): #Detects a custom NotFound message you raised earlier (e.g., "Task with ID 5 not found.")
        try:
            id = str(e.description).split('Task with ID ')[1].split(' ')[0] #task with id nantr cha pahili space nantr ([1]) we have str tyamadhun apun " " madhe split kela and tyacha pahila means 5 here in eg
            type = 'Task' #as our db contains tasks
        except IndexError:
            pass
    
    return render_template('not_found.html', id=id, type=type), 404 


if __name__ == '__main__':
    app.run(debug=True)