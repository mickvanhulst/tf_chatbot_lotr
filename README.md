#Tensorflow Chatbot
Tensorflow Chatbot Demo by @Sirajology on [Youtube](https://youtu.be/SJDEOWLHYVo)

Overview
============
This is the full code for 'How to Make an Amazing Tensorflow Chatbot Easily' by @Sirajology on [Youtube](https://youtu.be/SJDEOWLHYVo). In this demo code, we implement Tensorflows [Sequence to Sequence](https://www.tensorflow.org/versions/r0.12/tutorials/seq2seq/index.html) model to train a
chatbot on the [Cornell Movie Dialogue dataset](https://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html). After training for a few hours, the bot is able to hold a fun conversation.


Dependencies
============
* numpy
* scipy 
* six
* tensorflow (https://www.tensorflow.org/versions/r0.12/get_started/os_setup.html)

Use [pip](https://pypi.python.org/pypi/pip) to install any missing dependencies


Usage
===========

Simply run 'python3 main.py' and your sentences are on the way!


Challenge
===========

The challenge for this video is write an entirely different script using [TF Learn](http://tflearn.org/) to generate Lord of the Ring style sentences. Check out this very similar [example](https://github.com/tflearn/tflearn/blob/master/examples/nlp/lstm_generator_shakespeare.py), it uses TF Learn to generate Shakespeare-style sentences. Train your model on Lord of the rings text to do something similar! And play around with the hyperparameters to get a more accurate result. Post your GitHub link in the video comments and I'll judge it! 

Result
===========
The sentences generated weren't very.. Hmm how do you say it? Intelligent? I've listed some below and you probably agree with me. To be honest I didn't expect much of it, but it was fun transforming the code into something that works with other data as well.

Example of output:
*about it and the heavy she beukais 'geiloau
th lo
tees h rfe ouod anherh Bis wg deeatas!er Taat Cn miiand wheut cpenoryem, fanat mesres owea
isrighe wise t ts  ore v ratm ta wd iaudlerrd teek fr ohe ntodd ton Eomeedeiawod nh rd.s te bsel pouboniat.ek Wede rh  on oe de h toes we ouopiueuteeo  ih aandee nme .e ̂e nh sorar DneoWed noord qkeacm? fas
rw'khe n -asor nh gw Gfes Ch nonD roih la fhen bh ileimrn rhot lhide Tol gt wamig thiw weurederolr rodeuner uy s gise nor yl w daeteemgadeav har rh w S th faaf ahed rger any.ed ds vit aaorahraseo-r naud hoewi'np lt n uwr nti riade di tkd! te 
usid ihe,e bg fh ca oag wd ahosola*


The sentence does match the [video](https://www.youtube.com/watch?v=9U2pINNSpHE) Sirajology showing at the end of his video xD. 

P.S. the entire list of sentences is in the 'the_awesome_lotr_sentences_file.txt' file!

Credits
===========
Credit for the vast majority of code here goes to [suriyadeepan](https://github.com/suriyadeepan). I've merely created a wrapper to get people started. 

Credits for being awesome go to @[Sirajology](https://www.youtube.com/sirajology) for enabling us to learn so much about ML!
