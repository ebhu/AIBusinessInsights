from openai import OpenAI

#method to use chatGPT to process something
def aiProcess(prompt):
  #connect to openai api using my api key
  client = OpenAI(api_key="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")  
  #create a chat with chatGPT  
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
     messages=[
       {
        "role": "user",
        "content": prompt
      }
     ],
  
    temperature=0,
    max_tokens=1000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
    #gather just the response from the ai and remove all the other information
  response_content_string = response.choices[0].message.content
  client.close()
    #return the response
  return response_content_string

