from __future__ import annotations

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .data_loader import load_json, load_text

app = FastAPI(title="Struktogramm E-Learning API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"] ,
    allow_headers=["*"] ,
)


@app.get("/api/health")
def health_check() -> dict:
    return {"status": "ok"}


@app.get("/api/themes")
def list_themes() -> list[dict]:
    return load_json("themes.json")


@app.get("/api/milestones")
def list_milestones() -> list[dict]:
    milestones = load_json("milestones.json")
    for milestone in milestones:
        content_path = milestone.get("contentPath")
        if content_path:
            milestone["content"] = load_text(content_path)
    return milestones


@app.get("/api/milestones/{milestone_id}")
def get_milestone(milestone_id: str) -> dict:
    milestones = load_json("milestones.json")
    for milestone in milestones:
        if milestone["id"] == milestone_id:
            content_path = milestone.get("contentPath")
            if content_path:
                milestone["content"] = load_text(content_path)
            return milestone
    raise HTTPException(status_code=404, detail="Milestone nicht gefunden")


@app.get("/api/tasks")
def list_tasks(milestone: str | None = None) -> list[dict]:
    tasks = load_json("tasks.json")
    if milestone:
        return [task for task in tasks if task.get("milestoneId") == milestone]
    return tasks


@app.get("/api/operatorenliste")
def get_operatorenliste() -> dict:
    milestones = load_json("milestones.json")
    if not milestones:
        raise HTTPException(status_code=404, detail="Operatorenliste nicht gefunden")
    operator_path = milestones[0].get("operatorListPath")
    if not operator_path:
        raise HTTPException(status_code=404, detail="Operatorenliste nicht gefunden")
    return {
        "path": operator_path,
        "content": load_text(operator_path),
    }
