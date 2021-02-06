import sys
import graphene
import mysql.connector as mysql
from flask import request, url_for

class Table(graphene.ObjectType):
    table = graphene.String()
    
class Skeleton(graphene.ObjectType):
    table = graphene.String()
    columns = graphene.List(graphene.String)
    dataTypes = graphene.List(graphene.String)
    
class Answer(graphene.ObjectType):
    sqlquery = graphene.String()
    columns = graphene.List(graphene.String)
    dataTypes = graphene.List(graphene.String)
    answers = graphene.List(graphene.List(graphene.String))
    
class Queries(graphene.ObjectType):
    
    login = graphene.List(Table, user=graphene.String(), pwd=graphene.String(), db=graphene.String())
    skeletons = graphene.List(Skeleton, tnames=graphene.List(graphene.String), user=graphene.String(), pwd=graphene.String(), db=graphene.String())
    get_answers = graphene.List(Answer, tabPar=graphene.List(graphene.String), colPar=graphene.List(graphene.String),
            condPar=graphene.String(), user=graphene.String(), pwd=graphene.String(), db=graphene.String())

    
               
    def resolve_login(self, info, user,pwd,db):

        try:

            dbase = mysql.connect(
            host="localhost",
            database=db,
            user=user,
            passwd=pwd
            #auth_plugin='mysql_native_password')
            )

            query = "SELECT table_name FROM information_schema.tables WHERE table_schema = '"+db+"' "            
            cursor = dbase.cursor()
            cursor.execute(query)
            records = cursor.fetchall()
            cursor.close()
            dbase.close()
            tables = []
            for record in records:
                tables.append(Table(table=record[0]))
        
            return tables
        except:
            dbase.rollback()
            cursor.close()
            dbase.close()
            return []
        
    
    def resolve_skeletons(self, info,tnames,user,pwd,db):

        try:

            dbase = mysql.connect(
                host="localhost",
                database=db,
                user=user,
                passwd=pwd
                #auth_plugin='mysql_native_password'
            )

            result = []
            
            for item in tnames:
                query = "SELECT t.table_name,  sc.column_name, sc.data_type FROM information_schema.tables t INNER JOIN " + \
                "information_schema.columns sc ON t.table_schema=sc.table_schema AND t.TABLE_NAME = sc.TABLE_NAME WHERE t.table_schema = 'qbe' and " + \
                "t.TABLE_NAME = '"+item+"' " 
                cursor = dbase.cursor()
                cursor.execute(query)
                records = cursor.fetchall()
                print(records)

                cols = []
                dtypes = []

                for record in records:
                    cols.append(record[1])
                    dtypes.append(record[2])
                print(item, cols, dtypes)
                result.append(Skeleton(table=item, columns=cols, dataTypes=dtypes))
            cursor.close()
            dbase.close()
            return result
        except:
            dbase.rollback()
            cursor.close()
            dbase.close()
            return []
                
    def resolve_get_answers(self, info, tabPar, colPar,condPar, user, pwd, db):


        try:
            


            dbase = mysql.connect(
                host="localhost",
                database=db,
                user=user,
                passwd=pwd
                #auth_plugin='mysql_native_password'
            )


            print("nhgh hkhk", tabPar)
            print(colPar)
            print(condPar)

        except:
            return []
            
            
            
            
    
schema = graphene.Schema(query=Queries)


tt = Skeleton(graphene.ObjectType)
aa = Queries(graphene.ObjectType)
ab = []
bb = []
#print(aa.resolve_get_answers(tt,ab,bb, "yy", "qbe", "q123", "qbe"))
#print(aa.resolve_skeletons(tt, ab, "qbe", "q123", "qbe"))