import requests
from typing import Dict
global auth
class SMAPI:
    
    def __init__(self, username, password, url):
        self.username = username
        self.password = password
        self.url = url
    

    def auth(self):
        global auth 
        authurl = f"{self.url}/api/v1/auth/authenticate-user" 
        myobj = {'username': self.username, 'password':self.password} 
        data = requests.post(authurl, data = myobj) # this posts the username and password to the api
        #print(data.json())
        refreshToken = data.json()['refreshToken'] # this is the refresh token
        accessToken = data.json()['accessToken'] # this is the access token
        accessTokenExpiration = data.json()['accessTokenExpiration'] # this is the access token expiration date
        access_info = {'accessToken': accessToken, 'accessTokenExpiration': accessTokenExpiration, 'refreshToken': refreshToken} # this is the access token, refresh token and expiration info
        auth = access_info['accessToken'] # this is the access token
        
    @property
    def header(self) -> Dict[str,str]:
        global auth
        return {'Authorization' : f'Bearer {auth}'}


    def GetUser(self,input_email):

        url = f"{self.url}/api/v1/settings/domain/user/{input_email}"
        

        myobjs = {""}
        x = requests.get(url, headers = self.header)
        return(x.json())
    
    
    def GetDomain(self):

        url = f"{self.url}/api/v1/settings/domain/data"
        

        myobjs = {""}
        x = requests.get(url, headers = self.header)
        return(x.json())
        
    def GetDomainPermissions(self):

        url = f"{self.url}/api/v1/settings/domain/permissions"
        

        myobjs = {""}
        x = requests.get(url, headers = self.header)
        return(x.json())
        
    def GetTotalDomainUsers(self):

        url = f"{self.url}/api/v1/settings/domain/total-server-users"
        

        myobjs = {""}
        x = requests.get(url, headers = self.header)
        return(x.json())
        
    def GetAlias(self,aliasname):

        url = f"{self.url}/api/v1/settings/domain/alias/{aliasname}"
        

        myobjs = {""}
        x = requests.get(url, headers = self.header)
        return(x.json())
        
    def DomainAccountListCount(self):

        url = f"{self.url}/api/v1/settings/domain/account-list-counts"
        

        myobjs = {""}
        x = requests.get(url, headers = self.header)
        return(x.json())
        
    def SystemDomainDetails(self,input_domain):

        url = f"{self.url}/api/v1/settings/sysadmin/domain/{input_domain}"

        myobjs = {""}
        x = requests.get(url, headers = self.header)
        return(x.json())   


    def SystemExportDomainsList(self):

        url = f"{self.url}/api/v1/settings/sysadmin/export-domains-list"
        

        myobjs = {""}
        x = requests.post(url, headers = self.header)
        x.encoding = x.apparent_encoding
        return(x.text)


    def SystemExportDomainsListToFile(self,filename):

        url = f"{self.url}/api/v1/settings/sysadmin/export-domains-list"
        

        myobjs = {""}
        x = requests.post(url, headers = self.header)
        x.encoding = x.apparent_encoding
        try:
            file = open(filename, "x")
        except:
            pass
        file = open(filename, "w")
        file.write("%s = %s\n" %("x", x.text))

        file.close()
        return(x.text)           
        
    def GetAllMailingLists(self):

        url = f"{self.url}/api/v1/settings/domain/mailing-lists/list"
        

        myobjs = {""}
        x = requests.get(url, headers = self.header)
        return(x.json())
        
        
    def RemoveSubscribersMailingList(self,input_mailingListId,email):

        url = f"{self.url}/api/v1/settings/domain/mailing-lists/{input_mailingListId}/subscriber-remove"
        

        myobjs = {"data":email}
        x = requests.post(url, data = myobjs, headers = self.header)
        x.encoding = x.apparent_encoding
        return(x.text)
        
        
        
    def AddBannedUserMailingList(self,input_mailingListId,email):

        url = f"{self.url}/api/v1/settings/domain/mailing-lists/{input_mailingListId}/banned-user-add"
        

        myobjs = {"data":email}
        x = requests.post(url, data = myobjs, headers = self.header)
        x.encoding = x.apparent_encoding
        return(x.text)
        
        
    def AddDigestSubscribers(self,input_mailingListId,email):

        url = f"{self.url}/api/v1/settings/domain/mailing-lists/{input_mailingListId}/digest-subscriber-add"
        

        myobjs = {'data':email}
        x = requests.post(url, data = myobjs, headers = self.header)
        x.encoding = x.apparent_encoding
        return(x.text)
        
        
    def RemoveSubscribersMailingListALL(self,input_mailingListId):

        url = f"{self.url}/api/v1/settings/domain/mailing-lists/{input_mailingListId}/subscriber-remove-all"
        

        #myobjs = {"data":email}
        x = requests.post(url,  headers = self.header)
        x.encoding = x.apparent_encoding
        return(x.text)
        
        
    def EditSubscriberMailinglists(self,input_subscriberEmail,input_mailingListId,input_mailingListId2):

        url = f"{self.url}/api/v1/settings/domain/mailing-lists/subscribers/{input_subscriberEmail}/edit/{input_mailingListId}"
        

        myobjs = {'subscribedLists':"input_mailingListId2"}
        x = requests.post(url, data = myobjs, headers = self.header)
        x.encoding = x.apparent_encoding
        return(x.text)
        
        
    def GetSubscriberMailingList(self,input_mailingListId,input_subscriberEmail):

        url = f"{self.url}/api/v1/settings/domain/mailing-lists/subscribers/{input_subscriberEmail}/{input_mailingListId}"
        

        myobjs = {""}
        x = requests.get(url, headers = self.header)
        return(x.json())
        
        
        
         
    def OptInUser(self,input_data,input_post):

        url = f"{self.url}/api/v1/settings/domain/mailing-lists/optin/{input_data}"
        

        myobjs = {"data":input_post}
        x = requests.post(url, data = myobjs, headers = self.header)
        return(x.json())
        
        
        
        
    def OptInUser(self,input_data,input_post):

        url =  f"{self.url}/api/v1/settings/domain/mailing-lists/optin/{input_data}"
        

        myobjs = {"data":input_post}
        x = requests.post(url, data = myobjs, headers = self.header)
        return(x.json())
        
        
        
    def RemoveDigestSubscribers(self,input_mailingListId,sub_email):
    
        url = f"{self.url}/api/v1/settings/domain/mailing-lists/{input_mailingListId}/digest-subscriber-remove"
        

        myobjs = {"data":sub_email}
        x = requests.post(url, data = myobjs, headers = self.header)
        return(x.json()) 


    def AddDigestSubscribers(self,input_mailingListId,sub_email):
    
        url = f"{self.url}/api/v1/settings/domain/mailing-lists/{input_mailingListId}/digest-subscriber-add"
        

        myobjs = {"data":sub_email}

        x = requests.post(url, data = myobjs, headers = self.header)
        return(x.json())
        
        
    def RemoveDigestSubscribersALL(self,input_mailingListId):
    
        url = f"{self.url}/api/v1/settings/domain/mailing-lists/{input_mailingListId}/digest-subscriber-remove-all"
        

        #myobjs = {"data":sub_email}

        x = requests.post(url, headers = self.header)
        return(x.json())      
        
    def SendMessage(self,email_from,email_to,subject,body):

        url = f"{self.url}/api/v1/mail/message-put"
        

        myobjs = {"from":email_from,"subject":subject,"to":email_to,"messagePlainText":body}

        x = requests.post(url, data = myobjs, headers = self.header)
        x.encoding = x.apparent_encoding
        return(x.text)
    
    def RestoreFolders(self,folder,email,recursive):
    
        url = f"{self.url}/api/v1/settings/sysadmin/restore-folders"
        

        myobjs = {"restorations":[{'folder':folder,'email':email,'recursive':recursive}]}


        x = requests.post(url, json = myobjs, headers = self.header)
        x.encoding = x.apparent_encoding
        return(x.text)
        
        
    def GetUserFolder(self,folder):

        url = f"{self.url}/api/v1/folders/folder"
        

        myobjs = {'folder':folder}


        x = requests.post(url, json = myobjs, headers = self.header)
        x.encoding = x.apparent_encoding
        return(x.text)
        
    def ListMailFoldersUsers(self):
        url = f"{self.url}/api/v1/folders/list-email-folders"
        

        #myobjs = {'folder':folder}

        x = requests.get(url, headers = self.header)
        x.encoding = x.apparent_encoding
        return(x.text)
        
        
        
    def SystemadminImpersonateUser(self,email):
        
        global auth
        url = f"{self.url}/api/v1/settings/domain/impersonate-user/{email}"
        
        myobjs = {'email':email}

        x = requests.post(url, json = myobjs, headers = self.header)
        x.encoding = x.apparent_encoding
        x = x.text
        x = x.replace("true", '''"true"''')
        x = x.replace("null", '''"null"''')
        x = eval(x)
        auth = x['impersonateAccessToken']
        return(auth)
        
        
        
    def GetDomainAdmins(self,domain):
    
        url = f"{self.url}/api/v1/settings/sysadmin/domain-admins/{domain}"      

        myobjs = {"domain":domain}

        x = requests.get(url, json = myobjs, headers = self.header)
        x.encoding = x.apparent_encoding
        return(x.text)
        
        
    def ListUsersDomain(self):
    
        url = f"{self.url}/api/v1/settings/domain/list-users"
        

       # myobjs = {"domain":domain}

        x = requests.get(url, headers = self.header)
        x.encoding = x.apparent_encoding
        return(x.text)
        
        
    def EditFolderUser(self,folder,newFolder):
    
        url = f"{self.url}/api/v1/folders/folder-patch"
        

        myobjs = {"newFolder":newFolder,"folder":folder}

        x = requests.post(url,json = myobjs ,headers = self.header)
        x.encoding = x.apparent_encoding
        return(x.text)
        
