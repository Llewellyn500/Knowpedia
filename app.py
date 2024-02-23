from flask import Flask, render_template, request, redirect, url_for
import markdown2
import random

app = Flask(__name__)

# Preloaded demo entries stored as markdown content
entries = {
    "MIT News on Computer Science and Technology": "This article from MIT News showcases a range of innovative projects and research at MIT, including advances in energy-efficient computing, new models for drug interactions, and smart devices that enhance learning and interaction. It highlights the cutting-edge work being done at the intersection of computer science and technology, offering inspiration and insight into what's possible in the field​",
    "The Cognitive Benefits of Learning to Code": "Published in Frontiers, this article presents a comprehensive look at how learning to code not only improves coding skills but also enhances a broad range of cognitive abilities. It discusses the positive effects on problem-solving, critical thinking, and creative thinking, among other skills, underscoring coding's relevance beyond the tech world​",
    "Coding for and as Social Science": "From the London School of Economics' blog, this article explores the transformative potential of programming skills in social sciences. It discusses how coding can open up new methodologies for research, offer innovative ways to engage with digital social life, and even transform how social phenomena are studied and understood",
    "Important Life Skills You Can Learn From Coding": "This article from the Singapore Management University (SMU) Blog discusses how coding isn't just for tech professionals but is a valuable skill that teaches logical thinking, problem-solving, and creativity. It makes a compelling case for the universality of computational thinking and its applicability to various aspects of life and decision-making",
    "Automated Method Helps Researchers Quantify Uncertainty in Their Predictions": "An article from MIT News describes an easy-to-use technique that could aid a wide range of professionals, from economists to sports analysts, in making more accurate predictions. This highlights the practical applications of computer science and coding skills across different fields​"
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
