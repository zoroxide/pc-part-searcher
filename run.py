import sys
import os
import uvicorn

# docker build -t pcpartsearcher .
# docker run --name=pc-part-searcher -p 5000:8000 pcpartsearcher

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", reload=True)