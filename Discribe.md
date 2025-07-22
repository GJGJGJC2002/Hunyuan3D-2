## 混元3D生成项目

### 项目描述
这是一个原件生成的项目，从文字生成3D模型，再生成texture。这个项目可以补全我是否能够写出能够被PR的开源代码，并且补全我对于生成模型的未知感，提升企业级开源项目。

### 参考资料
- 项目
- 相关论文
- 相关综述

### 需求1：运行起Hunyuan项目

python310torch240安装了diffuser,transformers,pymeshlab,rembg,onnxruntime但是过程中发现没有内存了
尝试清理了内存：
```
df -h
du -sh ~/*
du -sh ~/Work/*
```
#### 7-22
75G     /home/gejunchen/Work/2024-10
188G    /home/gejunchen/Work/2024-11
47G     /home/gejunchen/Work/2024-7
14G     /home/gejunchen/Work/2024-9
226G    /home/gejunchen/Work/2025-2
2.9G    /home/gejunchen/Work/2025-4
24G     /home/gejunchen/Work/2025-6
写一个脚本删除全部tram结果下的images文件夹下的所有文件 /home/gejunchen/Work/2024-11/Baseline/tram/delete_imgs.py  
我想尝试直接一键从requirement中安装所有未安装的包，但是和GPT相聊发现并没有  
安装bpy(blend)的包速度非常慢且不稳定大小390M，还未完成，使用自定义源速度变快  
pip install bpy -i https://pypi.tuna.tsinghua.edu.cn/simple  
但是出现了这样的错误：ImportError: /home/gejunchen/anaconda3/envs/py310torch240/lib/python3.10/site-packages/bpy/__init__.so: undefined symbol: rtcIsSYCLDeviceSupported切换了源都无效，可能说明只能使用pip安装
突然间速度变快了成了1.1MB/s，但是安装后依旧不可用还是原来的问题，难道是缓存造成的？
百度说这个问题是因为先导入的pymeshlab包导致的，要是将pymenshlab后导入即可  
根据网上信息，bpy的安装直接使用pip即可，并且test_bpy.py验证了可用  

先注释了纹理生成的部分，到了模型下载的阶段
Try to load model from local path: /home/gejunchen/.cache/hy3dgen/tencent/Hunyuan3D-2.1/hunyuan3d-dit-v2-1
后台下载模型文件
nohup wget -c https://huggingface.co/tencent/Hunyuan3D-2.1/resolve/main/hunyuan3d-dit-v2-1/model.fp16.ckpt --progress=dot:mega > wgetmodel1.log &  
等待模型下载完成.......


