<div id="top"></div>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]




<!-- PROJECT LOGO -->
<br />

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
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a simple Email Auto Sender based on Gmail.
1) Set UP the script based on instructions below
2) Run the script
3) Enjoy AutoSending of your emails!

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://python.org/)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/turazashvili/Gmail-Auto-Sender.git
   ```
2. Install Python
   Choose latest release for your OS https://www.python.org/downloads/
3. Install all libraries one by one
     ```py
      pip install smtplib 
      pip install  csv
      pip install  time
      pip install os
     ```
     
4. Change the emails.csv file with Full Name and Emails list to whom you want to send.</br>
  ![image](https://user-images.githubusercontent.com/74835523/174792730-2373d84c-33bd-49bb-ab9b-03600988ba14.png)


5. <a href="https://support.google.com/mail/answer/185833?hl=en-GB" target="_blank" >Create the APP password in your gmail account.</a> 

6. Insert your email and password to lines 19 and 20

7. Edit your SUBJECT and fulltext in file.py 

5. Run the script
   ```py
    python mail.py
   ```
You will receive console.log when email is sent to each recipient.

<p align="right">(<a href="#top">back to top</a>)</p>

 

<!-- USAGE EXAMPLES -->
## Usage
![image](https://user-images.githubusercontent.com/74835523/174792639-7f8f4fcd-6b06-40a2-891e-742d18f15dff.png)






<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Add support for images and other media.
- [ ] Check for possible ways to avoid emails going to spam if overabused.


See the [open issues](https://github.com/turazashvili/Gmail-Auto-Sender/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project 
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Nikoloz Turazashvili - [@axrisi](https://twitter.com/axrisi) - turazashvili@gmail.com

Project Link: [https://github.com/turazashvili/Gmail-Auto-Sender/](https://github.com/turazashvili/Gmail-Auto-Sender/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/turazashvili/Gmail-Auto-Sender.svg?style=for-the-badge
[contributors-url]: https://github.com/turazashvili/Gmail-Auto-Sender/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/turazashvili/Gmail-Auto-Sender.svg?style=for-the-badge
[forks-url]: https://github.com/turazashvili/Gmail-Auto-Sender/network/members
[stars-shield]: https://img.shields.io/github/stars/turazashvili/Gmail-Auto-Sender.svg?style=for-the-badge
[stars-url]: https://github.com/turazashvili/Gmail-Auto-Sender/stargazers
[issues-shield]: https://img.shields.io/github/issues/turazashvili/Gmail-Auto-Sender.svg?style=for-the-badge
[issues-url]: https://github.com/turazashvili/Gmail-Auto-Sender/issues
[license-shield]: https://img.shields.io/github/license/turazashvili/Gmail-Auto-Sender.svg?style=for-the-badge
[license-url]: https://github.com/turazashvili/Gmail-Auto-Sender/blob/main/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/turazashvili
[product-screenshot]: images/screenshot.png
