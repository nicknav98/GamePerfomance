from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy import relationship


from .database import Base

class User(Base):
    __tablename__ = 'users' #table name on PostgreSQL 
    #Native Attributes
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    
    #Relationships
    FavGames = relationship("Game", back_populates="FavouritedBy")

class Game(Base):
    __tablename__ = 'games' #table name on PostgreSQL 

    #Native Attributes

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    releaseDate = Column(String)

    #Relationships
    FavouritedBy = Column(String, ForeignKey='users.FavGames')
    
    MinSpecGPU = Column(String, ForeignKey='GPUs.model')
    MaxSpecGPU = Column(String, ForeignKey='GPUs.model')
    
    MinSpecCPU = Column(String, ForeignKey='CPUs.model')
    MaxSpecCPU = Column(String, ForeignKey='CPUs.model')

    minSpecRam = Column(String, ForeignKey='RAM.amount')
    maxSpecRam = Column(String, ForeignKey='RAM.amount')

    minSpecStorage = Column(String, ForeignKey='Storage.capacity')
    maxSpecStorage = Column(String, ForeignKey='Storage.capacity')



class GPU(Base):
    __tablename__ = 'GPUs' #table name of Postgres table

    #native attributes
    id = Column(Integer, primary_key=True, index=True)
    vendor = Column(String)
    model = Column(String)
    vram = Column(Integer)
    baseClockSpeed = Column(Integer)
    boostedClockSpeed = Column(Integer)
    cudaCores = Column(Integer)
    rayTracingCores = Column(Integer)
    currentPriceAvg = Column(Integer)
    
    #relationships
    listOfMinSpec = relationship("Game", back_populates='MinSpecGPU')
    listOfMaxspec = relationship("Game", back_populates='MaxSpecGPU')

class CPU(Base):
    __tablename__ = 'CPUs'

    #native attributes
    id = Column(Integer, primary_key=True, index=True)
    vendor = Column(String)
    model = Column(String)
    l3Cache = Column(Integer)
    d3Cache = Column(Integer)
    baseClock = Column(String)
    boostClock = Column(String)

    #relationships
    listOfMinSpec = relationship("Game", back_populates='MinSpecCPU')
    listOfMaxSpec = relationship("Game", back_populates='MinSpecCPU')


class RAM(Base):
    __tablename__ = 'ram'

    #native attributes
    id = Column(Integer, primary_key=True, index=True)
    vendor = Column(String)
    model = Column(String)
    amount = Column(Integer)

    #relationships
    listOfMinSpec = relationship("Game", back_populates='MinSpecRam')
    listOfMaxSpec = relationship("Game", back_populates='MaxSpecRam')




class Storage(Base):
    __tablename__ = 'Storage'

    #native attributes
    id = Column(Integer, primary_key=True, index=True)
    vendor = Column(String)
    model = Column(String)
    storageType = Column(String)
    capacity = Column(Integer)

    #relationships
    listOfMinSpec = relationship("Game", back_populates='minSpecStorage')
    listofMaxSpec = relationship("Game", back_populates='maxSpecStorage')








