# LoopClosureGPS
Finding loop closures for a closed track for Formula Student events like FSG, FSA, FS East and many more using data-points provided by GPS.

## Formula Student
Formula Student is a body that governs and holds competitions for university students from all over the world to build, showcase and compete with FS styled cars. These events include various different different events for various different vehicle categories such as Combustion Vehicle (CV), Electric Vehicle (EV) and Driverless Vehicle (DV).

## Some info about DV and autonomous vehicles in FS
Out of these, DV is a relatively new event and requires the team to build a completely autonomous car that works solely based on sensor data. Some of these sensors include GPS, LIDAR, RADAR, GYROSCOPES and cameras.
Thus this repo discusses the use of GPS data to form a track layout and get rid of discrepancies between the starting point and the ending points; which often do not coincide; leading to an open or broken track layout.


## Original track layout
Here, I've picked up a random track layout.

![test1 (1)](https://user-images.githubusercontent.com/82220795/177352874-9b851af0-f790-4a67-b8c1-3e8d7715fe27.jpg)

From this image, I extracted the co-ordinates from the image itself using OpenCV and mousecallback functions since I actually lacked original GPS data. However, the code shall still be functional if we use real GPS data values; all we need to do is change the base CSV file with the new file.

## Faulty data
As mentioned earlier, often the starting and ending co-ordinated of the lap differ by a few meters due to factors such as sensor accuracy as well as a thing called the racing line; which I won't go much into detail but basically means driving on an optimised path to get the best results; and that path may or may not be the center of the track. 
Thus this results in a broken graph or track layout; something similar to this:

![Figure_1](https://user-images.githubusercontent.com/82220795/177355519-d2c45b05-34c4-48eb-a2cb-881002d11be1.jpg)
 
Thus we aim to fix that little gap and remove the excess data that is collected after the lap is finished.

## Results
The logic I applied to solve this was that setting up a threshold value for the distances between the origin and the points. 

Along with this, the main filtering logic was that the starting point (in this case, the origin) and the actual ending point would coincide. So I took the coordinates that had the X coordinae as 0 since Y could vary depending upon the direction of the incoming driver. This co-ordinate would also satisfy the thresh since it is close to the origin, just not coinciding perfectly, and made all the remaining co-ordinates after this point as 0 which got rid of the excess data collected.

Thus the final result come out to be like this:

![Figure_2 (2)](https://user-images.githubusercontent.com/82220795/177358061-e6ce3073-764c-439f-ad8f-b00c86e266f9.jpg)
