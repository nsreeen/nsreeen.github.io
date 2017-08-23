import markdown2
import os


# get post text
def get_post_md(post):
    post_path = '../blog/posts/' + post
    with open(post_path, 'r') as post_file:
        post_text = post_file.read()
    return post_text

# get the html of the whole posts page
def get_post_html_and_meta(md_text):
    html = markdown2.markdown(md_text, extras=["tables", "metadata", "fenced-code-blocks"])
    title = html.metadata['title']
    date = html.metadata['date']
    h1 = "<h1>" + title + "</h1>"
    page = header + h1 + html + footer
    return page, title, date

# get the url
def get_url(title):
    url = "-".join(title.split()).lower()
    if url[-1] == "?":
        return url[:-1]
    return url

# write the html file
def write_page_html(page_html, post_url):
    post_dir = '../' + post_url
    if not os.path.exists(post_dir):
        os.makedirs(post_dir)
    with open(post_dir + '/index.html', 'w') as html_file:
        html_file.write(page_html)

# read file
def get_file_contents(path):
    with open(path, 'r') as f:
        file_contents = f.read()
    return file_contents

def get_page_list_unit(post):
    html = "<li><a href=" + post['url'] + ">" + post['title'] + "</li>"
    return html


# get template html
header = get_file_contents('../blog/templates/header.html')
footer = get_file_contents('../blog/templates/footer.html')

# get all posts in the posts folder
posts = [post for post in os.listdir('../blog/posts')]

posts_data = []

for post in posts:
    print(post)
    post_markdown = get_post_md(post)
    page, page_title, post_date =  get_post_html_and_meta(post_markdown)
    page_url = get_url(page_title)
    print('page_url: ', page_url)
    write_page_html(page, page_url)
    posts_data.append({'title': page_title, 'url': page_url, 'date': post_date})

ordered_posts = sorted(posts_data, reverse=True, key=lambda post: post['date'])
print(ordered_posts)

# makes index.html in root
index_html = header + '<ul class="page-list">'
for post in ordered_posts:
    index_html += get_page_list_unit(post)
index_html += "</ul>"
index_html += footer

with open('../index.html', 'w') as index_file:
    index_file.write(index_html)


# updates atom feed
# - to do
