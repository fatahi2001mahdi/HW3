class SocialMedia:
    def __init__(self, name: str):
        self.__name = name
        self.__post_list = []
        
    def getName(self):
        return self.__name
        
    def getMessages(self):
        return self.__post_list
        
    def setMessages(self, post: str):
        self.__post_list.append(post)


class Twitter(SocialMedia):
    def __init__(self):
        super().__init__("Twitter")
    
    def getTwitts(self):
        return super().getMessages()
        
    def createNewTweet(self, post: str):
        if len(post)<280:    
            super().setMessages(post)


class Instagram(SocialMedia):
    def __init__(self):
        super().__init__("Instagram")
    
    def publishNewPost(self, post: str):
        if len(post)<2200:
            super().setMessages(post)
            
    def getPosts(self):
        return super().getMessages()
             
        
def show_all_posts(social_media_list: list):
    for social_media in social_media_list:
        social_media_name = social_media.getName()
        
        if social_media_name == "Instagram":
            print(social_media_name, ": ", social_media.getPosts())
        elif social_media_name == "Twitter":
            print(social_media_name, ": ", social_media.getTwitts())
    
social_posts = []
social_posts.append(Instagram())
social_posts.append(Twitter())

social_posts[0].publishNewPost("Hi. My name is Mahdi Fatahi and this is my first post on instagram.")
social_posts[1].createNewTweet("Hi. My name is Mahdi Fatahi and this is my first twitt")
social_posts[1].createNewTweet("Length is more than 280 abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz")
social_posts[1].createNewTweet("This is my second twitt")

show_all_posts(social_posts)