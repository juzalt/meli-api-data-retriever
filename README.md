# MeLi Api Data Retriever

This tool allows you to fetch product data from Mercado Libre's public API. 

## Getting Started
### Pre-requisites
Install the following before using this tool:
```
Python 3.0 or later.
pip3 (sudo apt-get install python3-pip).
```

### Installing
```bash
$ git clone https://github.com/juzalt/meli-api-data-retriever.git
$ cd meli-api-data-retriever
$ pip3 install -r requirements.txt
```

If using Windows make sure to run that last line this way:
```bash
$ python -m pip install -r requirements.txt
```

### Parameters
```
-r --region [country] (required)
-q --query [search query] (required)
-o --output [output file] (optional)
```

### Usage
```bash
$ python3 main.py -r <region> -q <search query> [-o outputFile.txt]
```
### Example
```bash
$ python3 main.py -r MLA -q samsung_tv -o argentine-samsung-tv.txt
```

## Screenshots
<p align="center">
  <img src="https://julianzaltron.now.sh/static/media/meliadr-argentina.c371fd36.png" alt="Screenshot showing command being run for Argentina." />
</p>

<p align="center">
  <img src="https://julianzaltron.now.sh/static/media/meliadr-mexico.2235e3fc.png" alt="Screenshot showing command being run for Mexico." />
</p>

## Author
[Julian Zaltron](https://julianzaltron.now.sh)
