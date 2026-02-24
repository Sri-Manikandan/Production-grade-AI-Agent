from pydantic import BaseModel 

class NewsletterRequest(BaseModel):
    topic: str
    max_articles: int = 3
    