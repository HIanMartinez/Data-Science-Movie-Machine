# GA-Capstone

---

- [Introduction](#introduction)
- [The Data](#data)
- [The Method](#method)
- [The Results](#result)
---

<a id="introduction"></a>
## Introduction

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; This repository is my final project for General Assembly's 12-week Data Science Immersive program. The project puts together a tool, utilizing movie data, to make predictions of box office performance (measured in USD) and a Rotten Tomatoes score based on different selected factors (director, actors, genre). 
Feel free to create your own cast, director, and genres to see how your movie idea might perform!

<a id="data"></a>
## The Data

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The data behind the tool was put together by first downloading a dataset of titles and ratings from [IMDb](https://www.imdb.com/interfaces/). The dataset from IMDb is formatted with titles being in an ID format, [tt0335266](http://www.imdb.com/title/tt0335266/), which presents difficulties. The largest issue is that we don't know what movies these IDs are tied to. Similarly, other datasets have IDs for actors and actresses. To address this, I created a python script to interact with the [OMDb API](http://www.omdbapi.com/). A request to the OMDb API returns a JSON file structured like: ![OMDb JSON Return](https://github.com/HIanMartinez/GA-Capstone/blob/master/assets/Screen%20Shot%202018-04-06%20at%201.00.06%20PM.png)
It's a thing of beauty that's pretty well-structured for getting the appropriate elements and putting into a pandas DataFrame. 

Below are the features of the dataframe:
* Actors (String)
* Directors (String)
* Awards (String) 
* Country of Origin (String)
* Genre (String)
* Languages Released In (String)
* MPAA Rating (String)
* Movie Title (String)
* Short Plot (String)
* Production Studio (String)
* Release Date (String)
* Runtime (Integer)
* Writer(s) (String)
* Year of Release (Integer)
* IMDb ID (String)

Target Features:
* Box Office Returns in $US (Integer)
* Rotten Tomatoes Score (Float)
* IMDb Score (Float)

<a id="method"></a>
## The Method

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Linear regressions are used to predict box office returns and scores from Rotten Tomatoes and IMDb based on the inputs of actors, director, and genre. Below is the classic formula for multiple linear regression:
<p align="center">
<img width="300" height="20" src="https://github.com/HIanMartinez/GA-Capstone/blob/master/assets/CodeCogsEqn.png">
</p>
This is the essence of what will be happening behind the scenes of the tool. 

To get an idea of how the model will work with the data:
<p align="center">
<img width="600" height="20" src="https://github.com/HIanMartinez/GA-Capstone/blob/master/assets/CodeCogsEqnWords.png">
</p>
Actors, Directors, and Genre have been made into dummy variables. 1 if the element is present, 0 if not. For example, Zombieland would have 1 for Emma Stone, 0 for Emma Watson; 1 for comedy, 0 for drama. A model is trained with Box Office Returns, Rotten Tomatoes Score, and IMDb Score as target variables. The dummy variables will act as inputs for the predictive model, returning the predicted returns and scores for the target variables.
<br><br>
Additionally, Random Forest Regression is used as another model to test for the same as above. The image below gives an idea of how Random Forest Regression arrives at its prediction:

<p align="center">
<img width="450" height="400" src="https://github.com/HIanMartinez/GA-Capstone/blob/master/assets/randomforestimg.png">
</p>

<a id="result"></a>
## The Results

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Using data science and predictive models, we can guess how a movie might perform at the box office or with critics! Of course this isn't foolproof and having more data and greater tuning would help boost the predictive power of the models. But this project highlights the amalgam of using data science and having fun! <br><br>
This repo will be updated with the script that you can use for choosing your own cast, director, and genres soon!
