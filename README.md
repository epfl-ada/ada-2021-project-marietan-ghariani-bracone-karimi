# ADA 2021 Project
Authors: Raphael Marietan, Amine Ahmed Ghariani, Luca Bracone, Omid Karimi

# TITLE HERE

## Abstract
Natural disasters, such as earthquakes, hurricanes, floods and forest fires, occur every year causing a lot of damage. In this project the goal is to observe some of these disasters through the quotes of the Quotebank dataset and reconstruct a map of natural disasters in the US that is comparable to what really happend. It is indeed interesting, since the numbers of these phenomenon increases with the years, talks about actions taken for protecting the people and the infrastructures (<- TODO better wording?) and also the problematic of climate change are more abundant. These subjects are quite political and can be easily seen in the quotations dataset. ... DEVELOPP MORE (can still do ~70 words)

## Research Questions
- Can natural disasters be observed through the quotes of the Quotebank dataset ?
- Is it possible to recreate a spatial and temporal map of natural disasters with the quotes, that is close to what really happend ?
- Does the speakers and quotes semantic help us conclude something on the involvments concerning disaters handling  or climate ? (<- TODO better wording?)

## Additional datasets
Natural disasters in US, seems easy to use </br >
https://www.kaggle.com/headsortails/us-natural-disaster-declarations </br >
International, maybe better/more precise
https://www.emdat.be/ </br >

This dataset contains all natural disasters in the US from 1953 to 2021, with most notably the exact date, location and type of disaster. It can be used to compare with the outcome of our observations on the natural disasters through the quotes.

## Methods
#### 1. Data loading and handling
This step is mostly done in Milestone 2. First, we find a ground truth dataset containing all natural disasters from past year. This will help us to generate a small dictionary used to extract relevant quotations from the Quotebank dataset using the Google Colab notebook, and also verify that we can correctly recreate a map of what happend. </br >
We compute some basic statistics the two datasets, like the number of available quotes per type of incidents, how many incidents/quotes with respect to the date, etc... Also, we create some plots for a better understanding and visualization. We can conclude that the main part of the project we intend to do is feasible. </br >
The code is present in the notebook ```project.ipynb```.
#### 2. Recreating a map
The main part of the project consist in contructing a map of natural catastrophies in the US through their occurences in the quotes. The idea is to work with one type of crisis at a time and build a map ... ???????????????

## Timeline and organization
TODO
