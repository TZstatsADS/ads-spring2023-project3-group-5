### A Note on Contributions

Whenever we have team projects, there are always concerns on unequal contributions from members of a project team. In the ideal world, we are all here to put in our best efforts and learn together. Even in that ideal world, we have different skill sets and preparations, and we will still contribute differently to a project. 

Therefore, you are required to post a *contribution statement* in the root README.md of your GitHub repo. Please beware that your GitHub repo will become public and remain public after the due date of the projects. 

Post your title, team members, project abstract and a contribution statement in the README.md file.  This is a common practice for research scientific journals. 

Below is an example. If no contribution statement is provided, we will insert a default statement that goes "**All team members contributed equally in all stages of this project. All team members approve our work presented in this GitHub repository including this contributions statement**. "

---

Project 3: Weakly supervised learning: label noise and correction

Team members: Yuxin Liang, Nixon Mckenzie, Safira Raharjo, Yi Sun, Yixun Xu, Haoyu Zhang

Summary: In this project, we conducted an analysis of weakly supervised learning on an imbalanced image dataset. For Model I, we used a pre-trained VGG model. We achieved around 35% validation accuracy by treating the noisy labels as clean ones. For Model II, 2 pre-trained VGG models were used, one for label correction as suggested by Inoue et al. (2017) to address the label noise issue, and corrected labels were used to train a final VGG model. We achieved around 70% validation accuracy, a significant improvement over the baseline model.

[Contribution Statement] Yuxin Liang, Nixon Mckenzie, Safira Raharjo, Yi Sun, Yixun Xu, and Haoyu Zhang all contribute in finding the best model for Model 1 and Model 2. By comparing the proformance of both model 1 and model 2 of everybody, we chose Yixun Xu's VGG for highest accuracy above 70%!

Yuxin Liang tried a KNN model on model 1 and obtained an accuracy around 19%. After compare to the model of Yixun Xu, I decided to use Yixun Xu's neural network model 1 as the base of my model 2. I utilized a CNN model as my label-cleaning model and the accuracy reached about 55%. After that, I redid the exactly same model as model 1 and gained the accuracy around 49%.

Nixon Mckenzie tried to utilize a pre model for model 1, and attempted a "pseudo- labeling" technique for model 2, which leveraged our groups designated model 1 to develop new labels for our initial model to be trained on, in order to increase it's accuracy. 

Safira Raharjo used a CNN model with cross-fold validation, which gave a 29% accuracy rate for model 1. When utilized for label cleaning however, the accuracy was reduced.

Yi Sun utilized the ResNet50 pre-model for model 1 and denoise the imbalance dataset by training models use co-teaching technique. Co-teaching is a fancy way to deal with noisy labels and Yi Sun shared it during the meeting. But two bad teachers cannot solve problems either, the best outcome is around 31%.

Yixun Xu utilized a single layer neural network for model 1 whcih obtained an accuracy around 23%. For model 2, used VGG 16 and neural networks to take noisy labels and images as input and clean labels as output. Label cleaning network has around 80% accuracy. Applied VGG 16 on the clean labels and correct noisy labels. Accuracy around 65%

Haoyu Zhang utilized a basic CNN model with keras for model 1 and obtained an accuracy around 15%. Label cleaning is achieved by adding convolutions and mobileNet and the accuracy on the clean images and labels is around 50%. Combining the clean data and the new predicted labels after label-cleaning, model 2 was able to get an accuracy of around 37%.

Thank you very much for everybody's effort and we have created a wonderful Image Classifier to classify images correctly.

