from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # API Keys
    openai_api_key: str
    gemini_api_key: str
    
    # Model Configuration
    openai_model: str = "gpt-4"
    gemini_model: str = "gemini-pro"
    
    # LLM Selection
    primary_llm: str = "openai"
    secondary_llm: str = "gemini"
    
    # Application
    debug: bool = True
    log_level: str = "INFO"
    app_name: str = "Agile AI Sprint Planner"
    
    # Server
    host: str = "0.0.0.0"
    port: int = 8000
    
    # Database
    database_url: str = "sqlite:///./sprint_planner.db"
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()