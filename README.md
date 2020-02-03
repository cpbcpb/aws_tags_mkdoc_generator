# README

## Use Tags To Make Docs

This project was started Feb 3, 2020 by Christine Beck.  It's purpose is to create documentation from AWS tags.  

## Features

- Will list working features here as they come.

## How to Use

- Will explain how to get this project working here once it has some features.

## Tools Used

- Boto3, a python AWS library
- Python3
- (probably) mkDocs

## Why am I making this

The user has AWS resources with tags describing dependencies. The user wants to be able to automatically create and update documentation in .md files based on these tags.  

*The Tag Key* is "Dependencies" and *Tag Value* is stringified json with the name and version of each dependency:

```json
    'Dependencies': "{
        'Python' : '3.7.4',
        'boto3' : 'boto3'
        }"
```
