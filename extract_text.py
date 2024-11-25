import requests
from bs4 import BeautifulSoup
import openai
import os


def extract_text_from_url(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        for script_or_style in soup(["script", "style"]):
          script_or_style.decompose()
        texto = soup.get_text(separator= ' ')
        #limpar texto
        linhas = (line.strip() for line in texto.splitlines())
        parts = (phrase.strip() for line in linhas for phrase in line.split("  "))
        texto_limpo = '\n'.join(part for part in parts if part)
        return texto_limpo
    else:
      print(f"Failed to fetch the URL. Status code: {response.status_code}")
      return None

    text = soup.get_text()
    return text

extract_text_from_url("https://dev.to/kenakamu/azure-open-ai-in-vnet-3alo")
from langchain_openai.chat_models.azure import AzureChatOpenAI

client = AzureChatOpenAI(
    azure_endpoint= "https://oai-dio-bootcamp-dev-eastus-001.openai.azure.com/",
    api_key= "",
    api_version= "2023-03-15-preview",
    deployment_name= "gpt-4o-mini",
    max_retries=0
)

def translate_article(text, lang):
  messages =[
      ("system", "Você atua como tradutor de textos"),
      ("user", f"traduza o {text} para o idioma {lang} e responda em markdown")
  ]
  response = client.invoke(messages)
  print (response.content)
  return response.content

translate_article ("Let´s see the deployment was succeded", "portugues")
url = "https://dev.to/kenakamu/azure-open-ai-in-vnet-3alo"
text = extract_text_from_url(url)
article = translate_article(text, "pt-br")

print(article)