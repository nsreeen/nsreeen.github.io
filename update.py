
import os

def update_line(l):
    if l == '"""':
        return '+++'
    if l.startswith("published: ") or l.startswith("type: "):
        return ""
    if l.startswith("title: "):
        return f'title = "{l.split(":")[1].strip()}"'
    if l.startswith("date: "):
        return f'date = {l.split(" ")[1]}'
    return l

if __name__ == "__main__":
    posts = [post for post in os.listdir('old') if post[0] != "_"]
    for postname in posts[1:]:
        with open(f"old/{postname}", 'r') as post_file:
            post_text = post_file.read()
        new_text = "\n".join([update_line(l) for l in post_text.split("\n")])
        with open(f"content/blog/{postname}", 'w') as new_file:
            new_file.write(new_text)
