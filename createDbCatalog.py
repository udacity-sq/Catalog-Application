from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import Catalog, Base, Items, User

 
engine = create_engine('sqlite:///catalogitemswithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Saad Qureshi", email="saadshaheen121@gmail.com",
             picture='https://lh3.googleusercontent.com/-xWOkI_KYENc/AAAAAAAAAAI/AAAAAAAAAAA/ACSILjWiEOa476mcfSHdc_tVf6FAD1qNhg/s192-c-mo/photo.jpg')
session.add(User1)
session.commit()

#Catalog Entry for Soccer
catalog1 = Catalog(category = "Soccer")

session.add(catalog1)
session.commit()

Item2 = Items(title = "Shinguards", description = "Shin Protection",  catalog = catalog1, user_id=1)

session.add(Item2)
session.commit()


Item1 = Items(title = "Two Shinguards", description = "A pair of Shinguards", catalog = catalog1, user_id=1)

session.add(Item1)
session.commit()


#Catalog Entry for Basketball
catalog2 = Catalog(category = "Basketball")

session.add(catalog2)
session.commit()


Item1 = Items(title = "Basketball", description = "Ball used to play basketball", catalog = catalog2, user_id=1)

session.add(Item1)
session.commit()


#Catalog Entry for Baseball
catalog1 = Catalog(category = "Baseball")

session.add(catalog1)
session.commit()

Item2 = Items(title = "Baseball Bat", description = "Used to hit baseball",  catalog = catalog1, user_id=1)

session.add(Item2)
session.commit()



#Catalog Entry for Frisbee
catalog1 = Catalog(category = "Frisbee")

session.add(catalog1)
session.commit()

Item2 = Items(title = "Frisbee", description = "Disk used to throw & catch",  catalog = catalog1, user_id=1)

session.add(Item2)
session.commit()


#Catalog Entry for Snowboarding
catalog1 = Catalog(category = "Snowboarding")

session.add(catalog1)
session.commit()

Item2 = Items(title = "Goggles", description = "Provides eye protection",  catalog = catalog1, user_id=1)

session.add(Item2)
session.commit()


Item1 = Items(title = "Snowboard", description = "Flat board used for sking", catalog = catalog1, user_id=1)

session.add(Item1)
session.commit()


#Catalog Entry for Rock climbing
catalog1 = Catalog(category = "Rock Climbing")

session.add(catalog1)
session.commit()

Item2 = Items(title = "Helmet", description = "Head Protection",  catalog = catalog1, user_id=1)

session.add(Item2)
session.commit()


#Catalog Entry for Foosball
catalog1 = Catalog(category = "Foosball")

session.add(catalog1)
session.commit()

Item2 = Items(title = "Table", description = "Foosball Table",  catalog = catalog1, user_id=1)

session.add(Item2)
session.commit()


#Catalog Entry for Skating
catalog1 = Catalog(category = "Skating")

session.add(catalog1)
session.commit()

Item2 = Items(title = "Ice Skates", description = "Special shoes for Skating",  catalog = catalog1, user_id=1)

session.add(Item2)
session.commit()



#Catalog Entry for Hockey
catalog1 = Catalog(category = "Hockey")

session.add(catalog1)
session.commit()

Item2 = Items(title = "Hockey Stick", description = "Used to play Hockey",  catalog = catalog1, user_id=1)

session.add(Item2)
session.commit()










print "added Catalog & items!"
