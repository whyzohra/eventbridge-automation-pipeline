from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "running"}

@app.get("/events")
def get_events():
    return {
        "service": "eventbridge-automation-pipeline",
        "events_processed": 10234,
        "status": "healthy"
    }
