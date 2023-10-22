from pymongo import MongoClient
url = 'mongodb+srv://rameshindia53:Wixmongodbpass@cluster0.hmlnnxr.mongodb.net/employeesdb?retryWrites=true&w=majority'
client = MongoClient(url)

try:
    client.admin.command('ping')
    # print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client['employeesdb']
coll = db.get_collection('employees')
data = list(coll.find({}))
