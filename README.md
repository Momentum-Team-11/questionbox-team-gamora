# Questionbox

Have you ever heard no questoin is a dumb question? Questionbox is a safe space for you to be able to ask anything you're curious about. Users are able to ask any question they can think of and have other users give their expeiences or thoughts to your question. A user has the ability to accept an answer from all the answers given. Within these accepted answers a user has the ability to pick their favorite answer. 

See another question by another user? Go ahead, answer it! See if that user accepts it or even favorites it. Your insight could be what they were looking for. 

Forgot what questions you asked? Go back and look at all the questions you asked and see what your favorite answer was in your profile. Users will be able to see a list of all questions asked as well as the ones they favorited. Along with a list of questions asked the associated answers will be available to be viewed. 

Do you have many questions or answers to comb through and you would like to do a quick lookup? Use the built in search feature to find what you're looking for. 

You get the gist! Now go out and ask some questions.
------ 

### REST Api
A quick overview of how REST Api's work. press cmd k+v to open preview README

![alt text](https://www.sqlshack.com/wp-content/uploads/2021/03/representational-state-transfer-diagram_gray-e1615546557211.png "Rest Api diagram")

The client machine is your PC from where you can request data from a database server and all the communication is done over the REST APIs. There are a few methods in this which are as follows.

⋅⋅⋅ GET – Used by the client to select or retrieve data from the server

⋅⋅⋅ POST – Used by the client to send or write data to the server

⋅⋅⋅ PUT/PATCH – Used by the client to update existing data on the server

⋅⋅⋅ DELETE – Used by the client to delete existing data on the server

Our machine is communicating with a production database called Heroku. Your base production URL is https://dj-questionbox.herokuapp.com/ and you put this in your Insomnia.

The way we are going to test our endpoints is through Insomnia. This application allows us to send those methods above to our production database. 

Now that we got that out of the way let us test some endpoints. Lets start by how a user will ask a question. 
## Create a new question

Requires authentication by registering and logging in.

### request

`question` are required fields.

```
POST api/user_q_list
(you will put <api/user_q_list> at the end of your base production URL)
{
   "question": "What is your birds name?",
}
```

### response

```
201 Created

{
	"id": 7,
	"user": "admin",
	"question": "What is your birds name?",
	"favorited": [],
	"created_at": "2022-04-08T19:17:00.463150Z"
}

```

After we have made a question we should have other users answering our question. Lets take a look how to view all those answers from that question using the `GET` method. 
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
	"id": 2,
	"user": "admin",
	"question": "Who is Gamora?",
	"answers": [
		{
			"id": 21,
			"user": "paul",
			"answer": "She is the daughter of Thanos.",
			"questions": 2,
			"accepted": 1,
			"favorited": [
				1
			],
			"answered_at": "2022-04-14T13:27:49.184754Z"
		}
	]
}
```

Notice how favorited has a 1 in the M2M field. That answer was favorited by that user. To update or `PATCH` existing data so that the favorited field is gone try this.
## Update a question

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
	"id": 21,
	"user": "paul",
	"answer": "She is the daughter of Thanos.",
	"questions": 2,
	"accepted": 1,
	"favorited": [],
	"answered_at": "2022-04-14T13:27:49.184754Z"
}
```

