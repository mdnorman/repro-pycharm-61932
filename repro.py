import strawberry


@strawberry.type
class MyType:
    id: strawberry.ID
    first_name: str
    last_name: str

    @strawberry.field
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
