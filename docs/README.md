# MSLTNet
WACV 2024 (Official implementation of "4K-Resolution Photo Exposure Correction at 125 FPS with ~ 8K Parameters") [[arxiv](https://arxiv.org/abs/2311.08759)] [[Paper](https://openaccess.thecvf.com/content/WACV2024/html/Zhou_4K-Resolution_Photo_Exposure_Correction_at_125_FPS_With_8K_Parameters_WACV_2024_paper.html)]

## 
#### A quick glimpse of comparison on the ME dataset:
<div align="left">
<img src="https://github.com/Zhou-Yijie/MSLTNet/blob/main/fig1.jpg" height="150px" ><img src="https://github.com/Zhou-Yijie/MSLTNet/blob/main/fig2.jpg" height="150px" >
</div>


## Dependencies and Installation
```
# create new anaconda env
conda create -n mslt python=3.7 -y
source activate mslt

# install python dependencies
pip3 install -r requirements.txt
```
## Prepare Dataset
Download ME Dataset from [[Baidu Disk](https://pan.baidu.com/s/1tgVVLpZnUsm1pgi8Df63EQ?pwd=m7ai)] or [[google drive](https://drive.google.com/file/d/1dFqOrIdkPZ2seYRN-Hldl8B7tGWNurlM/view?usp=drive_link)] , unzip the file and put it in data/ 
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

---

## Process Videos

1. Copy the videos that you want to process using MSLT Network into `sample_video` folder.
2. Activate the `MSLT` virtual environment.
3. Run `python video_process.py` in the root directory.
4. Output video will be inside `sample_video/$video_name$/output_$video_name$` folder

---

## Results Comparison


https://github.com/user-attachments/assets/1c2ad226-7483-402c-948c-153abcfc4eab
