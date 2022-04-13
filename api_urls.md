
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

## Login

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

## Logout

### request

```
POST api/auth/token/logout

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

## List all user questions 


Requires authentication.

### request

```txt
GET api/user_q_list
```

### response

```json
[
	{
		"id": 1,
		"user": "admin",
		"question": "What is your dogs name?",
		"favorited": [
			1
		],
		"created_at": "2022-04-05T18:20:14.912272Z"
	},
	{
		"id": 2,
		"user": "admin",
		"question": "Who is Gamora?",
		"favorited": [
			1
		],
		"created_at": "2022-04-05T18:20:58.309005Z"
	},
	{
		"id": 6,
		"user": "admin",
		"question": "What is your cat name?",
		"favorited": [
			1
		],
		"created_at": "2022-04-08T14:11:06.293625Z"
	},
	{
		"id": 7,
		"user": "admin",
		"question": "What is your bird name?",
		"favorited": [],
		"created_at": "2022-04-08T19:17:00.463150Z"
	}
]
```

## List all user favorited questions  

Requires authentication.

### request

```txt
GET api/user_favorited_q_list
```

### response

```json
[
	{
		"id": 1,
		"user": "admin",
		"question": "What is your dogs name?",
		"favorited": [
			1
		],
		"created_at": "2022-04-05T18:20:14.912272Z"
	},
	{
		"id": 2,
		"user": "admin",
		"question": "Who is Gamora?",
		"favorited": [
			1
		],
		"created_at": "2022-04-05T18:20:58.309005Z"
	},
	{
		"id": 6,
		"user": "admin",
		"question": "What is your cat name?",
		"favorited": [
			1
		],
		"created_at": "2022-04-08T14:11:06.293625Z"
	}
]
```

## List all user answers  


Requires authentication.

### request

```txt
GET api/user_a_list
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


## List all user accepted answers 

Requires authentication.

### request

```txt
GET api/user_accepted_a_list
```

### response

```json
[
	{
		"id": 11,
		"user": "admin",
		"answer": "He also goes by pups McGee.",
		"questions": 1,
		"accepted": 1,
		"favorited": [],
		"answered_at": "2022-04-11T12:51:47.917048Z"
	},
	{
		"id": 12,
		"user": "admin",
		"answer": "He also goes by pupperino.",
		"questions": 1,
		"accepted": 1,
		"favorited": [
			1
		],
		"answered_at": "2022-04-11T12:52:24.847807Z"
	}
]
```

## List all user accepted favorited answers  

Requires authentication.

### request

```txt
GET api/user_a_favorited_a_list
```

### response

```json
[
	{
		"id": 12,
		"user": "admin",
		"answer": "He also goes by pupperino.",
		"questions": 1,
		"accepted": 1,
		"favorited": [
			1
		],
		"answered_at": "2022-04-11T12:52:24.847807Z"
	}
]
```

## List one question and all answers to it

Requires authentication.

### request

Requires authentication.

```
GET api/question/<int:pk>/answers

```

### respons
```

{
	"id": 3,
	"user": "paul",
	"question": "whats your favorite color?",
	"answers": [
		{
			"id": 3,
			"user": "paul",
			"answer": "Green",
			"questions": 3,
			"favorited": [],
			"answered_at": "2022-04-06T22:12:01.827699Z"
		},
		{
			"id": 7,
			"user": "paul",
			"answer": "green/blue",
			"questions": 3,
			"favorited": [
				2
			],
			"answered_at": "2022-04-07T16:44:14.945693Z"
		}
	]
}
```

## Create a new question

Requires authentication.

### request

`question` are required fields.

```
POST api/user_q_list

{
   "question": "What is your bird name?",
   "favorited": []
}
```

### response

```
201 Created

{
	"id": 7,
	"user": "admin",
	"question": "What is your bird name?",
	"favorited": [],
	"created_at": "2022-04-08T19:17:00.463150Z"
}

```

## Create a user favorited question  

Requires authentication.

### request

`question` and `favorited` are required fields.

```
POST api/user_favorited_q_list

{
   "question": "What is your snakes name?",
   "favorited": [1]
}
```

### response

```
201 Created

{
		"id": 8,
		"user": "admin",
		"question": "What is your snakes name?",
		"favorited": [
			1
		],
		"created_at": "2022-04-08T19:34:01.290543Z"
	}

```

## Create a user answer

Requires authentication.

### request

`answer` and `questions` are required fields.

```
POST api/user_a_list

{
   "answer": "Sunny",
   "questions": 1
   "favorited": []
}
```

### response

```
201 Created

{
	"id": 9,
	"user": "admin",
	"answer": "Sunny",
	"questions": 1,
	"favorited": [],
	"answered_at": "2022-04-08T20:24:32.332402Z"
}

```

## Create an accepted answer

Requires authentication.

### request

`answer` and `questions` `accepted` `favorited`are required fields.

```
POST api/user_accepted_a_list

{
   "answer": "Sunny",
   "questoins": 1, 
   "accepted": 1, 
   "favorited": []
}
```

### response

```
201 Created

{
	"id": 10,
	"user": "admin",
	"answer": "jingles",
	"questions": 1,
    "accepted": 1,
	"favorited": [],
	"answered_at": "2022-04-08T20:31:56.477966Z"
}

```

## Create an accepted favorited answer

Requires authentication.

### request

`answer` and `questions` `accepted` `favorited`are required fields.

```
POST api/user_accepted_favorited_a_list

{
   "answer": "Sunny",
   "questoins": 1, 
   "accepted": 1, 
   "favorited": [1]
}
```

### response

```
201 Created

{
	"id": 10,
	"user": "admin",
	"answer": "jingles",
	"questions": 1,
    "accepted": 1,
	"favorited": [1],
	"answered_at": "2022-04-08T20:31:56.477966Z"
}

```

## Delete one question and all answers to it 

Requires authentication.

### request

`id` are required fields.

```
DELETE api/question/<int:pk>/answers
{
   "id": "3",
}
```

### respons
```

{
	"detail": "Not found."
}
```

## Delete one answer 

Requires authentication.

### request

`id` are required fields.

```
DELETE api/<int:pk>/answer_detail

{
   "id": "9",
}
```

### respons
```

{
	"detail": "Not found."
}
```

## Update a question

Requires authentication. 

### request

```

PATCH api/<int:pk>/question_detail

{
  "favorited": []
}
```

### response

```
200 OK

{
	"id": 1,
	"user": "admin",
	"question": "What is your dogs name?",
	"favorited": [],
	"created_at": "2022-04-05T18:20:14.912272Z"
}
```
### note
```
When updating you only want to give them the option of updating the favorited field.
```

## Update a answer

Requires authentication. 

### request

```

PATCH api/<int:pk>/answer_detail

{
  "favorited": []
}
```

### response

```
200 OK

{
	"id": 1,
	"user": "admin",
	"answer": "My dogs name is Crowley.",
	"questions": 1,
	"accepted": null
	"favorited": [],
	"answered_at": "2022-04-05T18:20:41.199009Z"
}
```
### note
```
When updating you only want to give them the option of updating the accepted or favorited fields or both. 
```