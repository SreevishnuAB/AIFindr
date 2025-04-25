import os
from google import genai
from google.genai import types

from backend.models.profile import CompatibilityReasoning
from dotenv import load_dotenv

load_dotenv()

class LLMUtils:

    def __init__(self):
        self.client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

    def get_embeddings(self, text: str) -> list:
        """
        Get embeddings for the given text.
        """

        result = self.client.models.embed_content(
            model="gemini-embedding-exp-03-07",
            contents=text,
            config=types.EmbedContentConfig(task_type="SEMANTIC_SIMILARITY")
            )
        return result.embeddings[0].values
    
    def get_reasoning(self, query: str, profile: str) -> CompatibilityReasoning:
        """
        Asks LLM why a profile fits a prompt
        """

        res = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[f'Given the query: {query} and the profile: {profile}, explain why they are a match.'],
            config={
                'response_mime_type': 'application/json',
                'response_schema': CompatibilityReasoning,
            },
        )
        return res.parsed