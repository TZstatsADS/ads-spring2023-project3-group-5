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

+ Project summary: Summary: In this project, we conducted an analysis of weakly supervised learning on an imbalanced image dataset. For Model I, we used a pre-trained VGG model. We achieved around 35% validation accuracy by treating the noisy labels as clean ones. For Model II, 2 pre-trained VGG models were used, one for label correction as suggested by Inoue et al. (2017) to address the label noise issue, and corrected labels were used to train a final VGG model. We achieved around 70% validation accuracy, a significant improvement over the baseline model.
	

**Contribution statement**: ([default](doc/a_note_on_contributions.md)) Each team member attempted a version of model 1 and model 2, and the group picked the best model for each stage and put them together to fit the criteria of the project. Yixun's model had the best result, and he tuned it until the final model was reached. Safira compiled the documentation and files into the final commit. 

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
