## About MongoEngine
    PyMongo is a mongodb driver, MongoEngine is a Document-Object Mapper based on ~~PyMongo~~
    
    mongoengine depends on pymongo and six
    
    mongoengine-0.13 pymongo 3.5.1 were used in this project
    
    
## Mongoengine config
    ```
    app.config['MONGODB_DB'] = 'test'
    app.config['MONGODB_HOST'] = '127.0.0.1'
    app.config['MONGODB_PORT'] = 27017
    app.config['MONGODB_USERNAME'] = 'admin'
    app.config['MONGODB_PASSWORD'] = '12345'
    
    or
    
    app.config['MONGODB_SETTINGS'] = {
      'db': 'test', 
      'username':'admin', 
      'password':'12345'
    }
    
    or 
    
    app.config.from_pyfile('config.json')
    db.init_app(app)
    
    ```
    
## ORM
    ```
    from mongoengine import MongoEngine

    db = MongoEngine()
    
    class User(db.Document):
        meta = {
            'collection': 'users',
            'ordering': ['-create_at'],
            'strict': False,
        }
        username = db.StringField(db_field="u", required=True, unique=True)
        password = db.StringField(db_field="p", required=True)
        email = db.EmailField(db_field="e", required=True, unique=True)
    ```
    
## MongoEngine field type
    email = db.StringField(required=True)
    
    username = db.StringField(max_length=30)
    
    password = db.StringField(required=True)
    
    create_at = db.DateTimeField(default=datetime.now)
    
    is_completed = db.BooleanField(default=False)
    
    status = db.IntField(db_field='s', choices=STATUS_TYPE)
    
    from_user = db.ReferenceField(User, db_field="fu", reverse_delete_rule=CASCADE)
    
## MongoEngine Query
    - Create
        todo1 = Todo(task='task 1', is_completed=False)
        
        todo1.save()
        
    - Require
        	
        todos = Todo.objects().all()

        users = User.objects(email__endswith('outlook.com'))
    
        user = User.objects.filter( username=form.username.data ).first()
        
    - Update
        user.update(password=admin123)
        
    - Delete
        user.delete()
        
    - Pagination
        todos = Todo.objects.paginate(page=page, per_page=10)

        todos = Todo.objects().order_by('-create_at').skip(skip_num)).limit(limit)
    