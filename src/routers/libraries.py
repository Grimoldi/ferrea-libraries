from fastapi import APIRouter, Depends, status
from fastapi_utils.cbv import cbv
from ferrea.db_engine import DBInterface, Neo4jInterface
from models.library import CreateLibrary
from operations.db_libraries import LibrariesOperation
from starlette.responses import JSONResponse

router = APIRouter()


def get_db() -> DBInterface:
    """
    This function just returns the instance of the db object.
    Needed a funcion for the "Depends" on fastapi.

    Returns:
        type[DBInterface]: an instance that matches the DBInterface protocol.
    """
    return Neo4jInterface()


@cbv(router)
class LibraryViews:
    """
    This class holds the endpoints for the app.
    """

    db: DBInterface = Depends(get_db)

    @router.get("/libraries")
    def search_all_libraries(self) -> JSONResponse:
        lib_ops = LibrariesOperation(self.db)
        libraries = lib_ops.find_all_libraries()
        if libraries:
            return JSONResponse(
                content=[library.serialize() for library in libraries],
                status_code=status.HTTP_200_OK,
            )
        else:
            return JSONResponse(
                content="not found", status_code=status.HTTP_404_NOT_FOUND
            )

    @router.get("/libraries/{id}")
    def search_library_by_id(self, id: str) -> JSONResponse:
        lib_ops = LibrariesOperation(self.db)
        library = lib_ops.find_library(name=id)
        if library:
            return JSONResponse(
                content=library.serialize(), status_code=status.HTTP_200_OK
            )
        else:
            return JSONResponse(
                content="not found", status_code=status.HTTP_404_NOT_FOUND
            )

    @router.post("/libraries")
    def create_new_library(self, data: CreateLibrary) -> JSONResponse:
        lib_ops = LibrariesOperation(self.db)
        new_library = lib_ops.create_library(data)
        return JSONResponse(
            content=new_library.serialize(), status_code=status.HTTP_200_OK
        )
