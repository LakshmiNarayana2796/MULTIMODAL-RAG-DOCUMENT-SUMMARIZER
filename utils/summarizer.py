from langchain.schema.messages import HumanMessage
from utils.config import llm

def summarize_text(text):
    prompt = f"Summarize the following text:\n\n{text}\n\nSummary:"
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content

def summarize_table(table):
    prompt = f"Summarize the following table:\n\n{table}\n\nSummary:"
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content

def summarize_image(encoded_image):
    prompt = [
        HumanMessage(content=f"Describe the contents of this image:"),
        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}}
    ]
    response = llm.invoke(prompt)
    return response.content
