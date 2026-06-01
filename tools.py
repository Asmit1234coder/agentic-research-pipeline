from langchain.tools import tool
import requests
import os
from tavily import TavilyClient
from dotenv import load_dotenv
from rich import print
from bs4 import BeautifulSoup

load_dotenv()

tavily=TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def search(query:str) -> str:
    """Get the recent and reliable information of given topic.Return Title,URL,content of articles"""
    response=tavily.search(query=query,max_results=5)

    out=[]
    for r in response['results']:
        out.append(
            f"Title: {r['title']}\nURL: {r['url']}\nSnippet: {r['content'][:300]}\n"
        )
    
    return "\n----\n".join(out)

    

print(search.invoke("Give me latest news about indian stock market"))

