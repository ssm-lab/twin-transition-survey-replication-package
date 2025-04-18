# Replication package

### for the paper _Bridging the Silos of Digitalization and Sustainability by Twin Transition: A Multivocal Literature Review_.


## About
Twin transition is the method of parallel digital and sustainability transitions in a mutually supporting way or, in common terms, ``greening of and by IT and data''. Twin transition reacts to the growing problem of unsustainable digitalization, particularly in the ecological sense. Ignoring this problem will eventually limit the digital adeptness of society and the problem-solving capacity of humankind. Information systems engineering must find ways to support twin transition journeys through its substantial body of knowledge, methods, and techniques. To this end, we systematically survey the academic and gray literature on twin transition, clarify key concepts, and derive leads for researchers and practitioners to steer their innovation efforts.

## Contents

- `/data`
  - `data-full.xlsx` - Data sheet of 161 shortlisted studies (66 parallel transition, 71 informed transition, 24 twin transition)
  - `data-extracted.xlsx` - Data extraction sheet of the 24 twin transition studies
- `/scripts` - Analysis scripts for the automated analysis of data
- `/output` - Results of the analyses as used in the article

## How to use

### Install requirements
- Install requirements by executing `pip install -r requirements.txt` from the root folder.

### Run analysis
- For publication trends: execute `python .\scripts\publication_trends.py` from the root folder.
- For RQ1: execute `python .\scripts\mosaic.py` from the root folder.
- For RQ2: execute `python .\scripts\upset.py` from the root folder.
