import cv2
import time


class MyOVBox(OVBox):
	def __init__(self):
		OVBox.__init__(self)
		
	def initialize(self):

		#This function start at the beguining of the openvibe scenario

		cv2.namedWindow('Frame', cv2.WINDOW_KEEPRATIO) # Allow to dont strech the image/video
		cv2.setWindowProperty('Frame',cv2.WND_PROP_ASPECT_RATIO,cv2.WINDOW_KEEPRATIO) 
		cv2.setWindowProperty('Frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN) #Display the image/video in full screen


		self.experience_visu = Visualisation()
		return

		
		# nop

		
	def process(self):



		for chunkIndex in range( len(self.input[0]) ):
			chunk = self.input[0].pop()
			if(type(chunk) == OVStimulationSet):
				# We move through all the stimulation received in the StimulationSet 
				
				for stimIdx in range(len(chunk)):
					stim=chunk.pop();

					#Chosse the image/video in function of the stimulus

					if stim.identifier == OpenViBE_stimulation['OVTK_GDF_Cross_On_Screen']:
						self.experience_visu.frame_image("cross")
					elif stim.identifier == OpenViBE_stimulation['OVTK_GDF_Stage_1']: 
						self.experience_visu.frame_video("push" , vid_duration = 10)
					elif stim.identifier == OpenViBE_stimulation['OVTK_StimulationId_ExperimentStart']:
						self.experience_visu.frame_image("black")

					elif stim.identifier == OpenViBE_stimulation['OVTK_GDF_End_Of_Trial']:
						self.experience_visu.frame_image("black")

					elif stim.identifier == OpenViBE_stimulation['OVTK_StimulationId_ExperimentStop']:
						self.uninitialize()

			else:
				print ('Received chunk of type ', type(chunk), " looking for StimulationSet")
		

	def uninitialize(self):
		# Destroy the frame
		self.experience_visu.kill()

		return


class Timer(object):
	# Simple timer
	def __init__(self):
		self.tstart = time.time()

	def tic(self):
		""" restart the timer"""
		self.tstart = time.time()

	def toc(self):
		""" send duration (in seconds) """
		return (time.time() - self.tstart)


class Visualisation(object): 
	def __init__(self):

		# Import the image and video in the memory
		self.path = "C:/Users/david/Documents/1-STAGE/Programation/OpenVibe/example/media/"
		self.cross_im = cv2.imread(self.path+"cross.png")
		self.black_im = cv2.imread(self.path+"black_screen.png") 
		self.push_vid = cv2.VideoCapture(self.path + "push_vid.mp4")




	def frame_video(self, mode, vid_duration):

		chrono = Timer() #Initiate the timer
		eval("self."+ mode+ "_vid.set(cv2.CAP_PROP_POS_FRAMES, 0)") #Run the command in the string,  here restart the video at the beginning


		while chrono.toc()< vid_duration: # If Vid_duration is greater than the video duration the image will freeze on the last image until a new stimulis
				# Capture frame-by-frame
		
				ret, frame = eval("self."+ mode+ "_vid.read()")
		
				if ret == True:
			
					# Display the resulting frame
					cv2.imshow('Frame', frame) 
					if cv2.waitKey(33) & 0xFF == ord('q') : #Wait 33 ms before ending the loop, IF THE FPS IN THE VIDEO CHANGE YOU MUST CHANGE THIS
						break
				# Break the loop
				else:
					break
	
				
	def frame_image(self, image):
		""" display image """

		cv2.imshow('Frame',eval("self."+ image+ "_im"))
		cv2.waitKey(1)		# Here the image is display until there is a new stimulus


	def kill(self):
		self.push_vid.release() # Released the video from the memory
		cv2.destroyAllWindows()


box = MyOVBox()