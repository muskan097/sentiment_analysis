# Sentiment Analysis

## Table of Content
  * [Overview](#overview)
  * [Technical Aspect](#technical-aspect)
  * [Demo](#demo)
  * [Directory Tree](#directory-tree)
  
 

## Overview
It is rightly said "Satisfied customer is the best source of advertisement".
Customer satisfaction plays a vital role within almost any business. Not only is it a leading indicator used to measure customer loyalty and retention, it enables businesses to identify unhappy customers, reduce customer losses.
What can be the best measure of their satisfaction. Of course, their own feedback.

In this project, we will try to analyse the customer reviews and separate them into tags: Positive and Negative. We have taken restaurant customers' reviews data. Reviews can tell you if you are keeping up with your customers’ expectations, which is crucial for developing marketing strategies



## Technical Aspect
The data in form of customers' reviews is unstructured. So to analyse this data, we need to sort it into structured form. 

Data Preprocessing: At first, the data is kept with only alphabet, all other numbers and special characters are replaced by blanks. Then, word with no meaning are removed called stopwords. NLTK has a list of stopwords. 
Next, the words are grouped together by removing the inflectional endings so they can be analysed as single term. At last, we used Tf-Idf vectorizer to transform text into a meaningful representation of numbers.

Training the model: Trained the structured data on Multinomial Naive Bayes. We got R squared value of 0.839 and MAE 1140. Saved the model into pickle file.

Deployment on Heroku: Deployed the model on Heroku platform connecting Github Profile.



## Demo
Link: [https://rev-sentiment-analysis.herokuapp.com/](https://rev-sentiment-analysis.herokuapp.com/)

[![](# Sentiment Analysis

## Table of Content
  * [Overview](#overview)
  * [Technical Aspect](#technical-aspect)
  * [Demo](#demo)
  * [Directory Tree](#directory-tree)
  
 

## Overview
It is rightly said "Satisfied customer is the best source of advertisement".
Customer satisfaction plays a vital role within almost any business. Not only is it a leading indicator used to measure customer loyalty and retention, it enables businesses to identify unhappy customers, reduce customer losses.
What can be the best measure of their satisfaction. Of course, their own feedback.

In this project, we will try to analyse the customer reviews and separate them into tags: Positive and Negative. We have taken restaurant customers' reviews data. Reviews can tell you if you are keeping up with your customers’ expectations, which is crucial for developing marketing strategies



## Technical Aspect
The data in form of customers' reviews is unstructured. So to analyse this data, we need to sort it into structured form. 

Data Preprocessing: At first, the data is kept with only alphabet, all other numbers and special characters are replaced by blanks. Then, word with no meaning are removed called stopwords. NLTK has a list of stopwords. 
Next, the words are grouped together by removing the inflectional endings so they can be analysed as single term. At last, we used Tf-Idf vectorizer to transform text into a meaningful representation of numbers.

Training the model: Trained the structured data on Multinomial Naive Bayes. We got R squared value of 0.839 and MAE 1140. Saved the model into pickle file.

Deployment on Heroku: Deployed the model on Heroku platform connecting Github Profile.



## Demo
Link: [https://rev-sentiment-analysis.herokuapp.com/](https://rev-sentiment-analysis.herokuapp.com/)

[![](<blockquote class="imgur-embed-pub" lang="en" data-id="a/oEoqYaU"  ><a href="//imgur.com/a/oEoqYaU"></a></blockquote><script async src="//s.imgur.com/min/embed.js" charset="utf-8"></script>)](https://flightsfareprediction.herokuapp.com/)



## Directory Tree 
```
├── static 
│   ├── css
│   ├── images 
├── templates
│   ├── home.html
│   ├── result.html
├── Procfile
├── README.md
├── app.py
├── Air Fare prediction.ipynb
├── sentiment.pkl
├── cv-transform.pkl
├── requirements.txt
```

)](https://flightsfareprediction.herokuapp.com/)



## Directory Tree 
```
├── static 
│   ├── css
│   ├── images 
├── templates
│   ├── home.html
│   ├── result.html
├── Procfile
├── README.md
├── app.py
├── Air Fare prediction.ipynb
├── sentiment.pkl
├── cv-transform.pkl
├── requirements.txt
```

