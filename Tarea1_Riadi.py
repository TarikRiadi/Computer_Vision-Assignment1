'''
Made by Tarik S. Riadi for Computer Vision 2019-10, 
Facultad de Ingeniería, Universidad de los Andes.
>> Make sure the original video is in the same folder as this script.
>> This script will apply the Anamorphus Temporallis effect to the input video.
>> Recomended max. resolution: Full HD (1920x1080) for time and memory constraints. 
   If you wish to try a higher resolution, make sure you have proper hardware. 
   You have been warned.
>> Take note of your video's file extension. If yours differs from .mp4, please 
   refer to the following website: http://www.fourcc.org/codecs.php   
'''

import cv2 #Version 4.0

def anamorphe(buffer,no_frames,resolution,tot_height,new_Vid):
    print('Creating new video...')
    for frame in range(0,no_frames-resolution):
        new_frame = buffer[frame] #Temporarily assign new frame
        for i in range(0,resolution-1):            
            new_frame[int((tot_height/resolution)*i):int((tot_height/resolution)*(i+1))] = buffer[frame+(resolution-i)][int((tot_height/resolution)*i):int((tot_height/resolution)*(i+1))]
        new_Vid.write(new_frame)

#---------------
# Manage Input.
#---------------        
print('Welcome to Anamorphe! Remember to write the video names with their corresponding file extension!')        
VideoName = input('Video Name: ')
new_VideoName = input('Anamorphous Video Name: ')
resolution = int(input('Resolution of the effect [default=100]: '))
rescale = input('Video resolution higher than 1080p? [y/n]: ')
#------------------------------------
# Read original video and its specs.
#------------------------------------
Vid = cv2.VideoCapture(VideoName)
buffer = [] #List to store the frames, acting as a buffer for the anamorphe function.
print('Reading input video...')
total_frames = int(Vid.get(cv2.CAP_PROP_FRAME_COUNT)) #Count total number of frames.
frames_per_second = int(Vid.get(cv2.CAP_PROP_FPS)) #fps of original video.
width, height = int(Vid.get(3)), int(Vid.get(4))
for i in range(0,total_frames):
    ret, frame = Vid.read()
    if rescale == 'y': #Rescale if video's resolution is greater than FullHD.
        if i == 0:
            print('Rescaling...')
        frame2 = cv2.resize(frame,(1920,1080),fx=0,fy=0,interpolation=cv2.INTER_CUBIC) #Resize resolution to HD.
        buffer.append(frame2)
    else:
        buffer.append(frame)
        
Vid.release() #Stop reading video.
#-------------------
# Create new video.
#-------------------
fourcc = cv2.VideoWriter_fourcc(*'MP4V') #http://www.fourcc.org/codecs.php
new_Vid = cv2.VideoWriter(new_VideoName, fourcc, frames_per_second, (1920,1080))
anamorphe(buffer, total_frames, resolution, height, new_Vid) #Create the effect on video.
#-----------------------------------------------
# Delete unecessary variables and close videos.
#-----------------------------------------------
print('Finishing...')
del buffer, fourcc, resolution
new_Vid.release()
cv2.destroyAllWindows() #Close Preview window.
print('All Done!')   
    