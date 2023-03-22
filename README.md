# Project: Weakly supervised learning-- label noise and correction


### [Full Project Description](doc/project3_desc.md)

Term: Spring 2023

+ Group 5
+ Team members
	+ Liang, Yuxin
	+ Raharjo, Safira
	+ Sun, Yi 
	+ Xu, YiXun
	+ Zhang, Haoyu 
	+ Mckenzie, Nixon

+ Project summary: For this project, we created a neural network for model 1 and trained it on a percentage of our noisy label data set. For model 2, we addressed the noisy labels by creating a new model trained on only clean labels and then making predictions with this new model. We leveraged these predictions to develop a more reliable dataset which we then used to train model 1 on. This led to a more accurate overall model. 
	

**Contribution statement**: ([default](doc/a_note_on_contributions.md)) Each team member attempted a version of model 1 and model 2, and the group picked the best model for each stage and put them together to fit the criteria of the project. 

Following [suggestions](http://nicercode.github.io/blog/2013-04-05-projects/) by [RICH FITZJOHN](http://nicercode.github.io/about/#Team) (@richfitz). This folder is orgarnized as follows.

```
proj/
├── lib/
├── data/
├── doc/
├── figs/
└── output/
```

Please see each subfolder for a README file.
