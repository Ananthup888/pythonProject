from blogapplication.models import users,blogs
#print((len(users)))
#q1 most liked post
#trending_post=max(blogs,key=lambda  blog:len(blog.get("liked_by")))
#print(trending_post)

#q2 which user has the lowestnumber of follwing
#least_following=min(users,key=lambda u:len(u.get("following")))
#print(least_following)

#q3 list allpost of a specific user
#post_filter=[post for post in blogs if post.get("userId")==2]
#print(post_filter)

#q4 followers of a specific user
#userid =1
#user_followers=[user.get("username")for user in users if userid in user.get("following")]
#print(user_followers)

#q5 authentication
# uname="akhil"
# password="Password@123"
# user=[u for u in users if u.get("username")==uname and u.get("password")==password]
# if len(user)>0:
#     print("login success")
# else:
#     print("invalid login")

#q6 which user uploaded most number of posts
#
# blog_count={}
# for blog in blogs:
#     user_id=blog.get("userId")
#     user_name =[user.get("username") for user in users if user.get("id") == user_id].pop()
#     if user_name in blog_count:
#         blog_count[user_name]+=1
#     else:
#         blog_count[user_name]=1
# print(blog_count)
# a_user=max(blog_count,key=lambda k:blog_count[k])
# print(a_user)

#q7 most active user
# liked_count={}
# for blog in blogs:
#     liked_users=blog.get("liked_by")
#     for user in liked_users:
#         if user in liked_count:
#             liked_count[user]+=1
#         else:
#             liked_count[user]=1
# print(liked_count)
# ac_user=max(liked_count,key=lambda k:liked_count[k])
# print([user.get("username") for user in users if user.get("id")==ac_user].pop())

#q8 sort users along with following count (ascending order)
# users.sort(key=lambda  u:len(u.get("following")))
# print(users)

#q9 sort users along with following count (decending order)
# users.sort(key=lambda  u:len(u.get("following")),reverse=True)
# print(users)

#q10 follow suggesions
loged_user=1
all_users=[user.get('id') for user in users]
all_users.remove(loged_user)
print(all_users)
loged_user_following=[user.get('following') for user in users if user.get("id")==loged_user].pop()
print(loged_user_following)
print(set(all_users)-set(loged_user_following))
