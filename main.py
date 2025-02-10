from fastapi import FastAPI

import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
