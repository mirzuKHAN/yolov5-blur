# yolov5-blur
Blur by Keyword

The idea of this project:
  You tell the programme what you want blurred (must include ChatGPT).
  If it detects objects that you specified (using YoloV5), it blurs them.

To date:
  For now it takes an image with a keyword from you and shows the result, where all the keyword objects are blurred.

To set up:
  Install requirements.txt in a Python>=3.8.0 environment, including PyTorch>=1.8. Models and datasets download automatically from the latest YOLOv5 release.
  
  pip install -r https://raw.githubusercontent.com/ultralytics/yolov5/master/requirements.txt 
  
  It is recommended that you have anaconda installed.
  Copy the .py file and your .jpg into the project. 
  Specify your keyword, and run it.

  This video might help: https://www.youtube.com/watch?v=fu2tfOV9vbY&t
