from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.search_routes import search_bp

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

options = {
    "Message": "Welcome to PC Part Searcher API, use the following instructions:",
    "Note":"sometimes search might take a while if you selected a big number of vendors",
    "search_endpoint": "/api/search",
    "search_options": {
        "search_term": "string (e.g., 'rtx')",
        "source_filters": {
            "amazon": "boolean (true/false)",
            "baraka": "boolean (true/false)",
            "olx":"boolean (true/false)",
            "sigma": "boolean (true/false)",
            "badr": "boolean (true/false)",
            "alfrensia":"boolean (true/false)"
        }
    }, 
    "Comming Soon": "Compumarts"
}

@app.get("/")
async def optios_route():
    return options

app.include_router(search_bp, prefix="/api")