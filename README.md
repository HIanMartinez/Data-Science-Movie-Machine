# GA-Capstone

---

- [Introduction](#introduction)
- [The Data](#data)
- [The Method](#method)

---

<a id="introduction"></a>
## Introduction

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; This repository is my final project for General Assembly's 12-week Data Science Immersive program. The project puts together a tool, utilizing movie data, to make predictions of box office performance (measured in USD) and ratings on various platforms (Rotten Tomatoes, Metacritic, and IMDb) based on different selected factors (director, actors, genre). 
Feel free to create your own cast, director, and genres to see how your movie idea might perform!

<a id="data"></a>
## The Data

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The data behind the tool was put together by first downloading a dataset of titles and ratings from [IMDb](https://www.imdb.com/interfaces/). The dataset from IMDb is formatted with titles being in an ID format, [tt0335266](http://www.imdb.com/title/tt0335266/), which presents difficulties. The largest issue is that we don't know what movies these IDs are tied to. Similarly, other datasets have IDs for actors and actresses. To address this, I created a python package to interact with the [OMDb API](http://www.omdbapi.com/). A request to the OMDb API returns a JSON file structured like: ![OMDb JSON Return](https://github.com/HIanMartinez/GA-Capstone/blob/master/assets/Screen%20Shot%202018-04-06%20at%201.00.06%20PM.png)
It's a thing of beauty that's pretty well-structured for getting the appropriate elements and putting into a pandas DataFrame. 

Below are the elements of the dataframe:
* Actors 
* Awards
* Box Office Returns ($US)
* Country of Origin
* Genre
* Languages Released In
* MPAA Rating
* Metacritic Score
* Movie Title
* Short Plot
* Production Studio
* Release Date
* Rotten Tomatoes Score
* Runtime
* Writer(s)
* Year of Release
* IMDb ID
* IMDb Score

<a id="method"></a>
## The Method

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Linear regressions are used to predict box office returns and scores across Rotten Tomatoes, Metacritic and IMDb based on the inputs of actors, director, and genre. Below is the classic formula for multiple linear regression:
<p align="center">
<img width="300" height="25" src="https://github.com/HIanMartinez/GA-Capstone/blob/master/assets/CodeCogsEqn.png">
</p>
This is the essence of what will be happening behind the scenes of the tool. 
To get an idea of how the model will work with the data:
<p align="center">
<img width="550" height="20" src="https://github.com/HIanMartinez/GA-Capstone/blob/master/assets/CodeCogsEqnWords.png">
</p>
