import markdown2
import os
import re
from index_row import get_index_row
import datetime

def replace_ticks_for_code(matchobj):
    return '<code>' + matchobj.group(0)[1:-1] + '</code>'

def fix_code_tags(html):
    html = re.sub('`([a-zA-Z]+?)`', replace_ticks_for_code, html)
    return html

def add_new_lines(html):
    #html = re.sub('', '<br>', html)
    return html

def get_post_md_text(post):
    post_path = 'blog/posts/' + post
    with open(post_path, 'r') as post_file:
        post_text = post_file.read()
    return post_text

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
    if not os.path.exists(post_url):
        os.makedirs(post_url)
    with open(post_url + '/index.html', 'w') as html_file:
        html_file.write(page_html)

def get_template(template):
    path = 'blog/templates/' + template + '.html'
    with open(path, 'r') as f:
        file_contents = f.read()
    return file_contents

def get_page_list_unit(post):
    date = datetime.datetime.strptime(post['date'], '%Y-%m-%d %H:%M:%S')
    formatted_date = date.strftime("%b %Y")
    #html = "<li><a href=" + post['url'] + ">" + post['title'] + post['date'] + "</li>"
    html = get_index_row(post['url'], post['title'], formatted_date)
    return html

def make_post_list_page():
    index_html = header + '<ul class="page-list">'
    for post in ordered_posts:
        index_html += get_page_list_unit(post)
    index_html += "</ul>"
    index_html += footer
    with open('index.html', 'w') as index_file:
        index_file.write(index_html)

# takes markdown file name, generates and writes the html file (in appropriate folder), and adds to posts data list
def make_post_page(post):
    print('\n post:', post)
    post_markdown = get_post_md_text(post)
    page, page_title, post_date =  get_post_html_and_meta(post_markdown)
    page = fix_code_tags(page)
    page = add_new_lines(page)
    page_url = get_url(page_title)
    write_page_html(page, page_url)
    posts_data.append({'title': page_title, 'url': page_url, 'date': post_date})


if __name__ == "__main__":

    # get template html
    header = get_template('header')
    footer = get_template('footer')

    # get all posts in the posts folder
    posts = [post for post in os.listdir('blog/posts') if post[:2] != "xx"]

    posts_data = []

    for post in posts:
        make_post_page(post)

    ordered_posts = sorted(posts_data, reverse=True, key=lambda post: post['date'])

    # write post list as index.html in root
    make_post_list_page()


"""
TO DO:
- use templates as templates:
     - pass named arguments to template filler function - meta should be an object?
     - use template for post page
- have a config object which has the paths to things so they are not hardcoded
and the xx for draft dont publish (in another file)
- separate all the markdown related stuff to another file?

"""
