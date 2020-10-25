# KU Polls

[![Build Status](https://travis-ci.com/Bheem6005/ku-polls.svg?branch=master)](https://travis-ci.com/Bheem6005/ku-polls)
[![codecov](https://codecov.io/gh/Bheem6005/ku-polls/branch/master/graph/badge.svg)](https://codecov.io/gh/Bheem6005/ku-polls)

Web application for KU staff and students to create online polls.

## Requirements

Requires Python 3.6 and the Python packages listed in [requirements.txt](requirements.txt).

Install required packages using `pip install -r requirements.txt.`

## Running the Application

1. Edit `.env` in the projet base directory and set these variables:

```
SECRET_KEY=a-secret-key
DEBUG=False   (set to True for development)
```

  - any string w/o space can be used as secret key. For a truly random secret that's in a format used by django use:

```
from django.core.management.utils import get_random_secret_key
print( get_random_secret_key() )
```

2. Start the server. Optionally, you can specify a port to listen on as extra command line argument.

```
python manage.py runserver
```

3. Visit http://localhost:8000

TODO: Document migrations and data import (once we have some polls to import!).

## Documents

[Wiki Home Page](https://github.com/Bheem6005/ku-polls/wiki)

[Vision Statement](https://github.com/Bheem6005/ku-polls/wiki/Vision-Statement)

[Requirements](https://github.com/Bheem6005/ku-polls/wiki/Requirements)

Iteration

- [Iteration 1 Plan](https://github.com/Bheem6005/ku-polls/wiki/Iteration-1-Plan) and [Task Board](https://github.com/Bheem6005/ku-polls/projects/1)

- [Iteration 2 Plan](https://github.com/Bheem6005/ku-polls/wiki/Iteration-2-Plan) and [Task Board](https://github.com/Bheem6005/ku-polls/projects/2)

- [Iteration 3 Plan](https://github.com/Bheem6005/ku-polls/wiki/Iteration-3-Plan) and [Task Board](https://github.com/Bheem6005/ku-polls/projects/3)