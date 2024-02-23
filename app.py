from flask import Flask, render_template, request, redirect, url_for
import markdown2
import random

app = Flask(__name__)

# Preloaded demo entries stored as markdown content
entries = {
    "Python": "# Python\n\nPython is an interpreted, high-level, and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace.",
    "Flask": "# Flask\n\nFlask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.",
    "Markdown": "# Markdown\n\nMarkdown is a lightweight markup language for creating formatted text using a plain-text editor. John Gruber and Aaron Swartz created Markdown in 2004 as a markup language that is appealing to human readers in its source code form."
}

# Convert markdown to HTML
def markdown_to_html(markdown_content):
    return markdown2.markdown(markdown_content)

@app.route("/")
def index():
    all_titles = sorted(entries.keys())  # Get all titles, sorted alphabetically
    return render_template("index.html", titles=all_titles)

@app.route("/wiki/<title>")
def entry(title):
    if title in entries:
        content = markdown_to_html(entries[title])
        return render_template("entry.html", title=title, content=content)
    else:
        return render_template("error.html", message="The requested page was not found.")

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q")
    if query:
        filtered_titles = {title: markdown_to_html(content) for title, content in entries.items() if query.lower() in title.lower()}
        if filtered_titles:
            return render_template("search_results.html", titles=filtered_titles)
    return redirect(url_for('index'))

@app.route("/new", methods=["GET", "POST"])
def new_entry():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        if title in entries:
            return render_template("error.html", message="An entry with this title already exists.")
        else:
            entries[title] = content
            return redirect(url_for('entry', title=title))
    return render_template("new_entry.html")

@app.route("/edit", methods=["GET", "POST"])
def edit_entry():
    if request.method == "POST":
        original_title = request.form.get("original_title")
        new_title = request.form.get("title")
        content = request.form.get("content")
        
        # Check if the new title already exists and is not the same as the original
        if new_title in entries and original_title != new_title:
            return render_template("error.html", message="An entry with this title already exists.")
        
        # Update the entry: remove the original and add the new one if title changed
        if original_title in entries:
            del entries[original_title]  # Remove the original entry
            entries[new_title] = content  # Add the new/updated entry
            return redirect(url_for('entry', title=new_title))
        else:
            return render_template("error.html", message="The original entry was not found.")

    # GET request handling
    title = request.args.get("title")
    if title and title in entries:
        content = entries[title]
        return render_template("edit.html", title=title, content=content)
    else:
        return render_template("error.html", message="The requested entry does not exist.")

@app.route("/random")
def random_entry():
    title = random.choice(list(entries.keys()))
    return redirect(url_for('entry', title=title))

if __name__ == "__main__":
    app.run(debug=True)
