import sys
import graphene
import mysql.connector as mysql
from flask import request, url_for, session
import cgi


class Table(graphene.ObjectType):
    #table = graphene.String()
    table = graphene.List(graphene.String)
    
class Skeleton(graphene.ObjectType):
    #skeleton = graphene.List(graphene.NonNull(graphene.String))
    # skeleton = graphene.List(graphene.String)
    rm = graphene.String()
    nameAndtype = graphene.String()
    
    

class Building(graphene.ObjectType):
    bcode = graphene.String()
    bname = graphene.String()

class Media(graphene.ObjectType):
    mcode = graphene.String()
    description = graphene.String()

class Room(graphene.ObjectType):
    bldg = graphene.String()
    rnumber = graphene.String()
    cap = graphene.Int()
    layout = graphene.String()
    rtype = graphene.String()
    dept = graphene.String()
    media = graphene.List(Media)

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
    
    buildings = graphene.List(Building)
    media = graphene.List(Media)
    rooms = graphene.List(Room,building=graphene.String())
    room = graphene.Field(Room,building=graphene.String(),
                               rno=graphene.String())
    roommedia = graphene.List(Media,building=graphene.String(),
                                    rno=graphene.String())
    roomscap = graphene.List(Room,cap_lower=graphene.Int(),
                                  cap_upper=graphene.Int())

    senators = graphene.List(Senator)
    hreps= graphene.List(HRep)
    #tnames2 = graphene.Field( args={'tnames':graphene.List(graphene.String)})
    login = graphene.List(Table, user=graphene.String(), pwd=graphene.String(), db=graphene.String())
    skeletons = graphene.List(Skeleton, tnames=graphene.List(graphene.String), user=graphene.String(), pwd=graphene.String(), db=graphene.String())
    
    def resolve_login(self, info, user,pwd,db):

        dbase = mysql.connect(
        host="localhost",
        database="qbe",
        user="qbe",
        passwd="q123"
        #auth_plugin='mysql_native_password')
        )

        if user =='qbe' and db == 'qbe' and pwd == 'q123':
            query = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'qbe' "            
            cursor = dbase.cursor()
            cursor.execute(query)
            records = cursor.fetchall()
            cursor.close()
            dbase.close()
            #if len(records) == 0:
            #  return ??
            tables = []
            for record in records:
                tables.append(Table(table=record))
        
            #tables = [item for sublist in tables for item in sublist]
        
            return tables
        
    
    def resolve_skeletons(self, info,tnames,user,pwd,db):

        if user =='qbe' and db == 'qbe' and pwd == 'q123':
            


            db = mysql.connect(
                host="localhost",
                database="qbe",
                user="qbe",
                passwd="q123"
                #auth_plugin='mysql_native_password'
            )
            # if user =='qbe' and db == 'qbe' and pwd == 'q123':
                # query = "SELECT column_name, data_type FROM information_schema.columns WHERE TABLE_NAME = @nm and table_schema = 'qbe' " 
            query = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'qbe' "            
            cursor = db.cursor()
            cursor.execute(query)
            records = cursor.fetchall()
            records = [x[0] for x in records]
            
            for i in records:
                tnames.append(i)

            bbb = []
            #item = 'BUILDING'
            
            for item in tnames:
                if item in records:

                    query2 = "SELECT t.table_name,  sc.column_name, sc.data_type FROM information_schema.tables t INNER JOIN " + \
                    "information_schema.columns sc ON t.table_schema=sc.table_schema AND t.TABLE_NAME = sc.TABLE_NAME WHERE t.table_schema = 'qbe' and " + \
                    "t.TABLE_NAME = '"+item+"' " 
                    cursor = db.cursor()
                    cursor.execute(query2)
                    records2 = cursor.fetchall()
                    #print(records2)
                    bbb.append(records2)
                    break
                else:
                    return None

            
            #list1 = list(set([x[0] for x in bbb]))
            #print(list1)
            list2 = [el[1:] for el in records2]
            #print(list2)
            
            cursor.close()
            db.close()
            skeletons2 = []
            listChars = []
            
            for field, value in list2:
                res = '{}({})'.format(field,value)
                listChars.append(res)
            print(listChars)
            
            final = listChars
            print(final)
            
            skeletons2 = [Skeleton(nameAndtype=element) for element in final]
            # for element in final:
            #     skeletons2.append(Skeleton(nameAndtype=element))

            
            
            return skeletons2
        else:
            return None
        



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


tt = Skeleton(graphene.ObjectType)
aa = Queries(graphene.ObjectType)
ab = []
print(aa.resolve_skeletons(tt,ab, "qbe", "q123", "qbe"))