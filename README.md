# invoiceocr
Invoice Ocr Parser POC
This implementation is tested on Ubuntu
You need to install openCV, 
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install build-essential checkinstall cmake pkg-config yasm
sudo apt-get install git gfortran
sudo apt-get install libjpeg8-dev libjasper-dev libpng12-dev

pip install numpy scipy matplotlib scikit-image scikit-learn ipython
git clone https://github.com/opencv/opencv.git
cd opencv 
git checkout 3.3.1 
cd ..
git clone https://github.com/opencv/opencv_contrib.git
cd opencv_contrib
git checkout 3.3.1
cd ..
cd opencv
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
      -D CMAKE_INSTALL_PREFIX=/usr/local \
      -D INSTALL_C_EXAMPLES=ON \
      -D INSTALL_PYTHON_EXAMPLES=ON \
      -D WITH_TBB=ON \
      -D WITH_V4L=ON \
      -D WITH_QT=ON \
      -D WITH_OPENGL=ON \
      -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \
      -D BUILD_EXAMPLES=ON ..
 sudo apt-get install python-opencv
 
 Install the Tesseract
 sudo apt install tesseract-ocr
 pip install pytesseract
