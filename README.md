# README

## Use Tags To Make Docs

This project was started Feb 3, 2020 by Christine Beck.  It's purpose is to create documentation from AWS tags.  

## Getting Started

### Setup

1. Clone this repo
2. You will need to install the AWS-cli. Check AWS-cli docs for install instructions.
3. Make sure the AWS account you are interested in is set to default in your root .aws directory's credentials file.
4. Install boto3, an aws library for python.

    ```python
    python3 -m pip install boto3
    ```

### To Run

```bash
cd use_tags_to_make_docs directory
python3 ./app.py
```

### Output

- Output will be printed to a new all_tags.md file in the output directory in this repo.  
- Output is replaced each time the ./app.py command is run.


## Why am I making this

The user has AWS resources with tags that need to be updated.  This program helps visualize and organize AWS EC2 tags key value pairs during the update process.

## Tools Used

- Boto3, a python AWS library
- Python3