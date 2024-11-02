# Replication package

### for the paper _Twin Transition: Bridging the Silos of Digitalization and Sustainability_.


## About
Twin transition is the method of parallel digital and sustainability transitions in a mutually supporting way—or, in common terms, "greening of and by IT and data". Twin transition reacts to the growing problem of unsustainable digitalization, particularly in the ecological sense. Ignoring this problem will eventually limit the digital adeptness of society and the problem-solving capacity of humankind. Information systems (IS) engineering must find ways to support twin transition journeys through its substantial body of knowledge, methods, and techniques. To this end, we systematically survey the academic and grey literature on twin transition, clarify key concepts, and derive leads for IS scientists and practitioners to steer their research and development efforts.

## Contents

- `/data` - Data extraction sheet of 22 included studies (with fully extrated data); and 16 eventually excluded studies (with quality data that justifies the exclusion).
- `/scripts` - Analysis scripts for the automated analysis of data.
- `/output` - Results of the analyses as used in the article.

## How to use

### Install requirements
- Install requirements by executing `pip install -r requirements.txt` from the root folder.

### Run analysis
- For publication trends: execute `python .\scripts\publication_trends.py` from the root folder.
- For RQ1: execute `python .\scripts\mosaic.py` from the root folder.
