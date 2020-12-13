
from pydantic import BaseModel

class cementpre(BaseModel):
    Cement: float 
    Slag: float 
    Ash: float 
    Water: float
    Superplasticizer: float
    Coarse : float
    Fine: float
    Age:int
