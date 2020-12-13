
from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class cementpre(BaseModel):
    Cement: float 
    Slag: float 
    Ash: float 
    Water: float
    Superplasticizer: float
    Coarse : float
    Fine: float
    Age:int