import requests
def summerize(text):
    url = "https://meaningcloud-summarization-v1.p.rapidapi.com/summarization-1.0"
    
    
    querystring = {"sentences":"5","txt":text}
    
    headers = {
    	"Accept": "application/json",
    	"X-RapidAPI-Key": "d9a0010e14msh5e78521fbc6ae2cp17d668jsn8ea8177100e4",
    	"X-RapidAPI-Host": "meaningcloud-summarization-v1.p.rapidapi.com"
    }
    
    response = requests.request("GET", url, headers=headers, params=querystring)

    return [line.strip() for line in response.json().get("summary").split("[...]")]








































# God of this code : Ankur Shukla