from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from app.routes.search_routes import search_bp

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def optios_route():
    html_content = """
    <html>
        <head>
            <title>PC Part Searcher API</title>
        </head>
        <body>
            <h1>Welcome to PC Part Searcher API</h1>
            <p>Note: Sometimes search might take a while if you selected a big number of vendors</p>
            <p>Use the following instructions:</p>
            <ul>
                <li>Search Endpoint: <code>/api/search</code></li>
                <li>Search Options:
                    <ul>
                        <li>search_term: string (e.g., 'rtx')</li>
                        <li>source_filters:
                            <ul>
                                <li>amazon: boolean (true/false)</li>
                                <li>baraka: boolean (true/false)</li>
                                <li>olx: boolean (true/false)</li>
                                <li>sigma: boolean (true/false)</li>
                                <li>badr: boolean (true/false)</li>
                                <li>alfrensia: boolean (true/false)</li>
                            </ul>
                        </li>
                    </ul>
                </li>
            </ul>
            <p>Coming Soon: Compumarts</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)

app.include_router(search_bp, prefix="/api")