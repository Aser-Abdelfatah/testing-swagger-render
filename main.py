from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Dummy Dataset API", description="Demo API with fixed responses", version="1.0")

# -------------------------
# Request Models
# -------------------------
class User(BaseModel):
    name: str
    email: str

class Usage(BaseModel):
    user_id: int
    dataset_id: int
    project_type: str

# -------------------------
# Endpoints
# -------------------------

# 1. Register a user
@app.post("/users/register")
def register_user(user: User):
    return {
        "message": "User registered successfully",
        "user_id": 1,
        "data": user
    }

# 2. Add usage
@app.post("/usage/add")
def add_usage(usage: Usage):
    return {
        "message": "Usage added",
        "usage_id": 101,
        "data": usage
    }

# 3. View user usage
@app.get("/usage/{user_id}")
def get_user_usage(user_id: int):
    return {
        "user_id": user_id,
        "usages": [
            {"dataset": "Dataset A", "project_type": "Research"},
            {"dataset": "Dataset B", "project_type": "Commercial"}
        ]
    }

# 4. View datasets by organization type
@app.get("/datasets/by-org-type/{org_type}")
def datasets_by_org_type(org_type: str):
    return {
        "org_type": org_type,
        "datasets": ["Dataset A", "Dataset B", "Dataset C"]
    }

# 5. Top 5 contributing organizations
@app.get("/organizations/top")
def top_organizations():
    return {
        "top_organizations": [
            "Org A", "Org B", "Org C", "Org D", "Org E"
        ]
    }

# 6. Datasets by format
@app.get("/datasets/by-format/{format}")
def datasets_by_format(format: str):
    return {
        "format": format,
        "datasets": ["Dataset CSV 1", "Dataset CSV 2"]
    }

# 7. Datasets by tag
@app.get("/datasets/by-tag/{tag}")
def datasets_by_tag(tag: str):
    return {
        "tag": tag,
        "datasets": ["Dataset Tagged 1", "Dataset Tagged 2"]
    }

# 8. Total datasets counts
@app.get("/datasets/counts")
def dataset_counts():
    return {
        "by_organization": {"Org A": 10, "Org B": 7},
        "by_topic": {"Health": 5, "Finance": 8},
        "by_format": {"CSV": 12, "JSON": 6},
        "by_org_type": {"Federal": 9, "State": 4}
    }

# 9. Top 5 datasets by users
@app.get("/datasets/top-used")
def top_datasets():
    return {
        "datasets": [
            {"name": "Dataset A", "users": 100},
            {"name": "Dataset B", "users": 90},
            {"name": "Dataset C", "users": 80},
            {"name": "Dataset D", "users": 70},
            {"name": "Dataset E", "users": 60},
        ]
    }

# 10. Usage distribution by project type
@app.get("/usage/distribution")
def usage_distribution():
    return {
        "distribution": {
            "Research": 50,
            "Commercial": 30,
            "Educational": 20
        }
    }

# 11. Top 10 tags per project type
@app.get("/tags/top-by-project")
def top_tags():
    return {
        "Research": ["AI", "ML", "Health", "Climate", "Data"],
        "Commercial": ["Finance", "Retail", "Logistics"],
        "Educational": ["Students", "Courses", "Labs"]
    }