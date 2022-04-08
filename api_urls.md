<!-- GET all user questions -->
https://dj-questionbox.herokuapp.com/api/user_question_list
Token: 77b1dff1442d4c67f250dc34dad55bd500b3f04b 
# this token is for user 1 admin btw
# "username": "admin",
# "password": "admin"

<!-- GET all user answer -->
https://dj-questionbox.herokuapp.com/api/user_answer_list


<!-- GET all questions -->
https://dj-questionbox.herokuapp.com/api/answer


<!-- GET all answer -->
https://dj-questionbox.herokuapp.com/api/question


<!-- GET all users -->
https://dj-questionbox.herokuapp.com/api/user


<!-- POST api auth token login -->
https://dj-questionbox.herokuapp.com/api/auth/token/login

<!-- POST api auth token logout -->
https://dj-questionbox.herokuapp.com/api/auth/token/logout


<!-- GET one question and one answer depending on what is put in for the <int:pk> value -->
https://dj-questionbox.herokuapp.com/api/<int:pk>/question_answer_detail


<!-- GET one answer depending on what is put in for the <int:pk> value -->
https://dj-questionbox.herokuapp.com/api/<int:pk>/answer_detail


Token: 626481b0af41ae56e4d9aac90c04bf975fe7adcc
# this token is for user 2 paul btw
# "username": "paul",
# "password": "paulcool"

# Backend Questionbox Documentation

## Models

- **Question**
    - Fields
      - : TextField
      - question: TextField
      - created_at: DateTimeField
      - user: FK
      - favorited: M2M
- **Answer**
    - Fields
      - answer: CharField
      - questions: FK
      - answer_at: DateTimeField
      - user: FK
      - favorited: M2M
<h1> Register a new user

### Endpoints

| Method | URL           | Description                                    | Notes |
|--------|---------------|------------------------------------------------|-|
| POST   | /question/    | create a new question   ||
| GET    | /question/:Q_id/   | returns a question with all the answers answers                   |slug/pk later?|
| PATCH  | /question/:Q_id/   | edit an existing question   ||
| DELETE | /question/:Q_id/   | edit an existing question   ||
| GET    | /questions/   | get a list of all questions                    ||
| GET    | /questions/:user_id/ | get a list of all questions the user has posted |slug/pk later?|
| GET    | /answers/ | return all the answers a user has given as well as the question they were to  ||
| GET    | /favorites/ | retrieve all favorites            ||
| GET    | /favorite/questions | retrieve all favorited questions            ||
| GET    | /favorite/answers | retrieve all favorited answers            ||


## Register a new user

### request

Username and password are required.

```
POST api/auth/users/

{
  "username": "emma",
  "password": "badpassword"
}
```

### response

```
201 Created

{
  "email": "",
  "username": "emma",
  "id": 3
}

```

## Log In

### request

```
POST api/auth/token/login

{
  "username": "admin",
  "password": "badpassword"
}
```

### response

```json
{
  "auth_token": "11b22b7796e3c1c7079b074c46a0cc137ce8b412"
}
```




## List all questions 

Requires authentication.

### request

```
GET api/question
```

### response

```json
[
	{
		"id": 2,
		"user": "admin",
		"question": "What is my favorite color?",
		"favorited": [
			2
		],
		"created_at": "2022-04-07T20:11:14.668474Z"
	},
	{
		"id": 1,
		"user": "admin",
		"question": "What is my dogs name?",
		"favorited": [
			2
		],
		"created_at": "2022-04-07T20:09:35.317679Z"
	}
]
```

## List all answers 

Requires authentication.

### request

```txt
GET api/answer
```

### response

```json
[
	{
		"id": 1,
		"user": "admin",
		"answer": "My dog name is Crowley.",
		"questions": 1,
		"favorited": [
			2
		],
		"answered_at": "2022-04-07T20:09:59.028817Z"
	},
	{
		"id": 3,
		"user": "admin",
		"answer": "another name he has is scuttle butt",
		"questions": 1,
		"favorited": [
			2
		],
		"answered_at": "2022-04-07T20:10:44.846454Z"
	},
	{
		"id": 4,
		"user": "admin",
		"answer": "Green",
		"questions": 2,
		"favorited": [
			2
		],
		"answered_at": "2022-04-07T20:11:38.500711Z"
	},
	{
		"id": 2,
		"user": "admin",
		"answer": "he also goes by crow bow",
		"questions": 1,
		"favorited": [],
		"answered_at": "2022-04-07T20:10:20.671853Z"
	},
	{
		"id": 5,
		"user": "admin",
		"answer": "Green/blue",
		"questions": 2,
		"favorited": [],
		"answered_at": "2022-04-07T20:11:57.694383Z"
	}
]
```

## List all user answers 

Requires authentication.

### request

```txt
GET api/user_answer_list
```

### response

```json
[
	{
		"id": 1,
		"user": "admin",
		"answer": "My dog name is Crowley.",
		"questions": 1,
		"favorited": [
			2
		],
		"answered_at": "2022-04-07T20:09:59.028817Z"
	},
	{
		"id": 2,
		"user": "admin",
		"answer": "he also goes by crow bow",
		"questions": 1,
		"favorited": [],
		"answered_at": "2022-04-07T20:10:20.671853Z"
	},
	{
		"id": 3,
		"user": "admin",
		"answer": "another name he has is scuttle butt",
		"questions": 1,
		"favorited": [
			2
		],
		"answered_at": "2022-04-07T20:10:44.846454Z"
	},
	{
		"id": 4,
		"user": "admin",
		"answer": "Green",
		"questions": 2,
		"favorited": [
			2
		],
		"answered_at": "2022-04-07T20:11:38.500711Z"
	},
	{
		"id": 5,
		"user": "admin",
		"answer": "Green/blue",
		"questions": 2,
		"favorited": [],
		"answered_at": "2022-04-07T20:11:57.694383Z"
	}
]
```