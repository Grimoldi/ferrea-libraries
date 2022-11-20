import os
from pathlib import Path

from ferrea import api

from routers import libraries

ferrea_app = os.environ["FERREA_APP"]
models_path = Path(__file__).parent / "definitions"
app = api.init_api(models_path=models_path, ferrea_app=ferrea_app)

app.include_router(libraries.router)
