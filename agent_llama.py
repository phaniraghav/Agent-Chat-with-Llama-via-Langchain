from langchain_groq import ChatGroq

llm = ChatGroq(
    #model="llama-3.1-70b-versatile",
    model="llama-3.3-70b-versatile",
    temperature=0,
    groq_api_key='<GENERATE THE API KEY IN https://console.groq.com/keys>'

)

response = llm.invoke('What is the first ai agent')
print(response.content)
