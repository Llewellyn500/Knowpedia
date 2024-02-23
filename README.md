# Knowpedia

Welcome to Knowpedia!
This is a repository for our CSM 399 - Web-Based Concepts and Development course, Group 1S1.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Contributors](#contributors)
- [Folder Structure](#folder-structure)

## Introduction

Knowpedia is a web-based application that allows users to create and edit their own knowledge base. Users can create articles, add images, and link articles together. Users can also search for articles and view articles in a list.

## Installation

- install python 3.12.2 or later

- open the repo and enter the following command:

```
python -m venv venv

source venv/bin/activate  # On Windows use `venv\Scripts\activate`

pip install Flask markdown2
```

## Usage

```
flusk run
```

## Contributors

...

## Folder Structure

```
/Knowpedia
    /static
        /css
            style.css
    /templates
        entry.html
        index.html
        search_results.html
        edit.html
        base.html
        new_entry.html
    app.py
```