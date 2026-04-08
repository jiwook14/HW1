import uvicorn

if __name__ == "__main__":
    # Runs the FastAPI server locally on port 8000
    print("Starting API Server at http://127.0.0.1:8000")
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
