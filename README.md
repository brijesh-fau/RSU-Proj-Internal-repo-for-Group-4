# RSU-Proj-Internal-repo-for-Group-4
## Bringing SENSATION components together
In this task, we have to combine all the tasks that we have done so far.<br>
Follow the below structure for your code:-
- [x] Convert model in onxx file <br>
Model: https://faubox.rrze.uni-erlangen.de/getlink/fiCPd3E5ruvMuJDXMbSXpK/final_model.pt <br>
Onxx mode: https://faubox.rrze.uni-erlangen.de/getlink/fiSRB89HXMgJy6ACMsMhnS/model.onnx <br>
- [ ] Write code in init__main__ as classes and define methods in those classes.
- [ ] Write a common rsu_vi.py file
- [ ] This file will take three inputs: input_video / images, gpxFile_path, OutputPath

### Road Map:
1. The user will give us input as a video, image, or camera. GPX file. Output Path
2. First, If the input are images, we will pass them through our model, then analysis.py which will return an instruction, we will write that instruction on the video and return those images in the output path.
3. If it is a video, we will first set them into frames, do task 2, combine them back into a video, get instructions from Valhalla using GPX file, and write them on the input video. In the end, will save it into the output path.

## Task Distribution:
### Sahil: Handling Model:
I will handle the input video, convert them into frames, pass them through our model, print model instructions, write those instructions on the images, and combine them again into a video.

### Firoz: Handling Input with Classes:
You will handle input, what with happen when we get input as images, video, or as camera. Your main task is to handle how these files will go through and how we can use classes effectively.

### Brijesh: Handling Frames:
You will test the frames of the video images. First, you shoot a small video and convert it into frames. Combine them and set a time elapsed on the video which will run per sec when we play the output video. This will help us to make sure that our frames are passing with each second as we have in the input video. After this, you will work with Antara to write those instructions on the video.

### Antara: Handling Instructions:
You will estimate the walking speed using the gpx file that we have. You can use the haversine library to calculate the speed. You will also collect the walking instructions from Valhalla and save the following input that we will use to show on our output video.
1. Walking speed
2. Lat and Lon
3. Time elapsed
4. Current street name
5. Distance left

When we are done with our task, we will combine all these tasks and give credits in the readme file for our contribution to this task.
