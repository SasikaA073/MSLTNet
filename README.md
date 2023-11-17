# MSLTNet
WACV 2024 (Official implementation of "4K-Resolution Photo Exposure Correction at 125 FPS with ~ 8K Parameters") [[arxiv](https://arxiv.org/abs/2311.08759)]

## 
#### A quick glimpse of comparison on the ME dataset:
<div align="left">
<img src="https://github.com/Zhou-Yijie/MSLTNet/blob/main/fig1.jpg" height="150px" ><img src="https://github.com/Zhou-Yijie/MSLTNet/blob/main/fig2.jpg" height="150px" >
</div>


## Dependencies and Installation
```
# create new anaconda env
conda create -n mslt python=3.7 -y
conda activate mslt

# install python dependencies
pip3 install -r requirements.txt
```
## Prepare Dataset
Download ME Dataset from [[Baidu Disk](https://pan.baidu.com/s/1tgVVLpZnUsm1pgi8Df63EQ?pwd=m7ai)] , unzip the file and put it in data/ 
## Quick Inference
```
# Inference On ME Dataset
python SingleTest.py
```
## Model Performance Testing
```
python test_model.py
```
## Train MSLT
```
python Train.py
```
## Citation
If this work is helpful for your research, please consider citing:
```
@inproceedings{zhou2024mslt,
  title={4K-Resolution Photo Exposure Correction at 125 FPS with ~8K Parameters},
  author={Zhou, Yijie and Li, Chao and Liang, Jin and Xu, Tianyi and Liu, Xin and Xu, Jun},
  booktitle={Winter Conference on Applications of Computer Vision (WACV)},
  year={2024}
}
```
