# TwitterTrendDetection
Twitter Trend Detection

The structure of the project:
1.codes python code
	----pipeline.py the pipeline python script to run the 		project
	----modules different modules responsible for different 	procedure of personalized trend generation
		----config.py all parameters like the input and 		output file name setting up here
		----data_frame_preprocess.py process json file to data_frame and filter out non-english tweets
		----preprocess_nlp.py all nlp methods used to 			preprocess tweets
		----time_explore.py scripts that detect the duration of tweets data in terms of hour
		----background_model.py generate statistic model 		for training data and testing data
		----hot_words_generator.py training and testing part 	 to generate hotwords from training and testing 	data
		----hotwords_statistic.py script used to generate 		hotwords and tweets corresponding pairs
		----group_burst.py script that generate trends from 	hotwords with their corresponding tweet ids
		----personalize.py LDA algorithm to extract topic from user profile and test data
		----recommend_tweets.py recommend tweets for specific user based on similarity between their LDA results
---file
	training data(csv), testing data(csv) and all the generated files

	The user profile we used are @JayZClassicBars, @KeyAndPeele, @realDonaldTrump, @taylorswift13.

	The training and testing data we used are meaningly extracted from 2011, in terms of spliting data, training data must come before testing data because trends or events have orders.
----tweets
	the original tweets crawled using twitter API
----generateCSV
	java code used to flatten the crawled data from the web

	If you'd like to run the whole program, you will need to specify the file names in the config.py and also specify the training data and test data file names in the pipeline.py. 

	The whole program will run for several minutes and you can choose which part to run or not also in the pipeline.py.

