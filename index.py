from fastapi import FastAPI
from routes.note import note

app = FastAPI()

# include router
app.include_router(note)

# run with: uvicorn index:app --reload
