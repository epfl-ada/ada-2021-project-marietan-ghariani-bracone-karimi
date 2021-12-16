# ADA 2021 Project
Authors: Raphael Marietan, Amine Ahmed Ghariani, Luca Bracone, Omid Karimi

# Natural disasters through quotes 

## Abstract
Natural disasters, such as earthquakes, hurricanes, floods and forest fires,
occur every year causing a lot of damage. In this project the goal is to observe
some of these disasters through the quotes of the Quotebank dataset and
reconstruct a map of natural disasters in the US that is comparable to what
really happend. Since the number of these phenomenon increases with each year,
it is vital to take meaningful actions to protect the people and the
infrastructures. Climate change is also a relevant problematic, and we would like
to see if its occurrence in discussion has increased or decreased over the
years, and what is the political affiliation of those who mention it. In fact,
we noticed that politics is a highly relevant factor, given that the most
frequently occurring speakers are politicians.
TODO

## Research Questions
TODO
- Can natural disasters be observed through the quotes of the Quotebank dataset ?
- Is it possible to recreate a spatial and temporal map of natural disasters with the quotes, that is close to what really happend ?
- Does the speakers and quotes semantic help us conclude something on the involvments concerning disaters handling or climate ? 

## Additional datasets
- Natural disasters in US: </br >
https://www.kaggle.com/headsortails/us-natural-disaster-declarations </br >
This dataset contains all natural disasters in the US from 1953 to 2021, with most notably the exact date, location and type of disaster. It can be used to compare with the outcome of our observations on the natural disasters through the quotes. </br >

- International, maybe better/more precise: https://www.emdat.be/ </br >
Main natural disasters that occured in the world.


## Methods
#### 1. Data loading and handling

* This step is mostly done in Milestone 2. First, we find a ground truth dataset
containing all natural disasters from past year. This will help us to generate a
small curated dictionary used to extract relevant quotations from the Quotebank
dataset using the Google Colab notebook, and also verify that we can correctly
recreate a map of what happend. 
* We compute some basic statistics relating to each of the two datasets, like
the number of available quotes per type of incidents, how many
incidents/quotes with respect to the date, etc... Also, we draw some plots for a
better understanding and visualization. Since we are able to find some
informations about the places of the disasters, we can conclude that the main
part of the project we intend to do is feasible.

The code is present in the notebook `project.ipynb`.

#### 2. Recreating a map
The main part of the project consist in constructing a map of natural
disasters in the US through their occurences in the quotes. The idea is to
build maps for fixed time periods, where we show the location and type of crisis
that happend. Through the number of quotations citing the natural disaster and a
particular location, we can deduce the chance that there was indeed a
catastrophe that occured. We think that building the map by state will be
easier, since it is quite hard to pinpoint a location through the quotes alone,
but from what we can observe it is still feasible. The final goal would be to
have a yearly (or for six months) map of the US, with the state borders, where
we can see different types of disasters in different colors and their location.

#### 3. Analyze speakers affiliation
TODO
For the last part, we will look more in depth at the quotations and their speakers. Indeed, we find mainly politicians in the speakers, and it would be interesting quickly to have a look at their opinions and affiliations. For this purpose, we need to work with another dataset (Wikidata as recommended in the description), but might have to look for some informations about speakers manually. Whether some actions were taken for the protection of the people, infrastructures or the environment could also be interesting, but might be too ambitious.</br >
We will developp these ideas in more details for the next milestone, because it is still unsure exactly what aspect we want to work on. 

## Timeline and organization
| Week number | Actionable items                                               | Assignment      |
|-------------|----------------------------------------------------------------|-----------------|
| Week 1-2    | Homework 2 + clearer outline of step 3                         | Everyone        |
| Week 3      | Generate maps                                                  | Raphael + Amine |
| Week 4      | Analysis of speaker (political affiliation) + begin data story | Omid + Luca     |
| Week 5      | Write data story                                               | Everyone        |
