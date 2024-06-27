<h1 align="center">Cloudforet Plugin Example</h1>  
  
<br/>  
<div align="center" style="display:flex;">  
  <img width="300" src="https://user-images.githubusercontent.com/65589909/197983716-71a1bd21-4d6a-4217-b509-177afbadf5bc.png">  
<p> <br>  
<a  href="https://www.apache.org/licenses/LICENSE-2.0"  target="_blank">  
<img  alt="License: Apache 2.0"  src="https://img.shields.io/badge/License-Apache 2.0-yellow.svg"  />  
</a>
</p>  
  
</div> 

`plugin-example-inven-collector` is an example inventory collector plugin for Cloudforet. This plugin helps you implement custom inventory collection.

# Development Guide

To develop the plugin, follow these steps:

1. Fork the repository (https://github.com/cloudforet-io/plugin-example-inven-collector.git)
2. Clone the repository.

```bash
git clone https://github.com/{Your repository}/plugin-example-inven-collector.git
cd plugin-example-inven-collector
```

## Development Environment

1) Python Virtual environment
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```

2) Install dependencies
```bash
pip3 install -e .
```

## Run Plugin Server

```
spaceone run plugin-server plugin -m src
```


## Local Test

```angular2html
pip3 install spacectl
spacectl config init -f test/local.yml
```
<br>
<br>

`List API spec`
```bash
spacectl api-resources
```

<br>

1) `Collector.init`
```bash
spacectl exec init inventory.Collector -f test/init.yml
```

<br>

2) `Collector.verify`
```bash
spacectl exec verify inventory.Collector -f test/verify.yml
```

<br>

3) `Collector.collect`
```bash
spacectl exec collect inventory.Collector -f test/collect.yml
```

