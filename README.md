# Winter-Hacklympics
## About The Project
The project uses PID to obtain filtered  values regarding the position of the  accelerometer/gyroscope(MPU6050)	as  feedback which it then uses to remain in  the calibrated position despite a  displacement. Servo motors have been  programmed to obey the microcontroller  based on the feedback received from the  gyroscope.

## REQUIREMENTS:
pip install opencv-python
pip install streamlit
pip install numpy==1.19.3

## EXECUTION:
The following were done on an Anaconda 3 environment on Windows OS
1. Navigate to the folder in which you have written your project and run --conda activate yourfoldername
2. After activating the conda environment, run --python test.py to get the stabilized output of your video.
3. If you want to run the web app, execute the following commands~
   --streamlit run test.py
4. The app opens up in Chrome browser with the URL as follows~
  Local URL: http://localhost:8501
  Network URL: http://192.168.29.97:8501

## DEPLOYED ON FIREBASE
Run the URL
https://stablympic-e6875.web.app/
