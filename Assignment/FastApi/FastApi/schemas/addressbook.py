from pydantic import BaseModel
#from models.index import users
class users(BaseModel):
    name : str
    Email : str
    Address : str
    Pincode : int