import requests
#access token for performing operation on user and owner account<<<<< used in the scope of basic, public_content, likes, comments.>>>>>
tokken_for_access_app = "1993495056.1b2b25a.bbdc1be8c2364ab181433835f5c37520"
                                                #url part commen in all urls
BASE_URL = "https://api.instagram.com/v1/"


def info_owner():                               #using get to collect owner information
    url_owner=BASE_URL+"users/self/?access_token="+tokken_for_access_app
    owner_info=requests.get(url_owner).json()
    print "\n\nowner id is "+owner_info["data"]['id']
    print "\nowner full name is "+owner_info["data"]["full_name"]
    print "\nowner bio is "+owner_info["data"]["bio"]
    print "\nowner usename is "+owner_info["data"]["username"]
    print "\n\n********************************************************************************************************************"
    return

def get_user_id_username(user_name):              #get user id
    if user_name  not in ['amritbirsingh345','yashika3990']:
        print"you enter wrong wrong username"
        return
    else:
        url_user=BASE_URL+"users/search?q="+user_name+"&access_token="+tokken_for_access_app#https://api.instagram.com/v1/users/search?q=jack&access_token=ACCESS-TOKEN
        user_info= requests.get(url_user).json()
        sucess = user_info["meta"]["code"]
        if sucess == 200:                          #checking url
            print "successsfully found user id "
        else:
            print "unsucsessfull plz try again"
        return user_info["data"][0]["id"]          #returning user id

#this funn is::: returning the post id :::on the bases of funn << get_user_by_user_name >>
def get_user_post_id(username):
    user_id1 = get_user_id_username(username)
    url_user1 = BASE_URL + "users/" + str(user_id1) + "/media/recent/?access_token=" + tokken_for_access_app  # https://api.instagram.com/v1/users/{user-id}/media/recent/?access_token=ACCESS-TOKEN
    request_for_user_to_get_all_post = requests.get(url_user1).json()
    sucess = request_for_user_to_get_all_post["meta"]["code"]
    for post_no in range(0,len(request_for_user_to_get_all_post["data"]),1): # traversingh all post id of user
        post_no
    exact_posts=str(post_no)                                                # variable contain the no of post in user id
    print 'we have total '+exact_posts+'posts of :'+username+'\n which post you want to chose'
    post_no=raw_input()
    i=int(post_no)
    if sucess == 200:
        print "successsfully found user id and fetched user's post id "
    else:
        print "unsucsessfull plz check user name again"
    return request_for_user_to_get_all_post["data"][i]['id']


#this funn is use to do like on users post_id which is getting from  funn <<<user_post_id>>>
def like_on_user_post_id(user_name):
    post_id = get_user_post_id(user_name)
    Access_token={'access_token':tokken_for_access_app}
    url_post_like= BASE_URL+"media/"+post_id+"/likes"
    like_result=requests.post(url_post_like,Access_token).json()
    sucess = like_result["meta"]["code"]
    if sucess == 200:                                                           # checking url
        print "successsfully liked the pic "
        return
    else:
        print "unsucsessfull plz try again"
        return


def comment_on_user_id(user_name):
    post_id = get_user_post_id(user_name)  # post_id which is getting from  funn <<<user_post_id>>>
    print "write comment u want to write \n but rules are \n 1. The total length of the comment cannot exceed 300 characters.\n 2. The comment cannot contain more than 4 hashtags.\n 3. The comment cannot contain more than 1 URL.\n 4. The comment cannot consist of all capital letters."
    entered_comment = raw_input()           #getting comment which user want to write on post
    entered_comment = str(entered_comment)
    url_post_comment = BASE_URL + "media/"+post_id+"/comments"
    Access_token_Plus_comment = {'access_token': tokken_for_access_app, 'text': entered_comment}
    comment_result = requests.post(url_post_comment, Access_token_Plus_comment).json() #posting comment on pic
    sucess = comment_result["meta"]["code"]
    if sucess == 200:  # checking url
        print "successsfully commented on the pic "
        return
    else:
        print "unsucsessfull plz try again"
        return


def search_comment_id(user_name): # is using for searching a perticular comment of user choice
    post_id=get_user_post_id(user_name)
    print "type content related to comment"
    search=raw_input()                          #getting comment which user want to search on post
    recent_comments=BASE_URL+"media/"+post_id+"/comments?access_token="+tokken_for_access_app
    recent_comments=requests.get(recent_comments).json()
    for i in range (0,len (recent_comments["data"]),1):     #traversing though all comments of that post
        if search in recent_comments['data'][i]['text']:    #checking is that commnet in post is match to user content or not
            print "comment is found ::"
            print recent_comments ['data'][i]['text']
            return recent_comments['data'][i]['id'],post_id
    print "comment is not found"
    return 112,3

def delete_comment(user_name):
        comment_id,media_id = search_comment_id(user_name)
        #https://api.instagram.com/v1/media/1486120579122616804_2338013941/comments/17876833795018201?access_token=1993495056.1b2b25a.bbdc1be8c2364ab181433835f5c37520
        sucess1 = BASE_URL+"media/"+str(media_id)+"/comments/"+str(comment_id)+"?access_token="+tokken_for_access_app
        sucess=requests.delete(sucess1).json()

        if sucess == 200:  # checking url
            print "successsfully deleted the commented on the pic "
            return
        else:
            print "unsucsessfull plz try again"
            return



def find_average(post_id):
    no_of_words = 0
    list_of_comments = []
    comment_id = []
    url =BASE_URL+"media/"+str(post_id)+"/comments/?access_token="+tokken_for_access_app
    data = requests.get(url).json()
    if len(data['data']) == 0:
        print("no comments on this post")
        return
    else:
        for comment in data['data']:
            list_of_comments.append(comment['text']) #making a list if comments
            #print list_of_comments
            no_of_words += len(comment['text'].split())# calculating words in comment without counting spaces
            #print no_of_words
        average_words = float(no_of_words)/len(list_of_comments)
        print("\nAverage on the post = %.2f" % average_words)
        return

Variable1 ="y"
while Variable1 =="y":
    info_owner()                                            # calling funn to print owner information
    print"hey type the username from following \n  amritbirsingh345  \n  yashika3990 "
    user_name = raw_input()
    print"select what do you want to do 1:like 2:comment 3:search 4:delete 5:avrage og words of comment on post"         #choice what user want to do
    choice=raw_input()
    if choice=="1":
        like_on_user_post_id(user_name)                     #for like a pic
    elif choice=="2":
        comment_on_user_id(user_name)                       #comment on pic
    elif choice=="3":
        search_comment_id(user_name)                        #searching commnet on pic
    elif choice== '4':
        delete_comment(user_name)                  #deleting comment on pic
    elif choice =='5':
        find_average(get_user_post_id(user_name)) #finding average
    else:
        print"you chose wrong"

    print" press any key for exit or press y to continue "  #choice he want to do again or not
    Variable1=raw_input()
print "******************************************** thanx for using this **********************************************************"