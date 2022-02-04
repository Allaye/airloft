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
  <a href="https://github.com/allaye/airloft">
    <!-- <img src="images/logo.png" alt="Logo" width="80" height="80"> -->
  </a>

<h3 align="center">Trakar</h3>

  <p align="center">
    This is an flight tracker for airline<br />
    <!-- <br />
    <a href="https://github.com/github_username/repo_name"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/github_username/repo_name">View Demo</a>
    · -->
    <a href="https://github.com/allaye/airloft/issues">Report Bug</a>
    ·
    <a href="https://github.com/allaye/airloft/issues">Request Feature</a>
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

This is a flight tracker for airline,the application keeps track of flight departure and arrival date and time. with this app you can track the time airports activity.

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

1. Clone the repo using: git clone https://github.com/allaye/airloft.git
2. Navigate into the directory containing the project: cd airloft
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

      -[x] Create New Aircraft (can only be created by an admin)
          * POST /api/create/aircraft/
            request body:{
                "manufacturer": "Boeing",
                "model": "7X7",
                "name": "gh1"
            }
            response object:{
                 "id": 4,
                "name": "gh1",
                "serial_number": "cba54b0f-2c82-47f9-a49d-9b4b30bdb558",
                "manufacturer": "Boeing",
                "model": "7X7"
            }
      -[x] Get all Aircrafts
          * GET /api/aircraft/
            response object:{
                "projects": [
                    {
                        "id": 1,
                        "name": "airforce 1",
                        "serial_number": "e73cfd62-7f5a-424f-96e1-18d22792e4a8",
                        "manufacturer": "Airbus",
                        "model": "Airbus A350"
                 },
                     {
                        "id": 2,
                        "name": "lighten",
                        "serial_number": "e0927ea6-2eee-46da-af27-3f1d6b1ad8d1",
                        "manufacturer": "Airbus",
                        "model": "Airbus A310"
                 },
                ]
            }
    - [x] Airport endpoints
        
        -[x] Create New Project Activity
            * POST /api/create/airport/
              request body:{
                    "location": "Albany",
                    "name": "Albany International"

              }
              response object:{
                
                    "id": 4,
                    "location": "Albany",
                    "name": "Albany International",
                    "code": "KBAL"

              }
        -[x] Get all Airport
            * GET /api/airport
              response object:{
                  "activities": [
                       {
                        "id": 1,
                        "location": "South Africa",
                        "name": "Malamala",
                        "code": "FAMD"
                    },
                    {
                        "id": 2,
                        "location": "United State",
                        "name": "Atlantic City",
                        "code": "KACY"
                    },
                  ]
              }

<p align="right">(<a href="#top">back to top</a>)</p>
<!-- 

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
