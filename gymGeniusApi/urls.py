from django.urls import path
from graphene_django.views import GraphQLView
# from users.schema import schema
from .schema import schema
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    # Only a single URL to access GraphQL
    #added csrf_exempt for when working with postman
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    # path("graphql", GraphQLView.as_view(graphiql=True, schema=schema)),
]