import streamlit as st
import requests
z = []
url = "https://microsoft-computer-vision3.p.rapidapi.com/ocr"
languages = ["unk","zh-Hans","zh-Hant","cs","da","nl","en","fi","fr","de","el","hu","it","ja","ko","nb","pl","pt","ru","es","sv","tr","ar","ro","sk"]
l = st.selectbox("Enter the language code. (unk is English and will be chosen by default.) For references on this, visit [this Wikipedia article.](https://en.wikipedia.org/wiki/IETF_language_tag)",languages)
querystring = {"detectOrientation":"true","language":l}
r = st.text_input("Enter the URL of the image. Keep in mind the image detection is still in beta and may give irrelevant results or make mistakes.","")

q = st.button("Submit")
payload = { "url": r }
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "ac63395f44mshe662342fb3bed36p114c3bjsn7421be01ca90",
	"X-RapidAPI-Host": "microsoft-computer-vision3.p.rapidapi.com"
}
if(q):
    response = requests.post(url, json=payload, headers=headers, params=querystring)
    g = response.json()['regions']
    for x in range(len(g[0]['lines'])):
        for y in range(len(g[0]['lines'][x]['words'])):
            z.append(g[0]['lines'][x]['words'][y]['text'])
            #print(g[0]['lines'][x]['words'][y]['text'])
    #print(g[0]['lines'][0]['words'])
    #print(" ".join(z))
    st.write(" ".join(z))




    