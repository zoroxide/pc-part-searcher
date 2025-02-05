import sys
import os
import uvicorn

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", reload=True)