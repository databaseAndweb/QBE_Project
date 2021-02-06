#Python HTTP server for GraphQL.
from flask import Flask, render_template
from flask_graphql import GraphQLView
from schema import schema
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


app.add_url_rule('/qbe/', view_func=GraphQLView.as_view('graphql',
                 schema=schema, graphiql=True))
app.run(debug=True)
