# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 12:29:41 2020

@author: niket
"""


def web(link,loc):
    import webbrowser
    link=link.lower()
    link=link.replace(" ","")
    link=link.replace("###@###NA###@###","")
    if(link=='youtube'):
        webbrowser.open('https://www.youtube.com/?gl=IN')
    elif(link=='youtubemovies' or link=='music'):
        webbrowser.open('https://www.youtube.com/channel/UClgRkhTL3_hImCAmdLfDE4g')
    elif(link=='youtubemovies' or link=='movies'):
        webbrowser.open('https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ')
    elif(link=='wiipedia'):
        webbrowser.open('https://www.wikipedia.org')
    elif(link=='google'):
        webbrowser.open('https://www.google.co.in')   
    else:
        webbrowser.open(link)
        
class PyWeb:
    '''
    loc->location of csv file.
    link->name of sile given by user
    Mlink->Modified link with no spaces and uppercase letter
    browser->Browswr of choice
    '''
    def __init__(self,loc,link,browser='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'):
        Mlink=link.lower()
        Mlink=Mlink.replace(" ","")
        self.loc=loc
        self.Mlink=Mlink
        self.link=link
        self.browser=browser
        
    def start(self):
        from webbrowser import open_new_tab as webopen
        from webbrowser import get as webget
        from pandas import read_csv
        webget(self.browser)
        data=read_csv(self.loc)
        SiteName=data.iloc[:,0].values
        SiteAddress=data.iloc[:,1].values
        num=0                                                           #Variable to store index of site.
        while(SiteName[num]!=self.Mlink and (num+1)<len(SiteName)):     #Finding site name in stored links.
            num+=1
        if(SiteName[num]==self.Mlink):
            webopen(SiteAddress[num])
        else:
            webopen(self.link)
        return True
    
    def add(self,SiteAddress):
        from csv import writer
        with open(self.loc,mode='a+',newline="") as file:
            csv_writter=writer(file)
            csv_writter.writerows([list([self.Mlink,SiteAddress])])
            return True
        
    def remove(self):
        from pandas import read_csv
        from numpy import delete
        from csv import writer
        data=read_csv(self.loc)
        SiteData=data.iloc[:,:].values
        num=0                                                              #Variable to store index of site.
        while(SiteData[num][0]!=self.Mlink and (num+1)<len(SiteData)):     #Finding site name in stored links.
            num+=1
        if(SiteData[num][0]==self.Mlink):
            SiteData=delete(SiteData,num,axis=0)
            with open(self.loc,mode='w') as file:
               csv_writter=writer(file)
               csv_writter.writerows(SiteData)
               return True 
            
    def show(self):
        from pandas import read_csv
        data=read_csv(self.loc)
        SiteData=data.iloc[:,:].values
        return SiteData
        
    
class PyWiki:
   def __init__(self,Text):
       self.text=Text
       
   def Summary(self):
       from wikipedia import summary
       return summary(self.text)
   
   def Search(self):
       from wikipedia import search
       return search(self.text)
   
class PyWikiPage:
       def __init__(self,text):
           from wikipedia import page
           self.page=page(text)
           
       def Title(self):
           return self.page.title
       
       def Content(self):
           data= self.page.content
           data=data.replace("====","")
           data=data.replace("===","")
           data=data.replace("\n\n\n==","#=#Heading#=#")
           data=data.replace("==","#=#HeadingData#=#")
           data=data.split("#=#Heading#=#")
           data=[_.split("#=#HeadingData#=#") for _ in data]
           DataDictonary={}
           DataDictonary["Introduction"]=data[0][0]
           for _ in range(1,len(data)):
               DataDictonary[data[_][0]]=data[_][1]
        
