from flask import Flask, redirect, render_template, request, url_for
from duckduckgo_search import DDGS
import json
from bson.objectid import ObjectId

from startpage import Startpage
import os

from mongoMethods import mongoInsertDataMethod, getAllMongo
from coicopModule import findCoicop,findSIC_ofCompany
from openAIModule import aiProcess
from seleniumModule import seleniumScraper



#initialise web app
app = Flask(__name__)

# JSON template for company data to be stored in
companyJson="""{
    "company_name" : [{"value": "?", "source": "?"}],
    "type of product": [{"value": "?", "source": "?"}],
    "most popular product": [{"value": "?", "source": "?"}],
    "ceo ": [{"value": "?", "source": "?"}],
    "net profit ": [{"value": "?", "source": "?"}],
    "share price": [{"value": "?", "source": "?"}],
    "other_info": {
    "?"
    }
    "qualitative_info": {
    "?"
    }
  """
    
def validate_json(json_str):
    """Validate JSON string"""
    try:
        json_obj = json.loads(json_str)
        print("Json str valid")
        return json_obj
    except ValueError as e:
        print("Error: Invalid JSON format:", e)
        return None
    
#method to combine search results
def combine_articles(titleList,linkList, contentList):
        """Combine articles from lists of titles, links, and contents."""
        all_articles_string = ""
        count = 1
        for title,link, content in zip(titleList,linkList, contentList):  # Iterate through corresponding titles, links and contents
            article_string = f"Article {count}:\nTitle: {title}\nLink:\n{link}\nContent:\n{content}\n\n"
            all_articles_string += article_string
            count += 1
            return all_articles_string
        
#method to divide a string into ten substrings- for scraping web pages 
def split_string_into_ten(text):
  # Calculate the ideal length of each substring
  ideal_length = len(text) // 10
  # Initialize an empty list to store the substrings
  substrings = []
  # Start index for the current substring
  start_index = 0
  # Iterate until the entire string is divided
  while start_index < len(text):
    # Calculate the end index for the current substring
    end_index = min(start_index + ideal_length, len(text))
    # Extract the substring
    substring = text[start_index:end_index]
    # Add the substring to the list
    substrings.append(substring)
    # Update the start index for the next substring
    start_index = end_index

  return substrings

def coicopMarketAnalysis(company_name, all_data):
   """Perform market analysis based on COICOP."""
   description="unknown"
   #find the coicop of the product
   try:
    description=findCoicop(company_name,all_data)
   except:
    print("Error catagorising company") 
   
   #if the category is determined perform market searches
   if description!="unkown":
      #createing searches with the description 
      searchOne="top companies in the "+description+" market 2024"
      searchTwo="what is the most sold "+description+" 2024"
      searchThree=description+" market size 2024" 
      searchFour=description+" market analysis 2024"

      #perform the searches  
      ddgMarketSearches(searchOne, description)
      ddgMarketSearches(searchTwo, description)
      ddgMarketSearches(searchThree, description)
      ddgMarketSearches(searchFour, description)

   #return the description 
   return description
   

#------------------------------------------------------------------------------DuckDuckGO methods-------------------------------------------------------------------------------


def find_kpis(company_name):
  """method to find key performance indicators"""

  #creating search with company name
  search="site:finance.yahoo.com "+company_name
  linkList=ddgCalledMethod(search,10)
  #count as length of linkList
  count=len(linkList)

  json_to_find="""{
     "eps": ?,
     "shareprice" : ?
     "net profit" : ?,
     "customer acquisition cost" : ?,
     "share price" : ?,
     "current ratio" : ?,
     "turnover" : ?
    }
      """

  for x in range(count):
            try:
              #scrape every link that was found
              scrapedResults=linkList[x]
              #parse results with chatGPT
              prompt="Read the following text about "+ company_name +": "+scrapedResults+"and try and extract any important information that is in the example: "+json_to_find+ """then replace the question marks in the json with the answers that you find.
              If you cannot find the answer to any values replace the question marks with null. Please respond to this message with json format only."""
              #parse link's content with chatGPT 
              strWebResults=aiProcess(prompt)
              #cast data to json
              json_dataRed=json.loads(strWebResults)
              #insert to mongo
              mongoInsertDataMethod(json_dataRed,company_name)     
            except:
              print("An exception occurred")     

  return strWebResults


def ddgMarketSearches(search,marketName):
    """method to perform searches to find information about the market"""
    #scrape random web pages----------------------------------------------------------------------------------------------------------------------------
    #lists for the title content and link to webpages 
    linkList=altCalledMethod(search,1)

    exampleJson="""{
  "month": "Jan",
  "year": 2024,
  "top_brands": [
    {
      "brand": "Volkswagen UK",
      "sales": 11460
    },
    {
      "brand": "BMW",
      "sales": 10795
    },
    {
      "brand": "Kia Motors (UK)",
      "sales": 10207
    },
    {
      "brand": "Ford Motor Company",
      "sales": 9696
    },
    {
      "brand": "Audi",
      "sales": 8832
    }
  ]
}"""
    strWebResults=""  

    for link in linkList:
            try:
              #scrape every link that was found
              scrapedResults=seleniumScraper(link)
              #parse results with chatGPT
              PromptContentScrape="You are a market research analyst. Read the following website snippit and extract any useful information about the"+marketName+"industry :"+scrapedResults+"please respond using json format only. For example,"+exampleJson+"""
              but please also provide other pieces of information not given in the example. The goal here is to analalyse any information that would be useful about the given market."""
              #parse link's content with chatGPT 
              strWebResults=aiProcess(PromptContentScrape)
              #cast data to json
              json_dataRed=json.loads(strWebResults)
              #insert to mongo
              mongoInsertDataMethod(json_dataRed,marketName)     
            except:
              print("An exception occurred")     


def ddgCalledMethod(search, mRes):
  """method to make a ddg search convieniently"""
  linkList=[]
  count=0

  #ddg general search on the web
  with DDGS() as ddgs:
      for r in ddgs.text(search, region='uk-en', safesearch='off', timelimit='y', max_results=mRes):
          # Concatenate the text and add a newline for readability
          linkStr=r['href']
          linkList.append(linkStr)
          count+=1

  return linkList        

def altCalledMethod(search,mRes):
  """alternative to duckduckgo when rate limited"""
  task = Startpage()
  results = task.search(search)
  print(results[1])
  return results[:mRes]

    
#-------------------------------------Methods to collect data----------------------------------------
   
def webSearchCompleteJson(company_name):
    """method to handle an individual company """
    #scrape random web pages----------------------------------------------------------------------------------------------------------------------------
    #lists for the title content and link to webpages 
    linkList=altCalledMethod(company_name,5)

    #get global JSON
    global companyJson
    strWebResults=""  
        
    for link in linkList:
            try:
              #scrape every link that was found
              scrapedResults=seleniumScraper(link)
              #parse results with chatGPT
              PromptContentScrape="Act as a data extraction system. Read the following website text (from this link:+"+link+") and extract any useful information about "+company_name+":"+scrapedResults+"please respond using json format only. The following is the json template,"+companyJson+"""
              please respond to this using the json template ONLY. Fill in the question mark placeholders with the specific informaiton and source and insert any other information in the other_info section as a json object. For the source, do not just say website but actually include the 
              website that the information is found from. If you cannot find the specific information leave their values as unchanged. If the information
              has already been collected (i.e. has no question mark placeholder and has an entry containing value and source) you should add another entry in that piece of information's list of dictionaries, stating the value and the source. In the other info section do not replace anyting, instead extend 
              it to include the new other information that has been collected. Remember to respond only with Json, ensure the sytnax is correct, with no errors for example missing :s or }s."""
              #parse link's content with chatGPT 
              strWebResults=aiProcess(PromptContentScrape)
              print(strWebResults)
              companyJson=strWebResults  
            except:
              print("An exception occurred")     
   

def redditSearchQualitative(company_name):
    """method to fill in qualitative information from reddit"""
    #create search for company on reddit
    search="site:reddit.com"+company_name
    #lists for the title content and link to webpages 
    linkList=ddgCalledMethod(search,10)

    #get global JSON
    global companyJson
    strWebResults=""  

    for link in linkList:
            try:
              #scrape every link that was found
              scrapedResults=seleniumScraper(link)
              PromptContentScrape="Act as a qualitative research data extraction system. Read the following reddit text and extract any qualitative information about "+company_name+":"+scrapedResults+"""Reply
              to this message in json format only,  The following is the json template,"""+companyJson+"""please respond to this using the json template ONLY. Do not remove any of the existing data in the json template! Simply add any 
              qualitative information in the qualitative_info section and include the source it was found from (i.e. reddit user on reddit post). It is of utmost importance that you reply only in VALID JSON so ensure there are no errors in the response.
              """
              #parse link's content with chatGPT 
              strRedditResults=aiProcess(PromptContentScrape)
              companyJson=strRedditResults
            except:
              print("An exception occurred")      


#--------------------------------------Methods for guessing product type and most popular product--------------------------------
            
def productsMethod(company_name):
   """method that calls both of the methods and enters the value into the global JSON  """
   type="unknown"
   bseller="unknown"
   try:
      #calls methods to find type and best seller
      type=find_product_type(company_name)
      bseller=best_seller(company_name,type)  

      global companyJson
      # Parse the string into a dictionary
      dictCompanyJson = json.loads(companyJson)
      # Add the new values to the list with the specified source
      dictCompanyJson["type of product"].append({"value": type, "source": "product handling results"})
      dictCompanyJson["most popular product"].append({"value": bseller, "source": "product handling results"})
      # Convert the dictionary back to a string
      companyJson = json.dumps(companyJson)

   except:
      print("error finding products/product type") 
    
   return type


def find_product_type(company_name):
    """method to attempt to find what products a company sells"""
    products=[]
    confidence_scores=[]

    def splitResponse(response):
            try:
             product, conScore = response.split(", ")
             # Ensure numerical confidence score before appending
             score=int(conScore)
             products.append(product)
             confidence_scores.append(score)
            except Exception as e:
             print(f"Error processing ChatGPT response: {e}")

    #asking chatgpt normally-------------------------------------
    promptOne="What kind of products does this company sell and how confident are u on a scale of one to ten: "+ company_name+"? Respond with only the product in one word and then the confidence score seperated by a comma. For example : food, 7"
    try:
      responseOne=aiProcess(promptOne)
      splitResponse(responseOne)
    except:
        print("error manually asking chatGPT")

    #scaping official webiste then asking chatGPT----------------
    searchOne=company_name+"official website "
    officialSite=altCalledMethod(searchOne, 1)
    x=officialSite[0]
    officialBody=seleniumScraper(x)
    bodyInParts=split_string_into_ten(officialBody)
    
    for part in bodyInParts:
        try:
          promptTwo="Read the following text from the official web site and tell me what kind of products this company sells. Respond with only the product in one word and then provide a confidence score out of ten to show how certain you are that the company sells this product:" + part+"""
          respond with only the product in one word and then the confidence score seperated by a comma. For example : food, 7"""
          responseTwo=aiProcess(promptTwo)
          splitResponse(responseTwo)
        except:
            print("error parsing official website")

    #general search answers
    """answer_text=""
    with DDGS() as ddgs:
      for r in ddgs.answers(company_name):
        if 'text' in r:
            answer_text = r['text']
            break"""
    list=altCalledMethod(company_name,5)    
    for item in list:
      answer_text=seleniumScraper(item)
      promptThree="Read the following text from a general web search and tell me what kind of products this company sells. Respond with only the product in one word and then provide a confidence score out of ten to show how certain you are that the company sells this product:" + answer_text+"""
          respond with only the product in one word and then the confidence score seperated by a comma. For example : food, 7"""  
      try:
          resultsThree=aiProcess(promptThree)    
          splitResponse(resultsThree)
      except:
          print("error with general web search")    
  

 # Find highest confidence score
    if confidence_scores:
      highest_score_index = confidence_scores.index(max(confidence_scores))
      return products[highest_score_index]
    else:
       return None 


def best_seller(company_name, product):
  """method to attempt to find a companies most sold/ most popular product"""
  products=[]
  confidence_scores=[]

  def splitResponse(response):
            try:
             product, conScore = response.split(", ")
             # Ensure numerical confidence score before appending
             score=int(conScore)
             print(product)
             products.append(product)
             confidence_scores.append(score)
            except Exception as e:
             print(f"Error processing ChatGPT response: {e}")

    #asking chatgpt normally-------------------------------------
  promptOne="What is the most sold "+product+" that this company offers and how confident are u on a scale of one to ten: "+ company_name+"? Respond with only the product in one word and then the confidence score seperated by a comma. Do not include any other text/characters. For example : food, 7"
  try:
    responseOne=aiProcess(promptOne)
    splitResponse(responseOne)
  except:
    print("error manually asking chatGPT")

    #scaping official webiste then asking chatGPT----------------
    searchOne=company_name+"official website "
    officialSite=altCalledMethod(searchOne, 1)
    x=officialSite[0]
    officialBody=seleniumScraper(x)
    bodyInParts=split_string_into_ten(officialBody)
    
    for part in bodyInParts:
        try:
          promptTwo="Read the following text from the official web site and tell me what "+product+" from this company is the most popular/ most sold. Respond with only the product in one word and then provide a confidence score out of ten to show how certain you are that the company sells this product the most:" + part+"""
          respond with only the product in one word and then the confidence score seperated by a comma. Do not include any other text/characters. For example : food, 7"""
          responseTwo=aiProcess(promptTwo)
          splitResponse(responseTwo)
        except:
            print("error parsing official website")

    #general search answers
    search=company_name+"most sold "+ product
    """answer_text=""
    with DDGS() as ddgs:
      for r in ddgs.answers(search):
        if 'text' in r:
            answer_text = r['text']
            break"""
    list=altCalledMethod(search,5)
    for item in list:
      answer_text=seleniumScraper(item)
      promptThree="Read the following text from a general web search and tell me which "+product+" is the most sold. Also provide a confidence score out of ten to show how certain you are that the company sells this product:" + answer_text+"""
      respond with only the product in one word and then the confidence score seperated by a comma. Do not include any other text/characters. For example : food, 7"""  
      try:
          resultsThree=aiProcess(promptThree)    
          splitResponse(resultsThree)
      except:
          print("error with general web search")    
  
    #searching different web results
    linkList=altCalledMethod(search,10)
    for link in linkList:
        Body=seleniumScraper(link)
        bodyInPartsTwo=split_string_into_ten(officialBody)
        for part in bodyInPartsTwo:
          try:
            promptTwo="Read the following text from the web site and tell me what "+product+" from this company is the most popular/ most sold. Respond with only the product in one word and then provide a confidence score out of ten to show how certain you are that the company sells this product the most:" + part+"""
            respond with only the product in one word and then the confidence score seperated by a comma. Do not include any other text/characters. For example : food, 7"""
            responseTwo=aiProcess(promptTwo)
            splitResponse(responseTwo)
          except:
            print("error parsing website")
        

 # Find highest confidence score
    if confidence_scores:
      highest_score_index = confidence_scores.index(max(confidence_scores))
      return products[highest_score_index]
    else:
       return None 


#-------------------------------------Other methods
def resetcompanyJson():
   """method to reset the company json global variable"""
   global companyJson
   companyJson="""{
    "company_name" : [{"value": "?", "source": "?"}],
    "type of product": [{"value": "?", "source": "?"}],
    "most popular product": [{"value": "?", "source": "?"}],
    "ceo ": [{"value": "?", "source": "?"}],
    "net profit ": [{"value": "?", "source": "?"}],
    "share price": [{"value": "?", "source": "?"}],
    "other_info": {
    "?"
    }
    "qualitative_info": {
    "?"
    }
  """


def getCompanyJson(company_name):
    """method to call all of the methods to find and extract data into the JSON format"""
    resetcompanyJson()
    global companyJson
    webSearchCompleteJson(company_name)
    productType=productsMethod(company_name)
    description=coicopMarketAnalysis(company_name,companyJson)
  
    #validate correctness of json string
    newCompanyJson =validate_json(companyJson)
    mongoInsertDataMethod(newCompanyJson,description)

    return companyJson    


# Route for rendering the initial template
@app.route("/")
def index():
    
    return render_template("index.html")

#route for summary generation
@app.route("/Submit", methods=["POST"] )
def generate_data():
    #get company name from the user input
    company_name = request.form["company_name"]
    #generate a complete JSON object for this company
    jsonData=getCompanyJson(company_name)
    #return the JSON to the web page
    return render_template("index.html", data=jsonData)
    

#run the web app
if __name__ == "__main__":
    app.run()


