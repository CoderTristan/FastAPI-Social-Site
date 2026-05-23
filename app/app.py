from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate

app = FastAPI()

text_posts = {1: {"title": "World", "content": "content things"}, 2: {"title": "World", "content": "content things"}, 3: {"title": "World", "content": "content things"}}

@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code= 404, detail= "post not found")
    return text_posts.get(id)

@app.post("/posts")
def create_post(post: PostCreate):
    pass