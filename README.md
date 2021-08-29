# My blog

## To create a new post

1) Activate your venv.
If this is the first time you are creating one, create it and install the requirements.  If you want to use pyenv:
```
pyenv virtualenv venv
pyenv activate venv
pip install -r requirements.txt
```

2) Write the ost, and save it as an .md file in blog/posts.  It should have a metadata section at the top.

3) Run the script to create the html page for the post:
`python3 ./bin/update_blog.py`

4) Open the post in a browser to check it looks ok.

5) Push the changes.
