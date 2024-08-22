import json


json_data = '''{
  "basics": {
    "name": "abhishek Verma",
    "label": "Programmer",
    "image": "",
    "email": "abhishekverma9091@gmail.com",
    "phone": "9792299091",
    "url": "https://abhishekverma.com",
    "summary": "A summary of abhishek verma..",
    "location": {
      "address": "2712 Broadway St",
      "postalCode": "ind 94115",
      "city": "San Francisco",
      "countryCode": "IND",
      "region": "INDIA"
    },
    "profiles": [{
      "network": "Twitter",
      "username": "abhishek",
      "url": "https://twitter.com/abhishek"
    }]
  },
  "work": [{
    "name": "XYZ Company",
    "position": "SDE",
    "url": "https://company.com",
    "startDate": "2013-01-01",
    "endDate": "2014-01-01",
    "summary": "Description…",
    "highlights": [
      "Started the company"
    ]
  }],
  "volunteer": [{
    "organization": "Organization",
    "position": "Volunteer",
    "url": "https://organization.com/",
    "startDate": "2012-01-01",
    "endDate": "2013-01-01",
    "summary": "Description…",
    "highlights": [
      "Awarded 'Volunteer of the Month'"
    ]
  }],
  "education": [{
    "institution": "GLA University",
    "url": "https://institution.com/",
    "area": "Software Development",
    "studyType": "Bachelor",
    "startDate": "2011-01-01",
    "endDate": "2013-01-01",
    "score": "4.0",
    "courses": [
      "DB1101 - Basic SQL"
    ]
  }],
  "awards": [{
    "title": "Award",
    "date": "2014-11-01",
    "awarder": "Company",
    "summary": "There is no spoon."
  }],
  "certificates": [{
    "name": "Certificate",
    "date": "2021-11-07",
    "issuer": "Company",
    "url": "https://certificate.com"
  }],
  "publications": [{
    "name": "Publication",
    "publisher": "Company",
    "releaseDate": "2014-10-01",
    "url": "https://publication.com",
    "summary": "Description…"
  }],
  "skills": [{
    "name": "Web Development",
    "level": "Master",
    "keywords": [
      "HTML",
      "CSS",
      "JavaScript"
    ]
  }],
  "languages": [{
    "language": "English",
    "fluency": "Native speaker"
  }],
  "interests": [{
    "name": "Wildlife",
    "keywords": [
      "Ferrets",
      "Unicorns"
    ]
  }],
  "references": [{
    "name": "Jane Doe",
    "reference": "Reference…"
  }],
  "projects": [{
    "name": "Project",
    "startDate": "2019-01-01",
    "endDate": "2021-01-01",
    "description": "Description...",
    "highlights": [
      "Won award at AIHacks 2016"
    ],
    "url": "https://project.com/"
  }]
}'''

# Parsing the JSON data
data = json.loads(json_data)

# Accessing and printing some of the data
print("Name:", data['basics']['name'])
print("Email:", data['basics']['email'])
print("Work Position:", data['work'][0]['position'])
print("Education Institution:", data['education'][0]['institution'])
print("Skills:", data['skills'][0]['name'], "-", data['skills'][0]['keywords'])