from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


from database import Base

class User(Base):
    __tablename__ = 'users' #table name on PostgreSQL 
    #Native Attributes
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    
    #Relationships
    #Games_title = Column(String, ForeignKey('games.title'), nullable=False)
    FavGames = relationship("Game", backref='FavouritedBy', uselist=True, foreign_keys=[id])

class Game(Base):
    __tablename__ = 'games' #table name on PostgreSQL 

    #Native Attributes

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    releaseDate = Column(String)

    #Relationships
    FavouritedBy = relationship('User', back_populates='user_FavGames')
    
    MinSpecGPU = Column(Integer, ForeignKey('GPUs.id'), nullable = True)
    MaxSpecGPU = Column(Integer, ForeignKey('GPUs.id'), nullable = True)
    
    MinSpecCPU = Column(Integer, ForeignKey('CPUs.id'), nullable = True)
    MaxSpecCPU = Column(Integer, ForeignKey('CPUs.id'), nullable = True)

    minSpecRam = Column(Integer, ForeignKey('RAM.id'), nullable = True)
    maxSpecRam = Column(Integer, ForeignKey('RAM.id'), nullable = True)

    minSpecStorage = Column(Integer, ForeignKey('Storage.id'), nullable = True)
    maxSpecStorage = Column(Integer, ForeignKey('Storage.id'), nullable = True)



class GPU(Base):
    __tablename__ = 'GPUs' #table name of Postgres table

    #native attributes
    id = Column(Integer, primary_key=True, index=True)
    vendor = Column(String)
    model = Column(String)
    modelFamily = Column(String)
    vram = Column(Integer)
    baseClockSpeed = Column(Integer)
    boostedClockSpeed = Column(Integer)
    memoryClock = Column(Integer)
    RTCores = Column(Integer)
    tdp = Column(Integer)
    suggestedPSU = Column(Integer)
    cudaCores = Column(Integer)
    tensorCores = Column(Integer)
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
    currentPriceAvg = Column(Integer)

    #relationships
    listOfMinSpec = relationship("Game", back_populates='MinSpecCPU')
    listOfMaxSpec = relationship("Game", back_populates='MaxSpecCPU')


class RAM(Base):
    __tablename__ = 'RAM'

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








