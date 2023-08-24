from pydantic import BaseModel

class GameBase(BaseModel):
    title: str
    releaseDate : str | None = None

class Game(GameBase):
    id: int
    FavouritedBy = list = []
    MinSpecGPU : str
    MaxSpecGPU : str
    MinSpecCPU : str
    MaxSpecCPU : str
    minSpecRam : str
    maxSpecRam : str
    minSpecStorage: str
    maxSpecStorage: str

    class Config:
        orm_mode = True

class GameCreate(GameBase):
    pass

# ---------------- END OF GAME schema


class GPUBase(BaseModel):
    id : int
    vendor : str
    model : str
    modelFamily : str
    vram : str 
    baseClockSpeed : int
    boostedClockSpeed : int
    memoryClock : int
    RTCores: int
    tdp: int
    suggestedPSU: int
    cudaCores : int 
    tensorCores : int
    currentPriceAvg : int
    listOfMinSpec : list = []
    listofMaxSpec : list = []

    class Config:
        orm_mode = True

class GPUCreate(GPUBase):
    pass

# --------------------- END OF GPU Schema

class CPUBase(BaseModel):
    id : int
    vendor : str
    model : str
    l3cache : int
    d3cache : int
    baseClock : str
    boostClock : str

    listOfMinSpec : list = []
    listOfMaxSpec : list = []

    class Config:
        orm_mode = True

class CPUCreate(CPUBase):
    pass

# -------------------- END OF CPU Schema 



class RAMBase(BaseModel):
    id : int
    vendor : str
    model : str
    amount : int

    listOfMinSpec : list = []
    listOfMaxSpec : list = []

    class Config:
        orm_mode = True

class RAMCreate(RAMBase):
    pass
#--------------- END OF RAM Schema


class StorageBase: 
    id: int
    vendor : str
    model : str 
    storageType : str
    capacity : int 

    listOfMinSpec : list = []
    listOfMaxSpec : list = []

#-------------- END OF RAM Schema 



class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool 
    is_admin: bool
    FavGames = list[GameBase] = []


    class Config:
        orm_mode = True

#------------- End Of User Schema 
        

class Token(BaseModel):
    token: str
    token_type: str

    class Config:
        orm_mode = True


class TokenData(BaseModel):
    email: str

    class Config:
        orm_mode = True

# ---------- END OF token schema 