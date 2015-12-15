# TwitterTrendDetection
Twitter Trend Detection


## Project Structure

### ./codes/

#### ./codes/pipeline.py 
The pipeline python script to run the project

#### ./codes/modules/
Different modules responsible for different procedure of personalized trend generation

- config.py (all parameters like the input and output file name setting up here)
- data\_frame\_preprocess.py (process json file to data_frame and filter out non-english tweets)
- preprocess\_nlp.py (all nlp methods used to preprocess tweets)
- time\_explore.py (scripts that detect the duration of tweets data in terms of hour)
- background\_model.py (generate statistic model for training data and testing data)
- hot\_words\_generator.py (training and testing part to generate hotwords from training and testing data)
- hotwords\_statistic.py (script used to generate hotwords and tweets corresponding pairs)
- group\_burst.py (script that generate trends from hotwords with their corresponding tweet ids)
- personalize.py (LDA algorithm to extract topic from user profile and test data)
- recommend\_tweets.py (recommend tweets for specific user based on similarity between their LDA results)

#### ./codes/generateCSV 
Java code used to flatten the crawled data from the web

## ./file/
Training data(csv), testing data(csv) and all the generated files
The user profile we used are @JayZClassicBars, @KeyAndPeele, @realDonaldTrump, @taylorswift13.

The training and testing data we used are meaningly extracted from 2011, in terms of spliting data, training data must come before testing data because trends or events have orders.

### ./file/tweets 
The original tweets crawled using twitter API


If you'd like to run the whole program, you will need to specify the file names in the config.py and also specify the training data and test data file names in the pipeline.py. 

The whole program will run for several minutes and you can choose which part to run or not also in the pipeline.py.

