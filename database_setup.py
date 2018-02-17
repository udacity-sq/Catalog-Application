import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))
 
class Catalog(Base):
    __tablename__ = 'catalog'
   
    id = Column(Integer, primary_key=True)
    category = Column(String(250), nullable=False)
    

    @property
    def serialize(self):
        #Returns object data in easily serializeable format
        return {
            'category' : self.category,
            'id': self.id,
            
        }
 
class Items(Base):
    __tablename__ = 'items'

    title =Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    category_id = Column(Integer,ForeignKey('catalog.id'))
    catalog = relationship(Catalog)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


    
    @property
    def serialize(self):
        #Returns object data in easily serializeable format
        return {
            'title' : self.title,
            'description' : self.description,
            'id' : self.id,
            'category Id' : self.category_id,
            
        }
 

engine = create_engine('sqlite:///catalogitemswithusers.db')
Base.metadata.create_all(engine)
