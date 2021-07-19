
function initialize(box)

	io.write("initialize has been called\n");


	dofile(box:get_config("${Path_Data}") .. "/plugins/stimulation/lua-stimulator-stim-codes.lua")

	number_of_trials = box:get_setting(2)
	cross_duration = box:get_setting(3)
	imagerie_duration = box:get_setting(4)



end

function process(box)

	local t=0

	-- manages baseline


	box:send_stimulation(1, OVTK_StimulationId_ExperimentStart, t, 0)

	t = t+ cross_duration
	



	for i = 1, number_of_trials do
		box:send_stimulation(1, OVTK_GDF_Start_Of_Trial, t, 0)
		
		box:send_stimulation(1, OVTK_GDF_Cross_On_Screen, t, 0) -- fixation cross
		t = t+ cross_duration 

		box:send_stimulation(1, OVTK_GDF_Stage_1, t, 0) -- video 
		t = t+ imagerie_duration 		

		box:send_stimulation(1, OVTK_GDF_End_Of_Trial, t, 0)

		t = t + math.random(1, 3)


	end



	t = t+ cross_duration

	-- used to cause the acquisition scenario to stop
	box:send_stimulation(1, OVTK_StimulationId_ExperimentStop, t, 0)

end
