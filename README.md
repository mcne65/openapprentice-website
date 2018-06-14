![OpenApprenticeFoundationLogo](/openapprentice/static/images/openapprentice-foundation-logo.png)


# The OpenApprentice Foundation
[![GitHub last commit](https://img.shields.io/github/last-commit/OpenApprenticeFoundation/openapprentice-website.svg)](https://github.com/OpenApprenticeFoundation/openapprentice-website/commits/master)
[![GitHub commit activity the past week, 4 weeks, year](https://img.shields.io/github/commit-activity/w/OpenApprenticeFoundation/openapprentice-website.svg)](https://github.com/OpenApprenticeFoundation/openapprentice-website/commits/master)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

oA (OpenApprentice) is a new look on solving a very specific problem:

How to get people the exact experience necessary to achieve competence in any given domain; and in gaining that competence, achieve it in an effecient, personalized and verifiable manner?

The world today has the technology to solve nearly all problems.  From education, to medicine, to space travel and entertainment. From economic disparity within and between countries to income inequility between the the very poorest to the very richest. From agriculture to self-driving vehicles.  The technology exists or the know-how exists to apply the existing technologies to these problems.

What we are missing are enough competent technicians, leaders, teachers and programmers. We are missing problem solvers, independent thinkers, scientists and artists. And so OpenApprentice is founded to provide a very real and useable path for those willing to apprentice, learn, teach and gain the experience necessary to accomplish the solutions within a company they are hired to work for or to start their own company or activity in the accomplishment of their unique visions.

OpenApprentice was created on the premise that competence, ability to learn, teach and lead, proven reliability and proven performance are alone the measure of ones value to a company and to society. That with these requisites, one's age, color, sex, and even geographic location (in most cases) should not determine or influence the value to any given project, organization or company.

We believe that when workers have options and know they have options within and for their careers, that this freedom alone permits for the best and most humane contribution. With that freedom and choice of where and who to work for, more good than evil will be affected. For our basic premise and empirically evident, is that the overwhelming majority of human beings are good and well intentioned, and these, the good and well intentioned should not fall prey to the whims of the smallest minority.


## The OpenApprentice Website

[OpenApprentice Foundation's Website](https://www.openapprentice.org)

[OpenApprentice's Twitter](https://twitter.com/open_apprentice)

[OpenApprentice Foundation's Github](https://github.com/OpenApprenticeFoundation)


## You can help - contributing to OpenApprentice

We are looking for people who share a similar vision and want to help:

+ Do you want to teach others a subject that you are passionate about?
+ Are you a Python developer for web or data science that has a lot or a little free time to help?
+ Have you built a Rasa based chatbot?
+ Are you familiar or want to get more experience with machine learning?
+ Are you a teacher of mathematics?
+ Do you have an interest in developing or have skills using blockchain technology?
+ Do you know Vue.js?
+ How about Public Relations and marketing?

The above are certain skills we are in need: for teachers (of any discipline), for people who want to learn and gain experience, and for supervisors and experts (with perhaps less time) who can "look over the shoulder, QC and mentor" in these above areas.


## What we are building

+ The OpenApprentice.org website itself - current progress can be followed here: [OpenApprentice Github](https://github.com/OpenApprenticeFoundation/openapprentice-website) - this is a Python Flask based website using Vue.
+ The oA teaching module, called "With Students" - many experts in many technical fields are willing to teach others. A methodology on how to teach and the software to implement such a method is being adopted here in oA. We are finishing plans for a upgradable, self-adapting and personalized teaching module to helps students learn any given skill at the exact level of knowledge they require to become competent in that skill. We are solving the problem of tutorials, books, courses and instruction that is either too advanced or too basic for the exact student studying at that exact moment in their career and education. More importantly, we are insisting on an application of the materials to specific problems. This is in the final planning stages.
+ A highly integrated chatbot using the Open Source Rasa stack. Consider this chatbot to be at once guide, problem solver, and communications agent.  The rasa chat platform can be found at this link: [Rasa Stack](https://rasa.com/products/rasa-stack/)


## Code of Conduct

We are developing a Code of Conduct unique to OpenApprentice but inspired by the leadership of such organizational examples, including [Python](https://www.python.org/psf/codeofconduct/), [Ubuntu](https://www.ubuntu.com/community/code-of-conduct) and others who have come before us with their examples and built purposeful thriving and effective organizations and communities.


## Translating

We are always in search for new languages to support !
Please follow the [Babel Tutorial](https://pythonhosted.org/Flask-Babel/#translating-applications).

### To update existing translation
First, Clone the repository and go into it.
Then,  You need to extract the strings to translate:
```bash
pybabel extract -F babel.cfg -o messages.pot .
```
Once extracted, merge the translations to update if some strings are missing:
```bash
pybabel update -i messages.pot -d openapprentice/translations
```
Then, you can start updating your desired translation in `openapprentice/translation/<lang_code>/LC_MESSAGES/messages.po`

Once done, Compile your changes with
```bash
pybabel compile -d openapprentice/translations
```
And test them. Once you are sure everything works push the updated `messages.po` to a new branch and start a PR!

### To create a new translation
Clone the repository and `cd` into it.

You first need to extract the strings to translate:
```bash
pybabel extract -F babel.cfg -o messages.pot .
```

Then, Initialize a new supported language by running
```bash
pybabel init -i messages.pot -d openapprentice/translations -l LANG_CODE
```
With `LANG_CODE` being the language code. Example: `fr` for French or `de` for German

You can now start translating the file located in `openapprentice/translation/<lang_code>/LC_MESSAGES/messages.po`.
Once done, make sure you add a flag for the language you edited to `openapprentice/static/images/flag-<lang_code>.png`
and edit the file `lang.ini`.

Once all of this is done, push this to a new branch and start a PR !

## Founded by David Kartuzinski

Founded in April 2018 to accomplish the aforementioned goals, and definitely not Founded alone.


## License

We continue to receive advice as to the best license for our project. We intend for our software and platform to be Open Sourced and available to anyone in their efforts to improve their fields of interest. For this reason we have adopted License GPL v3.

June 5, 2018

[GNU General Public License v3.0](https://github.com/OpenApprenticeFoundation/openapprentice-website/blob/master/LICENSE)










