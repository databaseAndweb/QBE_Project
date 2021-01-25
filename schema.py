import sys
import graphene
import mysql.connector as mysql


class Table(graphene.ObjectType):
    #table = graphene.String()
    table = graphene.List(graphene.String)
    


class Senator(graphene.ObjectType):
    lname = graphene.String()
    fname = graphene.String()
    birthday = graphene.Date()
    gender = graphene.String()
    state = graphene.String()
    party = graphene.String()
    url = graphene.String()
    twitter = graphene.String()
    facebook = graphene.String()
    youtube = graphene.String()
    

class HRep(graphene.ObjectType):
    lname = graphene.String()
    fname = graphene.String()
    birthday = graphene.Date()
    gender = graphene.String()
    state = graphene.String()
    district = graphene.Int()
    party = graphene.String()
    url = graphene.String()
    twitter = graphene.String()
    facebook = graphene.String()
    youtube = graphene.String()


class Queries(graphene.ObjectType):
    senators = graphene.List(Senator)
    hreps= graphene.List(HRep)
    login = graphene.List(Table, user=graphene.String(), pwd=graphene.String(), db=graphene.String())

    def resolve_login(self, info, user,pwd,db):
        
        db = mysql.connect(
            host="localhost",
            database="qbe",
            user="qbe",
            passwd="q123"
            #auth_plugin='mysql_native_password'
        )
        query = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'qbe' "            
        cursor = db.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        cursor.close()
        db.close()
        #if len(records) == 0:
        #  return ??
        tables = []
        for record in records:
            tables.append(Table(table=record))
        
        #tables = [item for sublist in tables for item in sublist]
        
        return tables

    def resolve_senators(self, info):
        db = mysql.connect(
            host="localhost",
            database="qbe",
            user="qbe",
            passwd="q123"
            #auth_plugin='mysql_native_password'
        )
        query = "select lname, fname, birthday, gender, state, "+ \
                 "party, url, twitter, facebook, youtube  from SENATOR "            
        cursor = db.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        cursor.close()
        db.close()
        #if len(records) == 0:
        #  return ??
        senators = []
        for record in records:
            senators.append(Senator(lname=record[0], fname=record[1], birthday=record[2], gender=record[3],
             state=record[4], party=record[5], url=record[6], twitter=record[7], facebook=record[8], youtube=record[9]))
        return senators
    
    def resolve_hreps(self, info):
        db = mysql.connect(
            host="localhost",
            database="qbe",
            user="qbe",
            passwd="q123"
            #auth_plugin='mysql_native_password'
        )
        query = "select lname, fname, birthday, gender, state, "+ \
                 "district, party, url, twitter, facebook, youtube  from HREP "            
        cursor = db.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        cursor.close()
        db.close()
        #if len(records) == 0:
        #  return ??
        hreps = []
        for record in records:
            hreps.append(HRep(lname=record[0], fname=record[1], birthday=record[2], gender=record[3],
             state=record[4], district=record[5], party=record[6], url=record[7], twitter=record[8], facebook=record[9], youtube=record[10]))
        return hreps

    
schema = graphene.Schema(query=Queries)
# tt = Table(graphene.ObjectType)
# aa = Queries(graphene.ObjectType)
# print(aa.resolve_login(tt, "qbe", "q123", "qbe"))