# ADA 2021 Project
Authors: Raphael Marietan, Amine Ahmed Ghariani, Luca Bracone, Omid Karimi

# Natural disasters through quotes

## Data story
[Link to the data story](https://omidou.github.io/Natural-disasters-through-quotes/)

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

## Research Questions
- Can natural disasters worldwide, like hurricanes, earthquakes and others, be observed through the quotes of politicians and researchers in the Quotebank dataset ?
- Is it possible to recreate a spatial and temporal map of natural disasters with the quotes, that is close to what really happend ?
- Does the vocabulary or topic used by the speakers give us hinsight on their occupations or political affiliation

## Additional datasets
- Natural disasters in US: </br >
https://www.kaggle.com/headsortails/us-natural-disaster-declarations </br >
This dataset contains all natural disasters in the US from 1953 to 2021, with most notably the exact date, location and type of disaster. It can be used to compare with the outcome of our observations on the natural disasters through the quotes. </br >
- Main natural disasters that occured in the world: https://www.emdat.be/ </br >
- Wikidata information for the speakers present in QuoteBank: provided ```parquet``` [file](https://drive.google.com/drive/folders/1VAFHacZFh0oxSxilgNByb1nlNsqznUf0).

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

The code is present in the notebook `milestone2_backup.ipynb`.

#### 2. Recreating a map
The main part of the project consist in constructing maps of natural
disasters worldwide and in the US through their occurences in the quotes. The idea is to
build maps for fixed time periods, where we show the location and type of crisis
that happend. Through the number of quotations citing the natural disaster and a
particular location, we can deduce the chance that there was indeed a
catastrophe that occured. We think that building the map by state (for the US) will be
easier, since it is quite hard to pinpoint a location through the quotes alone,
but from what we can observe it is still feasible. The final goal would be to
have yearly (or for six months) maps of the US, or of the world where
we can see different types of disasters in different colors and their location.

#### 3. Analyze speaker quotes and vocabulary
For the last part, we will look more in depth at the quotations and their speakers. We will try various methods of machine learning and text handling seen in class. At first, the goal would be to detect the topics present in the speeches of the speakers and then using regression, we could try to build a model to determine wheter the speaker is a politician or another influencial person (in the case of natural disasters, mostly reseachers). For this purpose, we need to work with another dataset (Wikidata as recommended in the description), but might have to look for some informations about speakers manually. </br>
We will also try other methods to see if they can give us other meaningful hinsights (sentiment analysis, other regressions, ...)

## Repository
- ```figures/``` contains plots and interactive plots
- ```interactive_maps/``` contains the maps and the code to create them
- ```milestone2_backup.ipynb``` is the notebook from Milestone 2
- ```project.ipynb``` is the final notebook for Milestone 3

### Summary of content for the project notebook
- Data loading and cleaning of the datasets
- Data visualisation
- Examples of methods helping to create maps
- Speaker analysis
  - Topic detection in quotes
  - Regression to predict occupations of speakers
  - Regression to predict speakers political affiliation
  - Sentiment analysis

Note: Not all analysis were conclusive and might not be present in the data story.

## Timeline and organization
| Week number | Actionable items                                               | Assignment      |
|-------------|----------------------------------------------------------------|-----------------|
| Week 1-2    | Homework 2 + clearer outline of step 3                         | Everyone        |
| Week 3      | Generate maps                                                  | Raphael + Amine |
| Week 4      | Analysis of speaker (political affiliation) + begin data story | Omid + Luca     |
| Week 5      | Write data story                                               | Everyone        |
