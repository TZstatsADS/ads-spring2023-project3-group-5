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

+ Project summary: Summary: In this project, we conducted an analysis of weakly supervised learning on an imbalanced image dataset. For Model I, we used a more sophisticated model than the baseline and experimented with pre-trained neural network models such as VGG and ResNet. We achieved around 40% accuracy by treating the noisy labels as clean ones. For Model II, we decided to continue the usage of VGG in Model I and added a label correction method suggested by Inoue et al. (2017) to address the label noise issue. We achieved around 70% accuracy, a significant improvement over the baseline model.
	

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
