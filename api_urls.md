<!-- GET all user questions -->
http://127.0.0.1:8000/api/user_question_list
Token: 77b1dff1442d4c67f250dc34dad55bd500b3f04b 
# this token is for user 1 admin btw
# "username": "admin",
# "password": "admin"

<!-- GET all user answer -->
http://127.0.0.1:8000/api/user_answer_list


<!-- GET all questions -->
http://127.0.0.1:8000/api/answer


<!-- GET all answer -->
http://127.0.0.1:8000/api/question


<!-- GET all users -->
http://127.0.0.1:8000/api/user


<!-- POST api auth token login -->
http://127.0.0.1:8000/api/auth/token/login


<!-- GET one question and one answer depending on what is put in for the <int:pk> value -->
http://127.0.0.1:8000/api/<int:pk>/question_answer_detail


<!-- GET one answer depending on what is put in for the <int:pk> value -->
http://127.0.0.1:8000/api/<int:pk>/answer_detail


Token: 626481b0af41ae56e4d9aac90c04bf975fe7adcc
# this token is for user 2 paul btw
# "username": "paul",
# "password": "paulcool"