# Author: Ryan Bagnulo @iryanb 
# SCA Lift Status Operational Management API client application emulator
# Copyright 2018 All Rights Reserved. guarden.io 
# Usage License: MIT

require 'rest-client'
#require "net/http"
require 'json'
require 'optparse'
require 'time'

gettime = Time.now

puts gettime.to_s

n=0      
# increase the below number to simulate more concurrent user requests                                                      
5.times do                                                          

responseMsg = RestClient.get "http://p0st3r.gateway.akana.com/SCA/v0/IntelligentAgent/lifts", 'Accept'=>"application/json"
responseMsgparsed = JSON.parse(responseMsg)
fieldA = responseMsgparsed[0]["LiftVibrationHz"]
fieldB = responseMsgparsed[1]["LiftVibrationHz"]
fieldC = responseMsgparsed[2]["LiftVibrationHz"]

n=n+1

#parsed
#puts n.to_s + " Response Message "  + fieldA + " " + fieldB + " " + fieldC 

puts n.to_s + " Response Message " + responseMsgparsed.to_s 
puts "************** PARSED JSON FIELD ****************"
puts n.to_s + " Vibration (Hz), Lift 1 = " + fieldA.to_s + ", Lift 2 = " + fieldB.to_s + ", Lift 3 = " + fieldC.to_s 

end                                                                  

elapsed = Time.now - gettime

puts "Completed " + n.to_s + " api requests " + " in " + elapsed.to_s + " seconds." 

puts "The Time now is " + Time.now.to_s 
