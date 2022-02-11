import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"


schema = strawberry.Schema(Query)


graphql_app = GraphQLRouter(schema)


app = FastAPI(docs_url=None, redoc_url=None)
app.include_router(graphql_app, prefix="/graphql")
