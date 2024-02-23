# Knowpedia

Welcome to Knowpedia!

This is a repository for our CSM 399 - Web-Based Concepts and Development, Group 1S1 Project work.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Group Members](#groupmembers)
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

## Group Members

- [Paintsil Llewellyn Kobina Adonteng](https://github.com/Llewellyn500)
- ADJETEY SOWAH Sharon Naa Adjeley
- ARKOH Theophilus
- BOATENG Peter Nkansah Brantuo
- DICKSON Angel Hope
- MACDUMOGAH Alfreda
- MENSAH Caleb Opoku Kudom
- NTI Hakeem
- OMABOE Leroy Junior
- WILLIAMS Spencer Edinam

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