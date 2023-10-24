# MixSegNet
Mixed Supervised Learning for Medical Image Segmentation

## Requirements
* Pytorch
* Some basic python packages such as Numpy, Scikit-image, SimpleITK, Scipy ......

## DataSets
We use the ACDC dataset which you can find here [Official](https://www.creatis.insa-lyon.fr/Challenge/acdc/databases.html). The pre-processed dataset i.e. scribble is with this GitHub Respository, and you can also simulate the scribble annotations with other dataset with the 'code/scribbles_generator.py' file.


## Usage

1. Clone the repo:
```
git clone https://github.com/ziyangwang007/MixSegNet.git 
cd MixSegNet
```


2. Train the model
```
cd code
```

```
python train_MixSegNet.py 
```

3. Test the model

```
python test_2D_fully.py 
```


## Semi-Supervised Baseline Methods
CV-SSL-MIS
![Github stars](https://img.shields.io/github/stars/ziyangwang007/CV-SSL-MIS.svg)<br>

## Weakly-Supervised Baseline Methods
CV-WSL-MIS
![Github stars](https://img.shields.io/github/stars/ziyangwang007/CV-WSL-MIS.svg)<br>

## Reference

TBC