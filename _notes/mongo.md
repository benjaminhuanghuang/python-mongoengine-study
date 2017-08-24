## Using mongo config file
    - https://docs.mongodb.com/manual/reference/configuration-options/
    - mongod --config /etc/mongod.conf
    - mongod -f /etc/mongod.conf
    
## Show Index
    > db.user.getIndexes()
    
## Mongo query details
    > db.user.find().explain()
    
## Restart mongo
    Create mongo_restart script
    
    rm -fr ~/data/mongod.lock
    
    mognod -f mongod.conf
    
    chmod 755 mongo_restart