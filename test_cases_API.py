import requests
import pytest

# API url
base_url = "https://jsonplaceholder.typicode.com"

# note: the order of test cases is according to the task document
# ******************************************************
# positive test case to get the posts route from api, access to postId = 2 and id = 11
# we will access to url https://jsonplaceholder.typicode.com/posts
def test_get_posts_have_postId_2_id_11_positive():
    # to get the url of API will use variable response to get the request from api using get method
    response = requests.get(base_url + "/posts")
    # access to the json file using .json() method
    response_body = response.json()
    # Access to list items, we will access to the item with id = 11,
    # but the index starts from zero, so the index is 10
    index = response_body[10]
    # Access to dictionary items, using the items() method will return each item in a dictionary,the keys and the values
    access = index.items()
    # chick if the data accessed passed or failed,the pytest assertion to verify expectations and values in Python tests
    assert index["title"] == "et ea vero quia laudantium autem"

    print(access)
    print(response.status_code)


# negative test case to get the posts route from api, access to postId = 2 and id = 11
# we will access to url https://jsonplaceholder.typicode.com/posts
def test_get_posts_have_postId_2_id_11_negative():
    # to get the url of API will use variable response to get the request from api using get method
    response = requests.get(base_url + "/posts")
    # access to the json file using .json() method
    response_body = response.json()
    # Access to list items, we will access to item with id = 11,
    # but the index starts from zero so the index is 10
    index = response_body[10]
    # Access to dictionary items, using the items() method will return each item in a dictionary,the keys and the values
    access = index.items()
    # chick if the data accessed passed or failed,the pytest assertion to verify expectations and values in Python tests
    assert index["title"] == "API testing"

    print(access)
    print(response.status_code)


# *****************************************************************
# positive test case to get the userId in posts route from api, access to postId = 1 and id = 1 according to the task was sent
# we will access to url https://jsonplaceholder.typicode.com/posts/1
def test_get_posts_have_postId_1_id_1_positive():
    # to get the url of API will use variable response to get the request from api using get method
    response = requests.get(base_url + "/posts")
    # access to the json file using .json() method
    response_body = response.json()
    # Access to list items, we will access to the first item with id = 1, but the index starts with 0
    index = response_body[0]
    # Access to dictionary items, using the keys() method will return each item key in a dictionary
    access = index.keys()
    # chick if the data accessed passed or failed,the pytest assertion to verify expectations and values in Python tests
    assert index["id"] == 1
    print(access)
    print(response.status_code)


# negative test case to get the userId in posts route from api, access to postId = 1 and id = 1 according to the task was sent
# we will access to url https://jsonplaceholder.typicode.com/posts/1
def test_get_posts_have_postId_1_id_1_negative():
    # to get the url of API will use variable response to get the request from api using get method
    response = requests.get(base_url + "/posts")
    # access to the json file using .json() method
    response_body = response.json()
    # Access to list items, we will access to the first item with id = 1, but the index starts with 0
    index = response_body[0]
    # Access to dictionary items, using the keys() method will return each item key in a dictionary
    access = index.keys()
    # chick if the data accessed passed or failed,the pytest assertion to verify expectations and values in Python tests
    assert index["id"] == 4

    print(access)
    print(response.status_code)


# *************************************************************
# positive test case to get the comments in posts route from api, access to postId = 1 and id = 1 according to the task was sent
# we will access to url https://jsonplaceholder.typicode.com/comments?postId=1
def test_get_comments_have_postId_equals_1_positive():
    # to get the url of API will use variable response to get the request from api using get method
    response = requests.get(base_url + "/comments")
    # access to the json file using .json() method
    response_body = response.json()
    # Access to list items, we will access to the first item with id = 1, but the index starts with 0
    index = response_body[0]
    # Access to dictionary items, using the values() method will return each item value in a dictionary
    access = index.values()
    # chick if the data accessed passed or failed,the pytest assertion to verify expectations and values in Python tests
    assert index["postId"] == 1
    print(access)
    print(response.status_code)


# negative test case to get the comments in posts route from api,access to postId = 1 and id = 1 according to the task was sent
# we will access to url https://jsonplaceholder.typicode.com/comments?postId=1
def test_get_comments_have_postId_equals_1_negative():
    # to get the url of API will use variable response to get the request from api using get method
    response = requests.get(base_url + "/comments")
    # access to the json file using .json() method
    response_body = response.json()
    # Access to list items, we will access to the first item with id = 1, but the index starts with 0
    index = response_body[0]
    # Access to dictionary items, using the values() method will return each item value in a dictionary
    access = index.values()
    # chick if the data accessed passed or failed,the pytest assertion to verify expectations and values in Python tests
    assert index["postId"] == 9
    print(access)
    print(response.status_code)


# *************************************************************
# positive test case to create new post to api using post method, we will create new post with userId, title and body
# Submit a POST request to url https://jsonplaceholder.typicode.com/posts
def test_create_new_post_using_post_method_positive_case():
    # write the json format
    new_post = {
        "userId": 1,
        "title": "My new post title",
        "body": "My new post body"

    }
    # to create the url and json post of API will use variable response to create the request to api using post method
    response = requests.post(base_url + "/posts", json=new_post)
    # access to the json file using .json() method
    response_body = response.json()
    # chick if the data accessed passed or failed,the pytest assertion to verify expectations and values in Python tests
    assert response_body["userId"] == 1
    # Check that the response status code equals 201 (Created)
    code = response.status_code
    # validate the response status code is 201 created
    assert code == 201
    print(response_body)
    print(code)


# negative test case to create new post to api using post method, we will create new post with userId, title and body
# Submit a POST request to url https://jsonplaceholder.typicode.com/posts
def test_create_new_post_using_post_method_negative_case():
    # write the json format
    new_post = {
        "title": "new post title",
        "body": " new post body",
        "userId": 2
    }
    # to create the url and json post of API will use variable response to create the request to api using post method
    # but will be failed because we are trying to access to the wrong url
    response = requests.post(base_url + "//posts//id", json=new_post)
    # Check that the response status code equals 404 that means page not found
    code = response.status_code
    print(code)
    # validate the response status code is 404
    assert code == 404
    # access to the json file using .json() method
    response_body = response.json()
    assert "name" in response_body == "Eliseo"


# ************************************************************
# Positive case of delete the posts using delete() method
def test_delete_posts_have_userId_equals_1_using_delete_method_positive_case():
    # delete the post have userId equals 1 using delete() method
    response = requests.delete(base_url + "/posts/1")
    print(response.status_code)


# Negative case of delete the posts
def test_delete_posts_have_userId_equals_1_using_delete_method_negative_case():
    # delete the post have userId equals 1 using delete() method, but this function will fail,
    # because chick the negative test case
    response = requests.delete(base_url + "//posts")
    # Check that the response status code equals 404 that means page not found
    code = response.status_code
    print(code)
    # validate the response status code is 404
    assert code == 404
    # access to the json file using .json() method
    response_body = response.json()
    assert "email" in response_body



