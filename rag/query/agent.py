from ollama import chat
import requests
import config
import logging
from rag.exceptions import LLMError
from pydantic import BaseModel
import requests
import logging
import json

logger = logging.getLogger("tos-analyzer")

class LLMResponse(BaseModel):
    response: str


def generate_prompt(question: str, context: str, error_message: str = "") -> str:
    error_hint = f"\nPrevious attempt failed: {error_message}\nFix the query." if error_message else ""
    return f"""
            You are a legal assistant specialized in analyzing Terms of Service.

            Instructions:
            - Answer ONLY using provided context
            - Highlight risks clearly
            - Be concise and structured
            - If unsure, say "Not found in document"

            User question: {question} 
            {error_hint}
            Use this as the context: {context}
            """

def prompt_agent(question: str, context: str,  max_retries: int = config.NUM_RETRIES) -> LLMResponse:
    error_message = ""
    for _ in range(max_retries):
        try:
            logger.info(f"Prompting for {question}")
            prompt = generate_prompt(question, context, error_message)
            response = chat(model=config.OLLAMA_MODEL, messages=[
                {
                    'role': 'user',
                    'content': f'{prompt}',
                },
            ], format=LLMResponse.model_json_schema())
            logger.info(f"{error_message}: {response}")
            parsed = LLMResponse.model_validate_json(response.message.content)
            logger.info(f"Parsed response: {parsed}")
            return parsed
        except Exception as e:
            error_message = f"{e}"
            logger.error(f"{error_message}")
            print(f"{error_message}")
            logger.error(f"{error_message}")
    raise LLMError(f"failed to run the agent with error {error_message}")