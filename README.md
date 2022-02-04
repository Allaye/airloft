<div id="top"></div>





<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- [![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url] -->



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/allaye/trakar">
    <!-- <img src="images/logo.png" alt="Logo" width="80" height="80"> -->
  </a>

<h3 align="center">Trakar</h3>

  <p align="center">
    This is a real time project activity time tracker, which tracks your time spent on projects.<br />
    <!-- <br />
    <a href="https://github.com/github_username/repo_name"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/github_username/repo_name">View Demo</a>
    · -->
    <a href="https://github.com/allaye/trakar/issues">Report Bug</a>
    ·
    <a href="https://github.com/allaye/trakar/issues">Request Feature</a>
  </p>
</div>

##### Thanks for checking out this project. 
##### If you have a suggestion that would make this better, please fork the repo and create a pull request or simply open an issue with the tag "feature update".
##### Don't forget to give the project a star if you like it!
##### Thanks again! Now go create something AMAZING! :D🫂


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#examples">Examples</a></li>
    <!-- <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li> -->
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

This is a real time project activity tracker, which tracks your time spent on projects. with this app you can track the time employees spents on projects. and 
come out with some analytics insight from it. it can be use to calculate employee productivity and wages etc.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://python.org/)
* [Django](https://www.djangoproject.com/)
* [DRF](https://www.django-rest-framework.org/)
* [SQLITE3](https://www.sqlite.org/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get started download or clone the repo.

### Prerequisites

You are required to have at least python 3.6.0 installed to use this project

### Installation

Navigate into the project directory and install the requirements.txt file.
install the requirements.txt file using the following command:

1. Clone the repo using: git clone https://github.com/allaye/trakar.git
2. Navigate into the directory containing the project: cd trakar
3. Install the requirements.txt file using: pip install -r requirements.txt
4. Run the project using: python manage.py runserver

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
This section contains all the useful endpoints this project provides.

    - [x] User endpoints

        - [x] Register a new user
             * POST /api/register/
              request body:{
                  "username": "johndoe",
                  "email": "john@email.com",
                  "password": "password"
              }
        - [x] Login a user
             * POST /api/login/
              request body:{
                  "email": "john@email.com",
                  "password": "password"
              }
              response object:{
                  "email": "a@email.com",
                  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImEiLCJlbWFpbCI6ImFAZW1haWwuY29tIiwiZXhwIjoxNjQwNDQ2OTM1fQ.wF4WvEK37GOXRWC8rzRWUv2UgToNtqaRXte_G_wbO4s",
                  "is_staff": false
              }
        - [x] Logout a user:{
          requirement is to be loged in
        }
    
    - [x] Project endpoints

      -[x] Create New Project (can only be created by an admin)
          * POST /api/create/project/
            request body:{
                "name": "project name",
                "description": "project description",
                "members": [1,4,2]
                "start_date": "2020-01-01",
                "end_date": "",
                "is_active": true
            }
            response object:{
                "id": 1,
                "name": "project name",
                "description": "project description",
                "start_date": "2020-01-01",
                "end_date": "2020-01-01",
                "is_active": true
            }
      -[x] Get all projects
          * GET /api/projects/
            response object:{
                "projects": [
                    {
                        "id": 1,
                        "name": "project name",
                        "description": "project description",
                        "start_date": "2020-01-01",
                        "end_date": "2020-01-01",
                        "is_active": true,
                        "members""[1,3]
                    },
                    {
                        "id": 2,
                        "name": "project name",
                        "description": "project description",
                        "start_date": "2020-01-01",
                        "end_date": "2020-01-01",
                        "is_active": true,
                        "members""[4]
                    }
                ]
            }
    - [x] Project Activities endpoints
        
        -[x] Create New Project Activity
            * POST /api/create/project/activity/
              request body:{
                  "user": 1,
                  "project": 1,
                  "activity": "activity name",
                  "description": "activity description",
                  "start_date": "2020-01-01",
                  "end_date": "",
              }
              response object:{
                  "id": 1,
                  "project": 1,
                  "activity": "activity name",
                  "description": "activity description",
                  "start_date": "2020-01-01",
                  "end_date": "2020-01-01",
                  "is_active": true
                  "duration": 1000
              }
        -[x] Get all project activities
            * GET /api/project/activities/
              response object:{
                  "activities": [
                      {
                          "id": 1,
                          "project": 1,
                          "activity": "activity name",
                          "description": "activity description",
                          "start_date": "2020-01-01",
                          "end_date": "2020-01-01",
                          "is_active": true
                      },
                      {
                          "id": 2,
                          "project": 1,
                          "activity": "activity name",
                          "description": "activity description",
                          "start_date": "2020-01-01",
                          "end_date": "2020-01-01",
                          "is_active": true
                      }
                  ]
              }

<p align="right">(<a href="#top">back to top</a>)</p>

## Examples
Register a new user, to create a new non admin user use the below example,
create a post request with the following minimum request body:

    - Endpoint: Post: /api/register/
    - Request body:{
    "username": "ab",
    "email": "ab@email.com",
    "password": "ab@email.com"
    }

    - Response:{
    "id": 1,
    "username": "ab",
    "email": "ab@email.com",
    "is_staff": false
    }
after creating a new user, you can now login with the email and password you provided to obtain a token on succesful login.
login using the below endpoint and example request body:

    - Endpoint: Post: /api/login/
    - Request body:{
    "email": "ab@email.com",
    "password": "ab@email.com"
    }

    - Response:{
    "email": "ab@email.com",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImEiLCJlbWFpbCI6ImFAZW1haWwuY29tIiwiZXhwIjoxNjQxMDUyMjI0fQ.unXe-dxoFCEY5l2VGkeRR8ue-Ggr6YxQS2nJUA63VZ4",
    "is_staff": false
    }
On successful login you get the above response object, the most important value there is the token, the token will be use on all protected
endpoint in other to gain access to the protected endpoints.

<b>Project Endpoints:</b>
The project endpoints have some few requirements to be able to use the endpoints,
1. You must be an admin to create a project
2. You must be logged in get details of a project
3. A project can have 1 or more members

create a new project using the below endpoint and example request body:

    - Endpoint: Post: /api/create/project
    - Authorization: Bearer <eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImEiLCJlbWFpbCI6ImFAZW1haWwuY29tIiwiZXhwIjoxNjQxMDUyMjI0fQ.unXe-dxoFCEY5l2VGkeRR8ue-Ggr6YxQS2nJUA63VZ4>
    - Request body:{
    "name": "project pholoa",
    "description": "blockchain systems to track spent time",
    "technology": {"technology":"blockchain"},
    "members": [1,4,2]           // this are the members ids added to the project (project members)
    "start_date": "2022-01-01",  // if left blank it defaults to today
    }

    - Response:{
    "id": 3,
    "is_completed": false,
    "title": "",
    "description": "blockchain systems to track spent time",
    "technology": {
        "technology": "blockchain"
    },
    "start_date": "2022-01-01",
    "end_date": null,
    "members": [
        1, 4, 2
    ]
    }
you get a 403 error if you try to create a project without being an admin, to create an admin user you added 
-     "is_staff": 1  
to the user body when creating a user.

List all, one, update and delete project endpoints are protected use token to access them,
endpoints url
List All: 
-      Endpoint Get api/projects/
-      Authorization: Bearer <eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImEiLCJlbWFpbCI6ImFAZW1haWwuY29tIiwiZXhwIjoxNjQxMDUyMjI0fQ.unXe-dxoFCEY5l2VGkeRR8ue-Ggr6YxQS2nJUA63VZ4>

-      - Response:{
        "projects": [
            {
                "id": 1,
                "is_completed": false,
                "title": "",
                "description": "blockchain systems to track spent time",
                "technology": {
                    "technology": "blockchain"
                },
                "start_date": "2022-01-01",
                "end_date": null,
                "members": [
                    1, 4, 2
                ]
            }

List All endpoint user is member of:
-      Endpoint Get api/projects/me/
-      token: <eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImEiLCJlbWFpbCI6ImFAZW1haWwuY29tIiwiZXhwIjoxNjQxMDUyMjI0fQ.unXe-dxoFCEY5l2VGkeRR8ue-Ggr6YxQS2nJUA63VZ4>
-      Response{

        }
List one project:
-      Endpoint Get api/projects/1/
-      Authorization: Bearer <eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImEiLCJlbWFpbCI6ImFAZW1haWwuY29tIiwiZXhwIjoxNjQxMDUyMjI0fQ.unXe-dxoFCEY5l2VGkeRR8ue-Ggr6YxQS2nJUA63VZ4>
-      Response{
        "id": 1,
        "is_completed": false,
        "title": "",
        "description": "blockchain systems to track spent time",
        "technology": {
            "technology": "blockchain"
        },
        "start_date": "2022-01-01",
        "end_date": null,
        "members": [
            1, 4, 2
        ]
        }


delete a project:
-      Endpoint DELETE api/project/delete/1/
-      Authorization: Bearer <eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImEiLCJlbWFpbCI6ImFAZW1haWwuY29tIiwiZXhwIjoxNjQxMDUyMjI0fQ.unXe-dxoFCEY5l2VGkeRR8ue-Ggr6YxQS2nJUA63VZ4>

-      Response{
        "message": "Project deleted successfully"
        }


Update a project:
-      Endpoint PATCH api/project/update/1/
-      Authorization: Bearer <eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImEiLCJlbWFpbCI6ImFAZW1haWwuY29tIiwiZXhwIjoxNjQxMDUyMjI0fQ.unXe-dxoFCEY5l2VGkeRR8ue-Ggr6YxQS2nJUA63VZ4>
-      Request body:{
        "start_date": "2022-01-01",
        "end_date": 2022-10-10,
        }
-      Response{
        "id": 1,
        "is_completed": true,
        "title": "title here",
        "description": "blockchain systems to track spent time",
        "technology": {
            "technology": "blockchain"
        },
        "start_date": "2022-01-01",
        "end_date": "2022-10-10",
        "members": [
            1, 4, 2
        ]
        }


<b>Project activities endpoints:</b>
These endpoints are used to create, list, update and delete project activities.
activities are tasks that are perform on a project., theses endpoints are all protected, use token to access them,

The project activities endpoints have some few requirements to be able to use the endpoints,
1. only a project member can create a project activity on a project
2. only a project activity creator can update or delete a project activity
3. only some field of a project activity can be updated or fields remain read only

-      Endpoint POST api/create/activity
-      Authorization: Bearer <eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImEiLCJlbWFpbCI6ImFAZW1haWwuY29tIiwiZXhwIjoxNjQxMDUyMjI0fQ.unXe-dxoFCEY5l2VGkeRR8ue-Ggr6YxQS2nJUA63VZ4>
-      Request body:{
        "user": 1,
        "description": "developing payment endpoint",
        "project": 3
      }
-      Response{
        "id": 1,
        "is_running": true,
        "duration": "0:00:00",
        "description": "developing payment endpoint",
        "start_time": "2021-12-31T17:26:46.826450Z",
        "end_time": null,
        "project": 3,
        "user": 1
        }

Update a project activity:
-      Endpoint PATCH api/activity/update/1/
-      Authorization: Bearer <eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImEiLCJlbWFpbCI6ImFAZW1haWwuY29tIiwiZXhwIjoxNjQxMDUyMjI0fQ.unXe-dxoFCEY5l2VGkeRR8ue-Ggr6YxQS2nJUA63VZ4>
-      Request body:{
        "end_time": 2022-10-10,
        }
-      Response{
        "id": 1,
        "is_running": false,
        "duration": "2:00:00",
        "description": "developing payment endpoint",
        "start_time": "2021-12-31T17:26:46.826450Z",
        "end_time": "2021-12-31T19:26:46.826450Z",
        "project": 3,
        "user": 1
        }

delete a project activity:
-      Endpoint DELETE api/activity/delete/1/
-      Authorization: Bearer <eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImEiLCJlbWFpbCI6ImFAZW1haWwuY29tIiwiZXhwIjoxNjQxMDUyMjI0fQ.unXe-dxoFCEY5l2VGkeRR8ue-Ggr6YxQS2nJUA63VZ4>
-      Response{
        "message": "Project deleted successfully"
        }

Analytics endpoints:
These endpoints are used to get analytics data for a project and a user.
we can get the total time a user spent on a project, we can get the total time all project member spent on a project,
List time spent on a project by a user:
-      Endpoint get api/analytics/activity/duration/<int:user>/<int:project>'
-      Authorization: Bearer <eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImEiLCJlbWFpbCI6ImFAZW1haWwuY29tIiwiZXhwIjoxNjQxMDUyMjI0fQ.unXe-dxoFCEY5l2VGkeRR8ue-Ggr6YxQS2nJUA63VZ4>
-      Response{
        "total_time": "8 days, 11:08:10",
        "user": 1
        }

List time spent on a project by all project members:
-      Endpoint get api/analytics/activity/duration/<int:project>'
-      Authorization: Bearer <eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImEiLCJlbWFpbCI6ImFAZW1haWwuY29tIiwiZXhwIjoxNjQxMDUyMjI0fQ.unXe-dxoFCEY5l2VGkeRR8ue-Ggr6YxQS2nJUA63VZ4>
-      Response{
        "total_time": "30 days, 11:08:10",
        "project": 1
        }
  
<!-- ROADMAP
## Roadmap

- [] Feature 1
- [] Feature 2
- [] Feature 3
    - [] Nested Feature

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
<!-- ## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p> -->



<!-- LICENSE -->
<!-- ## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p> -->



<!-- CONTACT -->
<!-- ## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)

<p align="right">(<a href="#top">back to top</a>)</p> -->



<!-- ACKNOWLEDGMENTS -->
<!-- ## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#top">back to top</a>)</p> -->



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!-- [contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png --> 

<h4 align="center"> --> Thanks for checking out this projecr. <-- </h4>
